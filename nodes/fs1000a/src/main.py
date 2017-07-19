import utime
import webrepl
import ujson
import credentials
import core
from rfsocket import RFSocket, Esp8266Timings
import machine
from machine import Pin, freq


MQTT_CLIENT_ID = 'node2'
REFRESH_TIME_MS = 100
PINGTIME_S = 60
SECONDS_TO_RESET = 60


freq(160000000)
rf_pin = Pin(0, Pin.OUT)
mqtt = None


def handle(topic, msg):
    global mqtt
    payload = ujson.loads(msg)
    rf = RFSocket(rf_pin, RFSocket.ANSLUT, remote_id=payload['remote_id'],
                  timings=Esp8266Timings)
    if payload['state'] == 'on':
        rf.on(payload['switch'])
    else:
        rf.off(payload['switch'])

    if mqtt is not None:
        mqtt.publish('home/power/out', msg)


def run():

    global mqtt

    try:
        wifi = core.WifiWrapper(credentials.WIFI_SSID, credentials.WIFI_PASSWORD)
        wifi.connect()
    except WifiConnectionError:
        machine.reset()


    try:
        webrepl.start()
    except Exception as e:
        print(e)

    try:
        mqtt = core.MQTTClientWrapper(
            client_id=MQTT_CLIENT_ID,
            server=credentials.MQTT_SERVER,
            port=credentials.MQTT_PORT,
            user=credentials.MQTT_USER,
            password=credentials.MQTT_PASSWORD,
            ssl=credentials.MQTT_SSL,
            keepalive=PINGTIME_S * 2
        )
        mqtt.connect()
        mqtt.subscribe('home/power/in', handle)
    except core.MQTTConnectionError:
        print('Could not connect to Mosquitto server. Performing reset in {} seconds.'.format(SECONDS_TO_RESET))
        utime.sleep(SECONDS_TO_RESET)
        machine.reset()

    ping_ticks_ms = utime.ticks_ms()
    while True:
        try:
            mqtt.check_msg()
            if abs(utime.ticks_ms() - ping_ticks_ms) >= 1000 * PINGTIME_S:
                print('Sending Ping...', end='')
                mqtt.ping()
                print('done')
                ping_ticks_ms = utime.ticks_ms()
        except Exception as e:
            print(e)
            print('Performing reset in {} seconds.'.format(SECONDS_TO_RESET))
            utime.sleep(SECONDS_TO_RESET)
            machine.reset()

        utime.sleep_ms(REFRESH_TIME_MS)

