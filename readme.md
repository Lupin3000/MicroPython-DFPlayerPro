# MicroPython Library for DFRobot: DFPlayer Pro - A mini

This repository contains the MicroPython UART library for the Fermion: DFPlayer Pro from DFRobot, as well as a very simple example of how to use it.

## Prerequisite

- [DFPlayer Pro](https://www.dfrobot.com/product-2232.html?tracking=Mszf2HlGMStAAKkFfhNgg3QhFFchlilhR47u9vXX9o9Ko6giJYRJQdmwZjbDIvMV)
- [ESP32](https://www.dfrobot.com/search-esp32.html?tracking=Mszf2HlGMStAAKkFfhNgg3QhFFchlilhR47u9vXX9o9Ko6giJYRJQdmwZjbDIvMV) (_MicroPython compatible device_)
- latest [VCP driver]( https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads) installed (_depending on used OS_)

## Installation

Clone this repository to your local computer. Optional install dependencies (_esptool, rshell, stubs_). Copy code from local to microcontroller.

```shell
# clone repository
$ git clone https://github.com/Lupin3000/MicroPython-DFPlayerPro.git

# change into local repository folder
$ cd MicroPython-DFPlayerPro/

# install python packages (optional)
$ pip3 install -r requirements.txt

# start rshell connection
$ rshell -p [SERIAL PORT]

# upload files and folder
/YOUR/LOCAL/PATH> cp main.py /pyboard/
/YOUR/LOCAL/PATH> cp -r lib/ /pyboard/
```

## Usage

```shell
# start the MicroPython REPL
/YOUR/LOCAL/PATH> repl
```

## Additional information

[DFRobot Wiki](https://wiki.dfrobot.com/DFPlayer_PRO_SKU_DFR0768)
