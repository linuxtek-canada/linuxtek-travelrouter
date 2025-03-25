#!/bin/bash

virsh shutdown debian12-arm64
virsh destroy debian12-arm64
virsh undefine debian12-arm64 --nvram --remove-all-storage