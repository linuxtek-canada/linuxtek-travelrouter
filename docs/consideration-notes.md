# Consideration Notes

## Build Considerations
* Looked at using [packer-plugin-arm-image](https://github.com/solo-io/packer-plugin-arm-image) to create a custom image to flash to the Raspberry Pi, however [this issue](https://github.com/solo-io/packer-plugin-arm-image/issues/171) indicates it is broken after Packer 1.11.0.
* Raspberry Pi has new [rpi-image-gen](https://github.com/raspberrypi/rpi-image-gen) tool to build a custom RPI image to flash:
  - [YouTube - Build Custom Raspberry Pi Images with rpi-image-gen: Step-By-Step Guide](https://www.youtube.com/watch?v=kxl_swm93XE)

## Boot and Setup Considerations
* To use NVME boot device, must first set boot order and enable PCIe. See [Jeff Geerling's Article](https://www.jeffgeerling.com/blog/2023/nvme-ssd-boot-raspberry-pi-5)

## Power Considerations
* Do NOT connect the Power supply to USB-C on Raspberry Pi 5 when you are using PoE+ Hat as a power supply, it may damage your device !!!
* 52Pi POE Hat only provides 25W at 5.1V/4.5A which is not the full 5A, so it may not fully power the unit - you will likely get warning messages regarding power draw.
* Potentially battery powered via USB-C.  Source must be able to provide stable 5V/5A DC power.
* Raspberry Pi 5 power button is connected to one of the [SoC GPIOs](https://github.com/raspberrypi/linux/blob/6137fb168c08bd8c41c8421bf26f09ed29479f08/arch/arm/boot/dts/bcm2712-rpi-5-b.dts#L447) which Linux monitors. Pressing initiates shutdown. Holding for 5 seconds is a hard power off.

## Network Considerations
* [Raspberry Pi 5 Wi-Fi Supported Chipsets](https://github.com/morrownr/USB-WiFi/tree/main)
* Need two Wi-Fi devices - connect to external Wi-Fi, and create own AP for private connections.
* Will need remote access to GUI to navigate captive portal.  Currently RaspAP does not have a solution - [feature request](https://github.com/RaspAP/raspap-webgui/issues/1419).
* Configure RJ45 on Raspberry Pi for direct 1Gbps laptop connection.
* Option to use USB-A to RJ45 for external WAN connection.

## Software Considerations
* Looked at RetroPie and EmulationStation for emulation options, but they have not been updated in a long time. 
* [Recalbox](https://gitlab.com/recalbox/recalbox) is currently maintained, but no Docker based install available.
* Apache Guacamole - Web Based Remote Desktop - [Website](https://guacamole.apache.org/). 
  - This would be helpful for accessing the Raspberry Pi GUI to handle captive portals, however there are no official arm64 images.
  - Will test deployment after initial install with GUI available.
* Can look at setting up Traefik for handling proper SSL/TLS, however this would be very custom and difficult for others to re-use. 

## Helpful References
* [Github - Awesome SelfHosted](https://github.com/awesome-selfhosted/)
* [Github - Homer Dashboard- Site Icons](https://github.com/homarr-labs/dashboard-icons)
