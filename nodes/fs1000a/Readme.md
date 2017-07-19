# FS1000A radio transmitter

The FS1000A is a very cheap 433MHz transmitter with receiver kit. It can be used 
for simple remote-controlled switches.

## Components

* [NodeMCU][2] ESP8266 development board
* 9V battery for increased signal range
* FS1000A radio transmitter

![Assignment][1]

## Schematic 

![Schematic][0]

## Configuration

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

[0]: schematic.png
[1]: assignment.png
[2]: http://nodemcu.com/index_en.html
