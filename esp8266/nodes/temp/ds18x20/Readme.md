# DS18X20 Temperature Sensor Node

## Parts

* [NodeMCU][2] ESP8266 development board
* one temperature sensor **DS18B20** or **DS18S20**, recommended is the DS18B20,
see [Maximintegrated Application Note 4377][1] for details

![Schematic][0]

You will need to put Micropython on your NodeMCU. See [Getting started with
MicroPython on the ESP8266][3] on how to install it.

## Modules

* ``core.py``
* ``credentials.py``
* ``boot.py``
* ``main.py``
* [``umqtt/simple.py``][4] from Micropython Library

## Configuration

### main.py

| name                  | description                   | default value |
| --------------------- | ----------------------------- |:-------------:|
| ``MQTT_CLIENT_ID``    | mqtt client id of the node    | ``"ds18x20"``   |
| ``MQTT_TOPIC``        | mqtt topic to use for publishing the measurement values | ``"home/temp"`` |
| ``ONEWIRE_PIN``       | the pin nr. of the NodeMCU where the temperature sensor is connected to | 0 |
| ``ENABLE_DEEPSLEEP``  | if enabled the NodeMCU goes into deepsleep after execution to save power. The sleeptime is set by ``SLEEP_TIME_S``| True | | ``SLEEP_TIME_S``      | time between two measurements | 60 |

[0]: schematic.png
[1]: https://www.maximintegrated.com/en/app-notes/index.mvp/id/4377
[2]: http://nodemcu.com/index_en.html
[3]: https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html
[4]: https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/umqtt/simple.py