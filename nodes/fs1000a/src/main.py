import utime
import webrepl
import ujson
import core
from rfsocket import RFSocket, Esp8266Timings
from config import config
import machine
from machine import Pin, freq


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
        mqtt.publish(config.MQTT_TOPIC + '/out', msg)


def run():

    global mqtt

    # Bring up Wifi
    try:
        wifi = core.WifiWrapper(config)
        wifi.connect()
    except core.WifiConnectionError:
        machine.reset()

    # Start WebREPL
    try:
        webrepl.start()
    except Exception as e:
        print(e)

    # Connect to MQTT Broker
    try:
        mqtt = core.MQTTClientWrapper(config)
        mqtt.connect()
        mqtt.subscribe(config.MQTT_TOPIC + '/in', handle)
    except core.MQTTConnectionError:
        print('Could not connect to Mosquitto server. Performing reset '
              'in {} seconds.'.format(config.ERROR_RESET_TIME_S))
        utime.sleep(config.ERROR_RESET_TIME_S)
        machine.reset()

    # Workloop
    ping_ticks_ms = utime.ticks_ms()
    while True:
        try:
            mqtt.check_msg()
            if (abs(utime.ticks_ms() - ping_ticks_ms) >=
                    (1000 * config.MQTT_KEEPALIVE / 2.0)):
                print('Sending Ping...', end='')
                mqtt.ping()
                print('done')
                ping_ticks_ms = utime.ticks_ms()
        except Exception as e:
            print(e)
            print('Performing reset in {} seconds.'
                  .format(config.ERROR_RESET_TIME_S))
            utime.sleep(config.ERROR_RESET_TIME_S)
            machine.reset()
        utime.sleep_ms(config.REFRESH_TIME_MS)
