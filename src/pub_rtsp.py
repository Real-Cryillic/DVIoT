import random
from paho.mqtt import client as mqtt_client

broker = ""
port = 1883
topic = ""
client_id = f"{random.randint(0,100)}"


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        payload = msg.payload.decode()
        topic = msg.topic
        return payload, topic

    client.subscribe(topic)
    client.on_message = on_message


def monitor_id():
    broker = "127.0.0.1"
    port = 1883
    topic = "device/init"
    client_id = f"{random.randint(0,100)}"

    client = connect_mqtt()
    payload, topic = subscribe(client)
    # payload = device ID
    # topic = /device/init

    return payload, topic

def sub_id(device_id):
    broker = '127.0.0.1' or 'localhost'
    port = 1883
    topic = f"device/{device_id}/cmd"
    client_id = f"{random.randint(0,100)}"

    client = connect_mqtt()
    payload, topic = subscribe(client)
    # payload = {cmd:"",url:""}
    # topic = /device/<id>/cmd, assume topic matches

    try:
        payload = payload.split(',').split(':')
        payload_match = ["cmd","","url",""]
        for char in payload:
            pass
    except:
        pass


def main():
    device_id, init_topic = monitor_id()
    sub_id(device_id)


if __name__ == "__main__":
    main()
