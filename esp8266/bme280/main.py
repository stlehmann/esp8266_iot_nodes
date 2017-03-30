import time
import machine
import bme280


I2C_SCL_PIN = 5
I2C_SDA_PIN = 4
BME280_ADDRESS = 119


i2c = None
bme = None


def init():
    global i2c, bme
    i2c = machine.I2C(scl=machine.Pin(I2C_SCL_PIN),
                      sda=machine.Pin(I2C_SDA_PIN))

    bme = bme280.BME280(i2c=i2c, address=BME280_ADDRESS)


def run():
    while True:
        print(bme.values)
        time.sleep(1)
