import utime
import machine
import bme280
from credentials import *
from umqtt.simple import MQTTClient

MQTT_TOPIC = 'home/balcony'
WIFI_TIMEOUT_MS = 10000

I2C_SCL_PIN = 0
I2C_SDA_PIN = 4
I2C_BME280_ADDRESS = 119

SLEEP_TIME_MS = 10000
ENABLE_DEEPSLEEP = True 


i2c = None
bme = None
mqtt_client = None


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
    global mqtt_client
    mqtt_client = MQTTClient(MQTT_CLIENT_ID, MQTT_SERVER, MQTT_PORT, MQTT_USER,
                         MQTT_PASSWORD, ssl=MQTT_SSL)
    print('connecting to mosquitto server...', end='')
    res = mqtt_client.connect()
    if res == 0:
        print('done')
    else:
        print('errorcode', res)


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
    rtc.alarm(rtc.ALARM0, SLEEP_TIME_MS)
    print('entering deepsleep')
    machine.deepsleep()


def run():
    wifi_connect()
    mqtt_connect()
    init_i2c()

    while True:
        vals = bme.values

        temp = vals[0][:-1]
        pressure = vals[1][:-3]
        humidity = vals[2][:-1]

        mqtt_publish('home/balkony/temp', temp)
        mqtt_publish('home/balkony/pressure', pressure)
        mqtt_publish('home/balkony/humidity', humidity)

        if ENABLE_DEEPSLEEP:
            print('disconnecting from mosquitto server...', end='')
            mqtt_disconnect()
            print('done')
            deepsleep()
        else:
            utime.sleep(SLEEP_TIME_MS / 1000)
