# Moisture sensor node

The [Grove Moisture sensor][0] from Seed can be used for detecting the moisture
of soil or judge if there is water around the sensor. It is a low-cost sensor
based on resistive measuring.

## Operating principle

The Grove moisture sensor is based on the measuring of the resistance of the
soil it is digged in. If the soil is moist then the resistance will be low. If
the moist is low then resistance will be hight. The sensor uses provides an
analogue output that is read by the ESP8266 ADC input.

## Hardware components

For this assembly I wanted to use the smaller Wemos D1 mini board that's nearly
half the size of the NodeMCU. It fits nicely with the moisture sensor and offers
the possibility of putting everything together in a small housing.

* [Wemos D1 mini ESP8266 board][3]
* a resistive moisture sensor with an analogue output e.g. [Seeds Grove][4] or
  [Sparkfun Soil Moisture Sensor][5]

![Assembly][1]

## Schematic

![Schematic][2]

## MQTT message scheme

* `{MQTT_TOPIC}`

| parameter      | value             |  description                 |
|----------------|-------------------|------------------------------|
|name            |`moisture`         |                              |
|value           |                   |current moisture value        |
|unit            |`pct`              |moisture in percent           |


[0]: http://wiki.seeed.cc/Grove-Moisture_Sensor/
[1]: assembly.png
[2]: schematic.png
[3]: https://wiki.wemos.cc/products:d1:d1_mini
[4]: http://wiki.seeed.cc/Grove-Moisture_Sensor/
[5]: https://www.sparkfun.com/products/13322
