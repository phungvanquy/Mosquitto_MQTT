import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print(client)


    for i in range(1,5):
        mess = client.publish("/phungvanquy/data/", 10)
        client.loop_start()
    # Subscribing in on_connect() means that if we lose the connection and

    # reconnect then subscriptions will be renewed.



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
print(client)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("quy", password="123456")

client.connect("192.168.0.107", 1883, 60)



# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()
while True:
    time.sleep(1)