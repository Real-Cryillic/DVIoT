import random
from paho.mqtt import client as mqtt_client

broker = "127.0.0.1"
port = 1883
client_id = f"{random.randint(0,100)}"
device_id = ""

def get_id(filename):
    with open(filename) as file: 
        for line in file:
            if len(line) > 19:
                print(line)
                return line
    
id = get_id("id.txt")
device_id = id

print("Gathered: ", device_id)

topic = f"device/{device_id}/cmd"

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
        print("Topic:", topic)
        print("Payload:", payload)
        print("Parsing payload...")
        payload = payload.split(",")
        CMD = 0
        URL = 1
        command_payload = payload[CMD]
        url_payload = payload[URL]
        print(command_payload)
        print(url_payload)
        target_cmd = "10"
            # for element in payload:
                # if element[CMD] == target_cmd:
                    # print("RTSP URL:", element[URL])

    client.subscribe(topic)
    client.on_message = on_message


'''
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
'''


def main():
    client = connect_mqtt()
    payload = subscribe(client)
    # payload = {cmd:"",url:""}
    # topic = /device/<id>/cmd, assume topic matches
    client.loop_forever()


if __name__ == "__main__":
    main()
