import utime
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
                wifi = core.WifiWrapper(config['WIFI_SSID'],
                                        config['WIFI_PASSWORD'])
            wifi.connect()

            if mqtt is None:
                mqtt = core.MQTTClientWrapper(
                    client_id=config.get('MQTT_CLIENT_ID', 'umqtt_client'),
                    server=config.get('MQTT_SERVER', 'localhost'),
                    port=config.get('MQTT_PORT', 0),
                    user=config.get('MQTT_USER'),
                    password=config.get('MQTT_PASSWORD'),
                    ssl=config.get('MQTT_SSL', False),
                )
            mqtt.connect()

            print('searching for Onewire Sensors...', end='')
            ow = onewire.OneWire(machine.Pin(config.get('ONEWIRE_PIN', 0)))
            temp_sens = ds18x20.DS18X20(ow)
            rom = temp_sens.scan()
            if len(rom) > 0:
                print('done. found {} sensors. reading from first.'
                      .format(len(rom)))
                temp_sens.convert_temp()
                temp = temp_sens.read_temp(rom[0])
                print('temperature: {:.2f}°C'.format(temp))
                mqtt.publish(config['MQTT_TOPIC'], '{:.2f}'.format(temp))
            else:
                print('failed. none found.')

            sleeptime = config.get('SLEEP_TIME_S', 60)
            if config.get('ENABLE_DEEPSLEEP', False):
                mqtt.disconnect()
                core.deepsleep(sleeptime)
            else:
                utime.sleep(sleeptime)
        except Exception as e:
            print(e)
