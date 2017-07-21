from credentials import WifiConfig, MQTTConfig


class Config:

    MQTT_CLIENT_ID = 'ds18x20node'
    MQTT_TOPIC = 'home/ds18x20'

    # onewire
    ONEWIRE_PIN = 0               # Pin number for the onewire port

    # deepsleep
    ENABLE_DEEPSLEEP = True       # Enter deepsleep while waiting
    SLEEP_TIME_S = 60             # time between two measurements


config = Config()
