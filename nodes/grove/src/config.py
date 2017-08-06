from credentials import WifiConfig, MQTTConfig


class Config(WifiConfig, MQTTConfig):

    MQTT_CLIENT_ID = 'grove_node'
    MQTT_TOPIC = 'home/moisture'

    # deepsleep
    ENABLE_DEEPSLEEP = False      # Enter deepsleep while waiting
    SLEEP_TIME_S = 60             # time between two measurements


config = Config()
