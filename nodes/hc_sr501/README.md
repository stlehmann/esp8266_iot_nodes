# HC-SR501 passive infrared motion sensor

## Components

* [NodeMCU][2] ESP8266 development board
* [HC-SR501 pir sensor][2]

![Assembly][0]

[0]: assembly.png
[1]: https://www.mpja.com/download/31227sc.pdf
[2]: http://nodemcu.com/index_en.html

## MQTT message schema

* `{MQTT_TOPIC}/out` 

| parameter      | value             |  description                    |
|----------------|-------------------|---------------------------------|
|name            |`motion`           |                                 |
|value           |True / False       |True if motion currently detected|
