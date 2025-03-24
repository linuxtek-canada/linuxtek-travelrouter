# linuxtek-travelrouter
Details and configuration for LinuxTek TravelRouter build.

## Introduction

## Hardware Bill of Materials
* Raspberry Pi 5 16GB - [PiShop.ca](https://www.pishop.ca/product/raspberry-pi-5-16gb/)
* Wi-Fi Dongle - FENVI WIFI6 FU-AX1800 USB Dongle - [AliExpress](https://www.aliexpress.com/item/1005005935638503.html)
* Official Raspberry Pi 27W USB-C Power Supply - [PiShop.ca](https://www.pishop.ca/product/raspberry-pi-27w-usb-c-power-supply-black-us/)
* 52Pi Aluminum Case for Raspberry Pi 5, With Official Active Cooler + P33 M.2 NVMe M-Key PoE+ HAT - [52Pi](https://52pi.com/products/52pi-aluminum-case-for-raspberry-pi-5-with-official-active-cooler-p33-m-2-nvme-m-key-poe-hat?variant=45639566852248)


    - 52Pi M.2 NVME M-KEY POE+ Hat with Official Pi 5 Active Cooler for Raspberry Pi 5 - [52Pi](https://52pi.com/collections/hat-addons/products/m-2-nvme-m-key-poe-hat-with-official-pi-5-active-cooler-for-raspberry-pi-5-support-m-2-nvme-ssd-2230-2242)
    - 52Pi Aluminum Case Black Brick Enlosure With Cooling Fan Heatsink for Raspberry Pi 5 - [52Pi](https://52pi.com/collections/cases/products/case-for-raspberry-pi-5)

## Software Bill of Materials
* Raspberry Pi Image Generator - rpi-image-gen - [Github](https://github.com/raspberrypi/rpi-image-gen)
* Raspberry Pi Imager - [Website](https://www.raspberrypi.com/software/)

## Software to install

* RaspAP - Debian based wireless router software - [Website](https://raspap.com/)
* Jellyfin - Free Software Media System - [Website](https://jellyfin.org/)
* PLEX - Web Media Playback 
* EmulationStation - Retro Video Game Emulation - [Website](https://emulationstation.org/)
* Apache Guacamole - Web Based Remote Desktop - [Website](https://guacamole.apache.org/)
* PiHole - Network-wide Ad Blocking - [Website](https://pi-hole.net/)
* Portainer - Container Management Software - [Website](https://www.portainer.io/)
* Heimdall - Application Dashboard - [Website](https://heimdall.site/)

## RaspAP OS

* [Website Link](https://raspap.com/)
* Full-featured wireless router setup for Debian-based devices.
* Custom Raspberry Pi OS Lite images with the latest RaspAP are available for [direct download](https://github.com/RaspAP/raspap-webgui/releases/latest). This includes both 32-bit and 64-bit builds for ARM architectures.
* [Example Setup Article](https://connectwithutkarshsingh.medium.com/how-to-turn-your-raspberry-pi-into-a-secure-travel-router-138377eb7e02)

## Other Considerations
* Potentially battery powered via USB-C.  Source must be able to provide stable 5V/5A DC power.
* Shutdown button to be able to halt safely without SSH/web login, or hard disconnecting power source.
* Need two Wi-Fi devices - connect to external Wi-Fi, and create own AP for private connections.
* Will need remote access to GUI to navigate captive portal.  Currently RaspAP does not have a solution - [feature request](https://github.com/RaspAP/raspap-webgui/issues/1419).
* Configure RJ45 on Raspberry Pi for direct 1Gbps laptop connection.
* Option to use USB-A to RJ45 for external WAN connection.
* To use NVME boot device, must first set boot order and enable PCIe. See [Jeff Geerling's Article](https://www.jeffgeerling.com/blog/2023/nvme-ssd-boot-raspberry-pi-5)





## Usage

1.  Clone this repository: `git clone https://github.com/linuxtek-canada/linuxtek-travelrouter.git`
2.  Initialize the rpi-image-gen submodule: `git submodule update --init --recursive`

## References
* [2025 Build Custom Raspberry Pi Images with rpi-image-gen: Step-By-Step Guide](https://www.youtube.com/watch?v=kxl_swm93XE)
    - [GitHub - rpi-imagegen-example](https://github.com/jonnymacs/rpi-image-gen-example)
* [Wi-Fi Supported Chipsets](https://github.com/morrownr/USB-WiFi/tree/main)
