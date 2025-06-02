# VM Test

## Introduction

Use this test directory to create a local ARM64 virtual machine to confirm all of the required software can be installed and run.

This will not be exactly the same as a proper Raspberry Pi OS - it will not have all of the optimizations, for local dev work it is sufficient.

## Prerequisites

1. Install Required KVM and QEMU Packages on Linux Mint/Ubuntu

```
sudo apt update

sudo apt -y install \
  qemu-kvm \
  cloud-utils 

sudo apt -y install \
  libvirt-daemon-system \
  libvirt-clients \
  cloud-init \
  bridge-utils \
  virt-manager \
  guestfs-tools \
  qemu-system-arm \
  qemu-efi-aarch64 \
  ovmf \
  binfmt-support \
  qemu-user-static
```

2. Create the proper users and services.

```
sudo adduser $USER libvirt
sudo adduser $USER kvm
sudo adduser $USER libvirt-qemu
```
Note: If you need to reload for current session, run `exec su -l $USER` to ensure all group memberships are refreshed.  This will clear loaded environment variables that aren't persisted.

3.  Ensure the qemu and images folders are permissioned for the created users/groups:

```
sudo chown -R libvirt-qemu:kvm /var/lib/libvirt/images
sudo chown -R libvirt-qemu:kvm /var/lib/libvirt/qemu
sudo chmod -R 775 /var/lib/libvirt/images
sudo chmod -R 775 /var/lib/libvirt/qemu
```

This will allow you to manage all of the files as a regular user which is a member of these groups.

Note:  You may need to reboot or log-in again to ensure the group permissions have taken effect.  
A good way to test is to confirm you can write to to the directory successfully by running: `touch /var/lib/libvirt/images/test.img`

4. Start and Persist libvirt service:

`sudo systemctl enable --now libvirtd`

5. Check that KVM support is enabled

`kvm-ok`

## Configure Networking

1. Set the host networking to use NAT rather than Bridge:

`virsh net-edit default`

The XML file should look similar to follows - the **forward mode** line will need to be added:

```
<network>
  <name>default</name>
  <uuid>d5613f4d-a454-493d-9a0f-57303b5f6a17</uuid>
  <forward mode='nat'/>
  <bridge name='virbr0' stp='on' delay='0'/>
  <mac address='52:54:00:2c:f0:3c'/>
  <ip address='192.168.122.1'>
    <dhcp>
      <range start='192.168.122.2' end='192.168.122.254'/>
    </dhcp>
  </ip>
</network>
```

2. Restart the virtual network:

```
virsh net-destroy default
virsh net-start default
```

3.  Confirm the network settings are active and correct:

```
virsh net-list
virsh net-dumpxml default
```

## Create cloud-init and launch VM

Note:  I've created a **buildvm.sh** to automate this process.  This section explains how this works.

1. Download Debian Bookworm ARM64 Cloud Image:

`wget https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-generic-arm64.qcow2`

Copy images to /var/lib/libvirt/images

2. Create cloud-init configuration:
* Uses cloud-init/user-data file configuration - add SSH keys.  **Note: The copy of the file in this repo includes my public key, so replace it with yours**
* Ensure cloud-init/meta-data file exists

Generate cloud-init ISO:

```
genisoimage -output debian12-cloud-init.iso -volid cidata -joliet -rock cloud-init/user-data cloud-init/meta-data
cp debian12-cloud-init.iso /var/lib/libvirt/images
```

**Note:**  TThe created user is "sysadmin" and the hashed SHA-512 password is "sysadmin", created via `mkpasswd --method=SHA-512 --rounds=4096 --salt=MCEqDm9nbk9Mk5Zl`.

`Value: $6$rounds=4096$MCEqDm9nbk9Mk5Zl$pIA0130Pwhbhx2NmYJJ30TRi5o/weADIEAytk.2NsS454klh.Uy4Voa9XO8.9W1MA0uX3FrfPaQCbnfhQpCFd0`

3. Create and start emulated ARM64/AARCH64 VM that boots the cloud-init.iso for configuration:

```
virt-install \
  --name debian12-arm64 \
  --os-variant debian12 \
  --arch aarch64 \
  --machine virt \
  --cpu cortex-a72 \
  --memory 16384 \
  --vcpus 4 \
  --disk path=/var/lib/libvirt/images/debian-12-generic-arm64.qcow2,format=qcow2,bus=virtio \
  --cdrom /var/lib/libvirt/images/debian12-cloud-init.iso \
  --network network=default,model=virtio \
  --graphics none \
  --boot hd \
  --console pty,target_type=serial
  ```

## Destroy VM

See **delevevm.sh** for automation script.

```
virsh shutdown debian12-arm64
virsh destroy debian12-arm64
virsh undefine debian12-arm64 --nvram --remove-all-storage
rm /var/lib/libvirt/images/debian12-cloud-init.iso
```

Notes:
* The nvram must be removed before recreating the VM, which can be done by deleting the values in `/var/lib/libvirt/qemu/nvram`, or using the switches above.
* This also deletes the built cloud-init ISO so it can be recreated to pick up changes.


## Helpful commands:

* Use `CTRL + ]` to exit the VM console.
* List all VMs: `virsh list --all`
* Show IP addresses for VM: `virsh domifaddr debian12-arm64`
* Start and stop the VM: `virst start debian12-arm64`
* Connect to the VM Console: `virsh console debian12-arm64`

## Troubleshooting

List networks and dump the default network info:
```
virsh net-list
virsh net-dumpxml default
```

Validate user-data schema while inside the VM:

`sudo cloud-init schema --system --annotate`