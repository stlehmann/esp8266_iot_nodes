import network
import utime
import machine
from umqtt.simple import MQTTClient


def deepsleep(seconds):
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, seconds * 1000)
    print('entering deepsleep ({} seconds)'.format(seconds))
    machine.deepsleep()


class WifiConnectionError(Exception):
    pass


class MQTTConnectionError(Exception):
    pass


class MQTTClientWrapper:

    def __init__(self, config):

        self.server = config.MQTT_SERVER
        self.port = config.MQTT_PORT
        self.mqtt_client = MQTTClient(
            client_id=config.MQTT_CLIENT_ID,
            server=self.server,
            port=self.port,
            user=config.MQTT_USER,
            password=config.MQTT_PASSWORD,
            keepalive=config.MQTT_KEEPALIVE,
            ssl=config.MQTT_SSL,
            ssl_params=config.MQTT_SSL_PARAMS,
        )
        self.mqtt_client.set_callback(self._process_incoming_msgs)
        self.callbacks = {}
        self.connected = False
        self.max_retries = config.MQTT_MAX_RETRIES 

    def connect(self):
        attempt = 1
        while attempt <= self.max_retries:
            print('connecting to mosquitto server "{}:{}" (attempt {})...'
                  .format(self.server, self.port,
                          attempt), end='')

            try:
                res = self.mqtt_client.connect()
                if res == 0:
                    print('done')
                    break
                else:
                    print('error {}'.format(res))
                    attempt += 1

            except OSError:
                print('error')
                attempt += 1
        else:
            self.connected = False
            raise MQTTConnectionError()

        self.connected = True

    def disconnect(self):
        self.mqtt_client.disconnect()

    def publish(self, topic, msg):
        print('publishing topic {}: {}...'.format(topic, msg), end='')
        self.mqtt_client.publish(topic, msg)
        print('done')

    def subscribe(self, topic, callback):
        self.callbacks[topic] = callback
        self.mqtt_client.subscribe(topic)

    def _process_incoming_msgs(self, topic, msg):
        topic = topic.decode()
        msg = msg.decode()
        callback = self.callbacks.get(topic)
        if callback is not None:
            callback(topic, msg)

    def wait_msg(self):
        return self.mqtt_client.wait_msg()

    def check_msg(self):
        return self.mqtt_client.check_msg()

    def ping(self):
        return self.mqtt_client.ping()


class WifiWrapper:

    def __init__(self, config):
        self.ssid = config.WIFI_SSID
        self.password = config.WIFI_PASSWORD
        self.max_retries = config.WIFI_MAX_RETRIES
        self.timeout_ms = config.WIFI_TIMEOUT_MS

    def connect(self):
        attempt = 1
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            sta_if.active(True)
            while attempt <= self.max_retries:
                print('connecting to network "{}" (attempt {})...'
                      .format(self.ssid, attempt), end='')
                sta_if.connect(self.ssid, self.password)
                t0 = utime.ticks_ms()
                while not sta_if.isconnected():
                    if abs(utime.ticks_ms() - t0) > self.timeout_ms:
                        print('error')
                        print('wifi connection timed out')
                        attempt += 1
                        break
                else:
                    break
            else:
                raise WifiConnectionError()
        print('done')
        print('network config:', sta_if.ifconfig())
