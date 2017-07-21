class WifiConfig:

    WIFI_SSID = ''  # SSID of the Wifi to log in
    WIFI_PASSWORD = ''  # Password of the Wifi connection


class MQTTConfig:

    MQTT_SERVER = ''  # ip or domain of the mqtt broker
    MQTT_PORT = 1883  # port for mqtt connection (e.g. 1883, 8883) 
    MQTT_USER = ''  # username if authentication is required
    MQTT_PASSWORD = ''  # password if authentication is required
    MQTT_KEEPALIVE = 0  # keepalive value in seconds for MQTT connect, 0 if disabled

    # ssl
    MQTT_SSL = False  # true if SSL enable, change the port to 8883 then
    MQTT_CERTFILE = None  # filename of the certfile for SSL connection
    MQTT_SSL_PARAMS = {}  # additional SSL parameters


class MQTTConfigSSL(MQTTConfig):

    MQTT_SSL = True
    MQTT_PORT = 8883
