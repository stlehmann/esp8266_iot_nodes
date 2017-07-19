class Config:

    # Wifi Config
    WIFI_SSID=''
    WIFI_PASSWORD=''

    # MQTT Config
    MQTT_SERVER=''
    MQTT_PORT=8883
    MQTT_USER=''
    MQTT_PASSWORD=''
    MQTT_SSL=True
    MQTT_CERTFILE=None
    MQTT_CLIENT_ID=''
    MQTT_TOPIC=''
    MQTT_KEEPALIVE=120

    REFRESH_TIME_MS = 100
    ERROR_RESET_TIME_S = 60

config = Config()
