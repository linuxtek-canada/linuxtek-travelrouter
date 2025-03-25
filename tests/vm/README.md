# VM Test

## Introduction

Use this test to create a local ARM64 virtual machine to confirm all of the required software can be installed and run.

## Prerequisites


1. Install Required KVM and QEMU Packages on Linux Mint/Ubuntu:

```
sudo apt update
sudo apt-get -y install \
    qemu-kvm \
    libvirt-daemon-system \
    libvirt-clients \
    cloud-init \
    bridge-utils \
    virt-manager \
    qemu-system-arm \
    qemu-efi-aarch64 \
    ovmf \ 
    cloud-utils \
    binfmt-support \
    qemu-user-static

sudo adduser $USER libvirt
sudo adduser $USER kvm
sudo adduser $USER libvirt-qemu

# Start and Persist libvirt service
sudo systemctl enable --now libvirtd 

# Reset to allow different pulling containers for different architectures 
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes 

# Check that KVM support is enabled
kvm-ok 
```

Note: if you need to reload for current session, run `exec su -l $USER` to ensure all group memberships are refreshed.  This will clear loaded environment variables that aren't persisted.


2. Download Debian Bookworm ARM64 Cloud Image:

`wget https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-generic-arm64.qcow2`

Copy images to /var/lib/libvirt/images

3. Create cloud-init configuration:

a. Uses cloud-init/user-data file configuration - add SSH keys
b. Ensure cloud-init/meta-data file exists
c. Generate cloud-init ISO:

`genisoimage -output cloud-init.iso -volid cidata -joliet -rock cloud-init/user-data cloud-init/meta-data`

Note:  The hashed SHA-512 default password is "debian", created via `mkpasswd --method=SHA-512 --rounds=4096`.

4.  Clone the qcow2 VM disk to use, then resize:

```
qemu-img convert -O qcow2 debian-12-generic-arm64.qcow2 debian12-vm.qcow2
qemu-img resize debian12-vm.qcow2 32G
```

4. Run Emulated ARM64/AARCH64 VM that boots the cloud-init.iso for configuration

```
virt-install \
  --debug \
  --name debian12-arm64 \
  --os-variant debian12 \
  --arch aarch64 \
  --machine virt \
  --cpu cortex-a76 \
  --memory 16384 \
  --vcpus 4 \
  --disk path=/var/lib/libvirt/images/debian-12-generic-arm64.qcow2,size=32,format=qcow2,bus=virtio \
  --cdrom /var/lib/libvirt/images/cloud-init.iso \
  --network bridge=virbr0,model=virtio \
  --graphics none \
  --console pty,target_type=serial
  ```

5.  Helpful commands:

```
virsh list --all
virsh domifaddr debian12-arm64
```
- Created buildvm.sh and deletevm.sh to automate quick build/delete
- Testing cloud-init

## 