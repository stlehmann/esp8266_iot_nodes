import utime
import ujson
import core
import machine
from config import config


def run():
    wifi = None
    mqtt = None
    adc = machine.ADC(0)  # analog digital converter

    while True:
        try:
            # connect wifi
            if wifi is None:
                wifi = core.WifiWrapper(config)
            if not wifi.isconnected:
                wifi.connect()

            # connect mqtt
            if mqtt is None:
                mqtt = core.MQTTClientWrapper(config)
            mqtt.connect()

            # get values from sensor
            val = 100 * adc.read() / 1024

            # publish value
            payload = {'name': 'moisture', 'value': val, 'unit': 'pct'}
            mqtt.publish(config.MQTT_TOPIC, ujson.dumps(payload))

            mqtt.disconnect()
            core.sleep(config)

        except Exception as e:
            print(e)
