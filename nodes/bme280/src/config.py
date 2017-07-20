class Config:

    # Wifi Config
    WIFI_SSID = ''                # SSID of the Wifi to log in
    WIFI_PASSWORD = ''            # Password of the Wifi
    WIFI_MAX_RETRIES = 3          # max. number of retries before resetting device
    WIFI_TIMEOUT_MS = 10000       # timeout value for Wifi connection

    # MQTT Config
    MQTT_SERVER = ''              # Address of the MQTT Broker.
    MQTT_PORT = 8883              # Port of the MQTT Broker (default=1883, ssl=8883)
    MQTT_USER = ''                # Username for the MQTT Broker if authentification is required
    MQTT_PASSWORD = ''            # Password for the MQTT Broker if authentification is required
    MQTT_CLIENT_ID = ''           # The MQTT client id of the node
    MQTT_TOPIC = ''               # The  MQTT topic of the node

    MQTT_KEEPALIVE = 120          # Keepalive value for MQTT Broker
    MQTT_SSL = True               # Use SSL connection to the broker. Set the port to 8883 if using SSL.
    MQTT_CERTFILE = None          # (SSL only) The certification file for the SSL connection
    MQTT_SSL_PARAMS = {}          # additional SSL params
    MQTT_MAX_RETRIES = 3          # Maximum retries for establishing MQTT connection

    # deepsleep
    ENABLE_DEEPSLEEP = False      # Enter deepsleep while waiting
    SLEEP_TIME_S = 60             # time between two measurements

    # I2C bus settings
    I2C_SCL_PIN = 0
    I2C_SDA_PIN = 4
    I2C_BME280_ADDRESS = 10


config = Config()
