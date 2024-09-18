# rpi-hid-emulator
this is one of my first github repos so please be respectful

the focus of this projekt is to provide a simple hid interface primarilly desined to work on the RaspberryPi lineup od devices

## Tested devices:
- RaspberryPi 4B

## Installation
prepare an installation of RaspberrypiOS Lite

boot your device

connect to pi via ssh:

`ssh [user]@[hostname]`

type in your password

if you haven't changed your configuration you can type:

`ssh pi@raspberrypi`

clone the github repository:

`git clone https://github.com/Radiirgummii/rpi-hid-emulator.git`

navigate into repository:

`cd rpi-hid-emulator`

run setup script:

`sudo ./setup.sh`

shutdown your pi:

`sudo shutdown`

Now you've finished setting up continue with the usage section

## Usage

now that you have set up your pi you can use the pi as an hid device

first you have to plug it in to the computer you want to control you have to use the USB-C port wich is usualy power only.
This port acts as the usb slave device. the pi should boot with the Computer. you can also plug it in while the computer is running.

now you have to connect to your pi again via ssh:

`ssh [user]@[hostname]`

navigate into the repo:

`cd rpi-hid-emulator`

now you can try out the exaple script(the script is designed for a Windows PC, and a German keyboard):

`sudo python example.py`

## planned features
| Feature                                 | Status     |
|-----------------------------------------|------------|
| single key encoder                      | testing    |
| lowercase text encoding                 | testing    |
| full text encoding with automatic shift | WIP        |

for feature requests please open an issue
