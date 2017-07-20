# DS18X20 Temperature Sensor Node

## Parts

* [NodeMCU][2] ESP8266 development board
* one temperature sensor **DS18B20** or **DS18S20**, recommended is the DS18B20,
see [Maximintegrated Application Note 4377][1] for details

![Assignment][0]

## Schematic

![Schematic][5]

You will need to put Micropython on your NodeMCU. See [Getting started with
MicroPython on the ESP8266][3] on how to install it.

## Modules

* ``core.py``
* ``config.py``
* ``boot.py``
* ``main.py``
* [``umqtt/simple.py``][4] from Micropython Library

## Configuration

The configuration is done in the config.py. The following tables show you all of
the configuration values. Import is that you setup wifi connection credentials
and the mqtt server. You don't need to supply ``MQTT_USER`` and
``MQTT_PASSWORD`` if you haven' t enabled authentification on your MQTT broker.
However it is recommended to do so to prevent others from intruding.

### config.py

| name                  | description                                                                 | default value        |
| --------------------- | --------------------------------------------------------------------------- |:--------------------:|
| ``WIFI_SSID``         | SSID of the wifi you want to connect to                                     | -                    |
| ``WIFI_PASSWORD``     | Password for your wifi access                                               | -                    |
| ``MQTT_SERVER``       | Address of your mqtt broker                                                 | ``"localhost"``      |
| ``MQTT_PORT``         | Port of your mqtt broker (default=1883, ssl=8883)                           | ``1883``             |
| ``MQTT_USER``         | Username for the mqtt broker                                                | -                    |
| ``MQTT_PASSWORD``     | Only needed if a username is given                                          | -                    |
| ``MQTT_SSL``          | Use ssl connection to the broker. Set port to 8883 if using this.           | -                    |
| ``MQTT_CERFILE``      | If you have a certfile for your ssl connection supply the filename here.    | -                    |
| ``MQTT_CLIENT_ID``    | mqtt client id of the node                                                  | ``"umqtt_client"``   |
| ``MQTT_TOPIC``        | mqtt topic to use for publishing the measurement values                     | -                    |
| ``ONEWIRE_PIN``       | the pin nr. of the NodeMCU where the temperature sensor is connected to     | 0                    |
| ``ENABLE_DEEPSLEEP``  | if enabled the NodeMCU goes into deepsleep after execution to save power. The sleeptime is set by ``SLEEP_TIME_S``| True |
| ``SLEEP_TIME_S``      | time between two measurements                                               | 60                   |

[0]: assignment.png
[1]: https://www.maximintegrated.com/en/app-notes/index.mvp/id/4377
[2]: http://nodemcu.com/index_en.html
[3]: https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html
[4]: https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/umqtt/simple.py
[5]: schematic.png
