# RaspAP

## Details

* [Website Link](https://raspap.com/)
* Full-featured wireless router setup for Debian-based devices.
* Custom Raspberry Pi OS Lite images with the latest RaspAP are available for [direct download](https://github.com/RaspAP/raspap-webgui/releases/latest). This includes both 32-bit and 64-bit builds for ARM architectures.
* [Example Setup Article](https://connectwithutkarshsingh.medium.com/how-to-turn-your-raspberry-pi-into-a-secure-travel-router-138377eb7e02)

## SD Card - Minimal Write
If you will be running the Travel Router on the MicroSD card, the frequent disk writes may accelerate the card lifespan.  RaspAP has configuration options for a [Minimal SD Write](https://docs.raspap.com/minwrite/?h=minimal) which may want to be implemented.

## Networking

* Based on: https://docs.raspap.com/defaults/?h=network#networking-defaults
* RaspAP Configuration Files are in /etc/raspap/networking
* Will need to swap the Wi-Fi adapters to use the external USB module for WPA3