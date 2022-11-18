import paho.mqtt.client as mqtt
import time


# The callback for when the client receives a CONNACK response from the server.
# Should not use time.sleep() in this call back
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    if rc!=0 :
        client.reconnect()
        return

    # Subscribing in on_connect() means that if we lose the connection and

    # reconnect then subscriptions will be renewed.



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("quy", password="123456")

broker_addr = "localhost"
broker_port = 1883
keepAlive = 60
client.connect(broker_addr, broker_port, keepAlive)
client.publish("/phungvanquy/data/", None, qos = 0, retain=True)    # Retain True -> Whenever new user subscribes to topic, he will recieve the last previous payload. To Remove retained messg we just need to use payload=None and retain=True
client.loop_forever()