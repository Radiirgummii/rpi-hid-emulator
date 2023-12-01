#! /bin/bash

# enable kernal modules
echo "dtoverlay=dwc2" | tee -a /boot/config.txt
echo "dwc2" | tee -a /etc/modules
echo "libcomposite" | tee -a /etc/modules



# configure device
mv ./config/isticktoit_usb /usr/bin/isticktoit_usb
chmod +x /usr/bin/isticktoit_usb
