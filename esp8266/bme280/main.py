import utime
import machine
import bme280
from credentials import *
from umqtt.simple import MQTTClient

MQTT_TOPIC = 'test'
WIFI_TIMEOUT_MS = 10000

I2C_SCL_PIN = 0
I2C_SDA_PIN = 4
I2C_BME280_ADDRESS = 119

SLEEP_TIME_MS = 10000


i2c = None
bme = None
mqtt_client = MQTTClient(MQTT_CLIENT_ID, MQTT_SERVER, MQTT_PORT, MQTT_USER,
                         MQTT_PASSWORD, ssl=MQTT_SSL)


def wifi_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        t0 = utime.ticks_ms()
        while not sta_if.isconnected():
            if abs(utime.ticks_ms() - t0) > WIFI_TIMEOUT_MS:
                print('Wifi connection timeout')
                return
    print('network config:', sta_if.ifconfig())


def mqtt_connect():
    print('connecting to mosquitto server...', end='')
    res = mqtt_client.connect()
    if res == 0:
        print('done')
    else:
        print('errorcode', res)


def mqtt_disconnect():
    mqtt_client.disconnect()


def init_i2c():
    global i2c, bme

    i2c = machine.I2C(scl=machine.Pin(I2C_SCL_PIN),
                      sda=machine.Pin(I2C_SDA_PIN))

    bme = bme280.BME280(i2c=i2c, address=I2C_BME280_ADDRESS)


def deepsleep():
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, SLEEP_TIME_MS)
    print('entering deepsleep')
    machine.deepsleep()


def run():
    wifi_connect()
    mqtt_connect()
    init_i2c()

    vals = '[' + ','.join(bme.values) + ']'
    print('publishing topic {}: {}...'.format(MQTT_TOPIC, vals), end='')
    mqtt_client.publish(MQTT_TOPIC, vals)
    print('done')
    print('disconnecting from mosquitto server...', end='')
    mqtt_disconnect()
    print('done')

    deepsleep()
