# Moisture sensor node

The [Grove Moisture sensor][0] from Seed can be used for detecting the moisture
of soil or judge if there is water around the sensor. It is a low-cost sensor
based on resistive measuring.

## Operating principle

The Grove moisture sensor is based on the measuring of the resistance of the
soil it is digged in. If the soil is moist then the resistance will be low. If
the moist is low then resistance will be hight. The sensor uses provides an
analogue output that is read by the ESP8266 ADC input.

## MQTT message scheme

* `{MQTT_TOPIC}`

| parameter      | value             |  description                 |
|----------------|-------------------|------------------------------|
|name            |`moisture`         |                              |
|value           |                   |current moisture value        |
|unit            |`pct`              |moisture in percent           |


[0]: http://wiki.seeed.cc/Grove-Moisture_Sensor/
