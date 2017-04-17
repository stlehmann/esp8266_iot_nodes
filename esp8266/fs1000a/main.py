import webrepl
import ujson
import credentials
import core
from rfsocket import RFSocket, Esp8266Timings
from machine import Pin, freq


MQTT_CLIENT_ID = 'node2'


freq(160000000)
wifi = core.WifiWrapper(credentials.WIFI_SSID, credentials.WIFI_PASSWORD)
mqtt = core.MQTTClientWrapper(
    client_id=MQTT_CLIENT_ID,
    server=credentials.MQTT_SERVER,
    port=credentials.MQTT_PORT,
    user=credentials.MQTT_USER,
    password=credentials.MQTT_PASSWORD,
    ssl=credentials.MQTT_SSL,
    keepalive=1,
)
rf_pin = Pin(0, Pin.OUT)


def handle(topic, msg):
    payload = ujson.loads(msg)
    rf = RFSocket(rf_pin, RFSocket.ANSLUT, remote_id=payload['remote_id'],
                  timings=Esp8266Timings)
    if payload['state'] == 'on':
        rf.on(payload['switch'])
    else:
        rf.off(payload['switch'])


def run():
    wifi.connect()
    webrepl.start()
    mqtt.connect()
    mqtt.subscribe('home/power', handle)

    while True:
        mqtt.wait_msg()
