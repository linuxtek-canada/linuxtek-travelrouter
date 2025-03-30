# VM Test

## Introduction

Use this test to create a local ARM64 virtual machine to confirm all of the required software can be installed and run.

## Prerequisites

1. Install Required KVM and QEMU Packages on Linux Mint/Ubuntu

```
sudo apt update
sudo apt-get -y install \
    qemu-kvm \
    libvirt-daemon-system \
    libvirt-clients \
    cloud-init \
    bridge-utils \
    virt-manager \
    guestfs-tools \
    qemu-system-arm \
    qemu-efi-aarch64 \
    ovmf \ 
    cloud-utils \
    binfmt-support \
    qemu-user-static
```

2. Create the proper users and services.

```
sudo adduser $USER libvirt
sudo adduser $USER kvm
sudo adduser $USER libvirt-qemu
```

3.  Ensure the qemu and images folders are permissioned for the created users/groups:

# Start and Persist libvirt service
sudo systemctl enable --now libvirtd 

# Reset to allow different pulling containers for different architectures 
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes 

# Check that KVM support is enabled
kvm-ok 
```

Note: if you need to reload for current session, run `exec su -l $USER` to ensure all group memberships are refreshed.  This will clear loaded environment variables that aren't persisted.

## Configure Networking

1. Set the host networking to use NAT rather than Bridge

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

3.  Restart the network:
Restart the virtual network:
```
virsh net-destroy default
virsh net-start default
```

4.  Confirm the network settings are active and correct:
```
virsh net-list
virsh net-dumpxml default
```

## Set up Image and cloud-init

1. Download Debian Bookworm ARM64 Cloud Image:

`wget https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-generic-arm64.qcow2`

Copy images to /var/lib/libvirt/images

2. Create cloud-init configuration:

a. Uses cloud-init/user-data file configuration - add SSH keys
b. Ensure cloud-init/meta-data file exists
c. Generate cloud-init ISO:

```
genisoimage -output debian12-cloud-init.iso -volid cidata -joliet -rock cloud-init/user-data cloud-init/meta-data
cp debian12-cloud-init.iso /var/lib/libvirt/images
```

Note:  The hashed SHA-512 password is "debian", created via `mkpasswd --method=SHA-512 --rounds=4096 --salt=MCEqDm9nbk9Mk5Zl`.

# Value: $6$rounds=4096$MCEqDm9nbk9Mk5Zl$pIA0130Pwhbhx2NmYJJ30TRi5o/weADIEAytk.2NsS454klh.Uy4Voa9XO8.9W1MA0uX3FrfPaQCbnfhQpCFd0


## Create the VM

1. Run Emulated ARM64/AARCH64 VM that boots the cloud-init.iso for configuration

```
virt-install \
  --name debian12-arm64 \
  --os-variant debian12 \
  --arch aarch64 \
  --machine virt \
  --cpu cortex-a76 \
  --memory 16384 \
  --vcpus 4 \
  --disk path=/var/lib/libvirt/images/debian-12-generic-arm64.qcow2,size=32,format=qcow2,bus=virtio \
  --cdrom /var/lib/libvirt/images/debian12-cloud-init.iso \
  --network network=default,model=virtio \
  --graphics none \
  --boot hd \
  --console pty,target_type=serial
  ```

## Helpful commands:

Use `CTRL + ]` to exit the VM console.

```
# List all VMs
virsh list --all

# Show network addresses for VM
virsh domifaddr debian12-arm64

# Start and stop the VM
virst start debian12-arm64

# Connect to VM console
virsh console debian12-arm64
```
- Created buildvm.sh and deletevm.sh to automate quick build/delete
- Testing cloud-init

## Troubleshooting

List networks and dump the default network info:
```
virsh net-list
virsh net-dumpxml default
```

Validate user-data while inside the VM:

`sudo cloud-init schema --system --annotate`