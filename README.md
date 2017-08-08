# ESP8266 IOT Nodes 

A collection of IoT clients based on the famous ESP8266 microcontroller 
(aka [NodeMCU][0]) using the [Micropython][1] programming language. All clients
use the [MQTT protocol][2] for data exchange. MQTT is a light-weight 
machine2machine protocol supporting publish/subscribe messaging transport.

## Hardware Installation

Each node has a recommended hardware setup which you can find in its README 
file. However it is completely up to you to change the layout, extend more 
sensors or install additional features.

## Software Installation

1. Install Micropython on your ESP8266 NodeMCU prototyping board. There is a 
very comprehensive guide available on [micropython.org][3] that uses the software
[esptool][5] to erase the flash and install the latest Micropython firmware. Please follow the
[instruction set][3].
2. Connect to your Node using a REPL. [mpfshell][4] is a good choice here. You
can also use the [WebREPL][6] if you like, but make sure your node is connected to
Wifi and WebREPL is activated.
3. Transfer the necessary files for the node of your choice on your device


## Nodes

| Node name        | description                              | 
| ---------------- | ---------------------------------------- |
| [BME280][7]      | humidity, temperature, pressure sensor   |
| [FS1000A][8]     | radio controlled power switch            |
| [DS18X20][9]     | digital temperature sensor               |
| [HC-SR501][10]   | passive infrared motion sensor           |
| [moisture][11]   | soil moisture sensor                     |

[0]: http://nodemcu.com/index_en.html
[1]: https://docs.micropython.org/en/latest/esp8266/index.html
[2]: http://mqtt.org/
[3]: https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html
[4]: https://github.com/wendlers/mpfshell
[5]: https://github.com/espressif/esptool
[6]: http://micropython.org/webrepl/
[7]: https://github.com/MrLeeh/esp8266_iot_nodes/tree/master/nodes/bme280
[8]: https://github.com/MrLeeh/esp8266_iot_nodes/tree/master/nodes/fs1000a
[9]: https://github.com/MrLeeh/esp8266_iot_nodes/tree/master/nodes/ds18x20
[10]: https://github.com/MrLeeh/esp8266_iot_nodes/tree/master/nodes/hc_sr501
[11]: https://github.com/MrLeeh/esp8266_iot_nodes/tree/master/nodes/moisture
