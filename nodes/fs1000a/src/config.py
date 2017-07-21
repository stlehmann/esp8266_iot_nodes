from credentials import WifiConfig, MQTTConfig


class Config(WifiConfig, MQTTConfig):

    MQTT_CLIENT_ID = 'fs1000anode'
    MQTT_TOPIC = 'home/fs1000a'

    # custom config
    REFRESH_TIME_MS = 100         # refresh interval for incoming MQTT messages
    ERROR_RESET_TIME_S = 60       # wait time for reset after an error was detected


config = Config()
