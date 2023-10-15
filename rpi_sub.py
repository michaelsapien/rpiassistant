import paho.mqtt.client as mqtt

# Configuration
broker_address = "YOUR_WINDOWS_IP_ADDRESS"  # Replace with the IP address of your Windows machine
topic = "chat"

# Callback for connection
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic)

# Callback for message
def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode('utf-8')}")

# Setup client
client = mqtt.Client("RaspberrySubscriber")
client.on_connect = on_connect
client.on_message = on_message

# Connect and start listening
client.connect(broker_address)
client.loop_forever()
