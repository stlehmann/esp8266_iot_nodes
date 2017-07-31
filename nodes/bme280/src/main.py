import utime
import ujson
import core
import machine
import bme280
from config import config


i2c = None
bme = None
mqtt_client = None


def run():
    wifi = None
    mqtt = None
    i2c = machine.I2C(scl=machine.Pin(config.I2C_SCL_PIN),
                      sda=machine.Pin(config.I2C_SDA_PIN))
    adr = i2c.scan()[0]
    bme = bme280.BME280(i2c=i2c, address=adr)

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
            vals = bme.values
            temp = vals[0][:-1]
            pressure = vals[1][:-3]
            humidity = vals[2][:-1]

            # publish temperature
            utime.sleep_ms(500)
            payload = {'name': 'temperature', 'value': temp, 'unit': 'C'}
            mqtt.publish(config.MQTT_TOPIC + '/temp', ujson.dumps(payload))

            # publish pressure
            utime.sleep_ms(500)
            payload = {'name': 'pressure', 'value': pressure, 'unit': 'bar'}
            mqtt.publish(config.MQTT_TOPIC + '/pressure', ujson.dumps(payload))

            # publish humidity
            utime.sleep_ms(500)
            payload = {'name': 'humidity', 'value': humidity, 'unit': 'pct'}
            mqtt.publish(config.MQTT_TOPIC + '/humidity', ujson.dumps(payload))

            mqtt.disconnect()
            core.sleep(config)

        except Exception as e:
            print(e)
