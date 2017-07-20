import utime
import ujson
from config import config
import core
import onewire
import machine
import ds18x20


def run():
    wifi = None
    mqtt = None

    while True:
        try:
            if wifi is None:
                wifi = core.WifiWrapper(config)
            wifi.connect()

            if mqtt is None:
                mqtt = core.MQTTClientWrapper(config)
            mqtt.connect()

            ow_pin = config.ONEWIRE_PIN
            ow = onewire.OneWire(machine.Pin(ow_pin))
            print('searching for Onewire Sensors on pin {}...'.format(ow_pin), end='')
            temp_sens = ds18x20.DS18X20(ow)
            rom = temp_sens.scan()
            if len(rom) > 0:
                print('done. found {} sensors. reading from first.'
                      .format(len(rom)))
                temp_sens.convert_temp()
                temp = temp_sens.read_temp(rom[0])

                print('temperature: {:.2f}°C'.format(temp))

                # create payload
                payload = {
                    'value': '{:.2f}'.format(temp),
                    'unit': 'C'
                }
                mqtt.publish(config.MQTT_TOPIC, ujson.dumps(payload))
            else:
                print('failed. none found.')

            if config.ENABLE_DEEPSLEEP:
                mqtt.disconnect()

            core.sleep(config)

        except Exception as e:
            print(e)
