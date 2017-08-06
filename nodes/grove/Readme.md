# Grove - moisture sensor node

The [Grove Moisture sensor][0] from Seed can be used for detecting the moisture
of soil or judge if there is water around the sensor. It is a low-cost sensor
based on resistive measuring.

## MQTT message scheme

* `{MQTT_TOPIC}`

| parameter      | value             |  description                 |
|----------------|-------------------|------------------------------|
|name            |`moisture`         |                              |
|value           |                   |current moisture value        |
|unit            |`pct`              |moisture in percent           |


[0]: http://wiki.seeed.cc/Grove-Moisture_Sensor/
