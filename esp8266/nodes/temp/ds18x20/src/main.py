import utime
import credentials
import core
import onewire
import machine
import ds18x20


MQTT_CLIENT_ID = 'node3'
MQTT_TOPIC = 'home/living/temp'
ONEWIRE_PIN = 0  # Pin D3 on the Node MCU
ENABLE_DEEPSLEEP = True
SLEEP_TIME_S = 60


def run():
    wifi = None
    mqtt = None

    while True:
        try:
            if wifi is None:
                wifi = core.WifiWrapper(credentials.WIFI_SSID, credentials.WIFI_PASSWORD)
            wifi.connect()

            if mqtt is None:
                mqtt = core.MQTTClientWrapper(
                    client_id=MQTT_CLIENT_ID,
                    server=credentials.MQTT_SERVER,
                    port=credentials.MQTT_PORT,
                    user=credentials.MQTT_USER,
                    password=credentials.MQTT_PASSWORD,
                    ssl=credentials.MQTT_SSL,
                )
            mqtt.connect()

            print('searching for Onewire Sensors...', end='')
            ow = onewire.OneWire(machine.Pin(ONEWIRE_PIN))
            temp_sens = ds18x20.DS18X20(ow)
            rom = temp_sens.scan()
            if len(rom) > 0:
                print('done. found {} sensors. reading from first.'.format(len(rom)))
                temp_sens.convert_temp()
                temp = temp_sens.read_temp(rom[0])
                print('temperature: {:.2f}°C'.format(temp))
                mqtt.publish(MQTT_TOPIC, '{:.2f}'.format(temp))
            else:
                print('failed. none found.')

            if ENABLE_DEEPSLEEP:
                mqtt.disconnect()
                core.deepsleep(SLEEP_TIME_S)
            else:
                utime.sleep(SLEEP_TIME_S)
        except Exception as e:
            print(e)
