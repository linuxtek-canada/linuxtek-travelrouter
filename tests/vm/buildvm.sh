#!/bin/bash

if [ -f /var/lib/libvirt/images/debian-12-generic-arm64.qcow2 ]; then
  rm /var/lib/libvirt/images/debian-12-generic-arm64.qcow2
fi
cp ./debian-12-generic-arm64.qcow2 /var/lib/libvirt/images

virt-install \
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