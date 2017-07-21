# BME280 - temperature, humidity and pressure node

Measure temperature, humidity and pressure with one sensor.

## Hardware components

* [NodeMCU][4] ESP8266 development board
* [BME280 I2C/SPI temperature, humidity, pressure sensor][5]

![Assembly][3]

## Schematic

![Schematic][2]

## MQTT message scheme

For each measurment cycle three messages will be sent with 500ms delay each.

* `{MQTT_TOPIC}/temp`

| parameter      | value             |  description                 |
|----------------|-------------------|------------------------------|
|name            |`temperature`      |                              |
|value           |                   |current temperature value     |
|unit            |`C`                |degrees celsius               |

* `{MQTT_TOPIC}/pressure`

| parameter      | value             |  description                 |
|----------------|-------------------|------------------------------|
|name            |`pressure`         |                              |
|value           |                   |current pressure value        |
|unit            |`bar`              |                              |

* `{MQTT_TOPIC}/humidity`

| parameter      | value             |  description                 |
|----------------|-------------------|------------------------------|
|name            |`humidity`         |                              |
|value           |                   |current humidity value        |
|unit            |`pct`              |percent                       |



[0]: https://github.com/catdog2/mpy_bme280_esp8266
[1]: https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
[2]: schematic.png
[3]: assembly.png
[4]: http://nodemcu.com/index_en.html
[5]: https://www.adafruit.com/product/2652
