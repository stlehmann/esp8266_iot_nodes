from credentials import WifiConfig, MQTTConfig


class Config(WifiConfig, MQTTConfig):

    MQTT_CLIENT_ID = 'bme280node'
    MQTT_TOPIC = 'home/bme280'

    # deepsleep
    ENABLE_DEEPSLEEP = False      # Enter deepsleep while waiting
    SLEEP_TIME_S = 60             # time between two measurements

    # I2C bus settings
    I2C_SCL_PIN = 0
    I2C_SDA_PIN = 4


config = Config()
