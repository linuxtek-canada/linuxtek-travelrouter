# raspap-travel
Details and configuration for RaspAP Travel Router build.

## Bill of Materials
* Raspberry Pi 3B
* Wi-Fi Dongle
* Battery Backup

## Wi-Fi Supported Chipsets
* https://github.com/morrownr/USB-WiFi/tree/main

## Hardware

* [Case/POE/NVME](https://52pi.com/products/52pi-aluminum-case-for-raspberry-pi-5-with-official-active-cooler-p33-m-2-nvme-m-key-poe-hat?variant=45639566852248) - 52Pi Aluminum Case for Raspberry Pi 5, With Official Active Cooler + P33 M.2 NVMe M-Key PoE+ HAT
* [DeskPi Lite for Raspberry Pi 5](https://52pi.com/products/deskpi-lite-for-raspberry-pi-5-with-power-button-heatsink-with-armor-lite-v5-fan-dual-full-size-hdmi-support-m-2-nvme-ssd?variant=45713729224856)

Started looking at options for cases, and to upgrade to newer Raspberry Pi 5 for increased network throughput, and more options.  Since one of the considerations was for a power button, the Raspberry Pi 5 includes this, and the DeskPi case makes it more convenient to hook up to a hotel TV when travelling.


## RaspAP OS

* [Website Link](https://raspap.com/)
* Full-featured wireless router setup for Debian-based devices.
* Custom Raspberry Pi OS Lite images with the latest RaspAP are available for [direct download](https://github.com/RaspAP/raspap-webgui/releases/latest). This includes both 32-bit and 64-bit builds for ARM architectures.
* [Example Setup Article](https://connectwithutkarshsingh.medium.com/how-to-turn-your-raspberry-pi-into-a-secure-travel-router-138377eb7e02)

## Other Considerations
* Battery powered via USB
* Need shutdown button to be able to halt safely without SSH/web login
* Need two Wi-Fi devices - connect to captive portal and then create own AP for private connections.
* Can also have option to use RJ45 port for wired WAN hookup.

