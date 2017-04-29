# DS18X20 Temperature Sensor Node

## Parts

* [NodeMCU][2] ESP8266 development board
* one temperature sensor **DS18B20** or **DS18S20**, recommended is the DS18B20,
see [Maximintegrated Application Note 4377][1] for details

## Schematic

![Schematic][0]

## Software

You will need to put Micropython on your NodeMCU. See [Getting started with
MicroPython on the ESP8266][3] on how to install it.

## Libraries

* [micropython-lib/umqtt.simple/umqtt/simple.py][4]


[0]: schematic.png
[1]: https://www.maximintegrated.com/en/app-notes/index.mvp/id/4377
[2]: http://nodemcu.com/index_en.html
[3]: https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html
[4]: https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/umqtt/simple.py