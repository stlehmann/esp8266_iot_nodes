import network
import utime
import machine
import bme280
from credentials import WIFI_SSID, WIFI_PASSWORD, MQTT_CLIENT_ID, \
    MQTT_SERVER, MQTT_PORT, MQTT_USER, MQTT_PASSWORD, MQTT_SSL

from umqtt.simple import MQTTClient

MQTT_TOPIC = 'home/balcony'
MQTT_MAX_ATTEMPTS = 3

WIFI_TIMEOUT_MS = 10000
WIFI_MAX_ATTEMPTS = 3

I2C_SCL_PIN = 0
I2C_SDA_PIN = 4
I2C_BME280_ADDRESS = 119

SLEEP_TIME_S = 60
ENABLE_DEEPSLEEP = True


i2c = None
bme = None
mqtt_client = None


class WifiConnectionError(Exception):
    pass


class MQTTConnectionError(Exception):
    pass


def wifi_connect():
    attempt = 1
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        while attempt <= WIFI_MAX_ATTEMPTS:
            print('connecting to network "{}" (attempt {})...'
                  .format(WIFI_SSID, attempt),
                  end='')
            sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
            t0 = utime.ticks_ms()
            while not sta_if.isconnected():
                if abs(utime.ticks_ms() - t0) > WIFI_TIMEOUT_MS:
                    print('error')
                    print('wiwi connection timed out')
                    attempt += 1
                    break
            else:
                break
        else:
            raise WifiConnectionError()
    print('done')
    print('network config:', sta_if.ifconfig())


def mqtt_connect():
    global mqtt_client
    mqtt_client = MQTTClient(MQTT_CLIENT_ID, MQTT_SERVER, MQTT_PORT, MQTT_USER,
                             MQTT_PASSWORD, ssl=MQTT_SSL)
    attempt = 1
    while attempt <= MQTT_MAX_ATTEMPTS:
        print('connecting to mosquitto server "{}:{}" (attempt {})...'
              .format(MQTT_SERVER, MQTT_PORT, attempt), end='')

        try:
            res = mqtt_client.connect()
            if res == 0:
                print('done')
                break
            else:
                print('error {}'.format(res))
                attempt += 1

        except OSError:
            print('error')
            attempt += 1
    else:
        raise MQTTConnectionError()


def mqtt_disconnect():
    mqtt_client.disconnect()


def mqtt_publish(topic, msg):
    print('publishing topic {}: {}...'.format(topic, msg), end='')
    mqtt_client.publish(topic, msg)
    print('done')


def init_i2c():
    global i2c, bme

    i2c = machine.I2C(scl=machine.Pin(I2C_SCL_PIN),
                      sda=machine.Pin(I2C_SDA_PIN))

    bme = bme280.BME280(i2c=i2c, address=I2C_BME280_ADDRESS)


def deepsleep():
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, SLEEP_TIME_S * 1000)
    print('entering deepsleep ({} seconds)'.format(SLEEP_TIME_S))
    machine.deepsleep()


def run():
    init_i2c()
    wifi_connect()
    mqtt_connect()

    while True:
        vals = bme.values

        temp = vals[0][:-1]
        pressure = vals[1][:-3]
        humidity = vals[2][:-1]

        utime.sleep_ms(100)
        mqtt_publish('home/balkony/temp', temp)
        utime.sleep_ms(100)
        mqtt_publish('home/balkony/pressure', pressure)
        utime.sleep_ms(100)
        mqtt_publish('home/balkony/humidity', humidity)

        if ENABLE_DEEPSLEEP:
            print('disconnecting from mosquitto server...', end='')
            mqtt_disconnect()
            print('done')
            deepsleep()
        else:
            print('sleeping for {} seconds'.format(SLEEP_TIME_S))
            utime.sleep(SLEEP_TIME_S)
