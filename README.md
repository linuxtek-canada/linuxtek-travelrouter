# raspap-travel
Details and configuration for RaspAP Travel Router build.

## Bill of Materials
* Raspberry Pi 3B
* Wi-Fi Dongle
* Battery Backup

## Wi-Fi Supported Chipsets
* https://github.com/morrownr/USB-WiFi/tree/main


## RaspAP OS

* [Website Link](https://raspap.com/)
* Full-featured wireless router setup for Debian-based devices.
* Custom Raspberry Pi OS Lite images with the latest RaspAP are available for [direct download](https://github.com/RaspAP/raspap-webgui/releases/latest). This includes both 32-bit and 64-bit builds for ARM architectures.
* [Example Setup Article](https://connectwithutkarshsingh.medium.com/how-to-turn-your-raspberry-pi-into-a-secure-travel-router-138377eb7e02)
## Considerations
* Battery powered via USB
* Need shutdown button to be able to halt safely without SSH/web login
* Need two Wi-Fi devices - connect to captive portal and then create own AP for private connections.
* Can also have option to use RJ45 port for wired WAN hookup.
* 

