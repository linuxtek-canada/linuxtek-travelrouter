#!/bin/bash

if [ ! -f debian-12-generic-arm64.qcow2 ]; then
  wget https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-generic-arm64.qcow2
fi

# Clean up previous files
rm /var/lib/libvirt/images/debian12-cloud-init.iso
rm /var/lib/libvirt/images/debian-12-generic-arm64.qcow2

# Recreate/copy cloud-init and image
genisoimage -o /var/lib/libvirt/images/debian12-cloud-init.iso \
  -volid cidata \
  -joliet \
  -rock \
  cloud-init/user-data \
  cloud-init/meta-data

cp ./debian-12-generic-arm64.qcow2 /var/lib/libvirt/images

# Create the virtual machine
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