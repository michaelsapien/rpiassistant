import paho.mqtt.client as mqtt
import time

# Configuration
broker_address = "localhost"  # Use the IP address of your Windows machine
topic = "chat"

# Callback for connection
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic)

# Callback for message
def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}")

# Setup client
client = mqtt.Client("WindowsPublisher")
client.on_connect = on_connect
client.on_message = on_message

# Connect and publish message
client.connect(broker_address)
client.loop_start()

while True:
    message = input("Enter your message: ")
    client.publish(topic, message)
    time.sleep(1)  # Ensure message is sent before ending program

client.loop_stop()
client.disconnect()
