import paho.mqtt.client as mqtt
import time

# Configuration:
BROKER_ADDRESS = "your_broker_ip"  # IP address of your MQTT broker.
TOPIC = "test/topic"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect

client.connect(BROKER_ADDRESS, 1883, 60)  # Connect to the broker.

client.loop_start()

try:
    while True:
        message = input("Enter your message: ")
        client.publish(TOPIC, message)  # Publish a message.
        time.sleep(1)  # Sleep for a short period to ensure the message is sent.

except KeyboardInterrupt:
    print("Disconnected")

finally:
    client.loop_stop()
    client.disconnect()