config = dict(

    # Wifi Config
    WIFI_SSID=None,
    WIFI_PASSWORD=None,

    # MQTT Config
    MQTT_SERVER='localhost',
    MQTT_PORT=8883,
    MQTT_USER=None,
    MQTT_PASSWORD=None,
    MQTT_SSL=False,
    MQTT_CERTFILE=None,
    MQTT_CLIENT_ID=None,
    MQTT_TOPIC='home/temperature',

    # onewire
    ONEWIRE_PIN=0,

    # deepsleep
    ENABLE_DEEPSLEEP=False,
    SLEEP_TIME_S=60,
)
