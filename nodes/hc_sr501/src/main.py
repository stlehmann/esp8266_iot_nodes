from config import config
import core
import utime
import ujson
import machine


state = False
t0 = 0


def motion_sens_callback(p):
    global state, t0
    if not state:
        payload = {
            'name': 'motion_state',
            'value': True 
        }
        mqtt.publish(
            config.MQTT_TOPIC + '/out', ujson.dumps(payload), qos=2
        )
    state = True
    t0 = utime.ticks_ms()


def run():

    global wifi, mqtt, sensor_pin, state, t0

    # Connect Wifi
    wifi = core.WifiWrapper(config)
    wifi.connect()

    # Connect MQTT
    mqtt = core.MQTTClientWrapper(config)
    mqtt.connect()

    # Init sensorpin
    sensor_pin = machine.Pin(config.PIN_SENSOR, machine.Pin.IN) 
    sensor_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_sens_callback)

    t0 = utime.ticks_ms()
    while True:
        utime.sleep(1)
        if abs(utime.ticks_ms() - t0) >= 10000:
            if state:
                payload = {
                    'name': 'motion_state',
                    'value': False
                }
                mqtt.publish(
                    config.MQTT_TOPIC + '/out', ujson.dumps(payload), qos=2
                )

            state = False

