from credentials import WifiConfig, MQTTConfig


class Config(WifiConfig, MQTTConfig):

    MQTT_CLIENT_ID = 'hcscr501node'
    MQTT_TOPIC = 'home/hcsr501'

    PIN_SENSOR = 4  # Pin for reading the sensor

config = Config()
