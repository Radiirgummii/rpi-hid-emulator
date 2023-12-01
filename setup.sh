#! /bin/bash

# enable kernal modules
echo "dtoverlay=dwc2" | tee -a /boot/config.txt
echo "dwc2" | tee -a /etc/modules 
echo "libcomposite" | tee -a /etc/modules




mv ./config/isticktoit_usb /usr/bin/isticktoit_usb # move device configuration script to final location
chmod +x /usr/bin/isticktoit_usb # make device configuration script executable

mv ./config/rc.local # configure device configuration script to start on startup

