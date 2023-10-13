import paho.mqtt.client as mqtt
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("speechToTextTopic")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")
    engine.setProperty('rate', 120)
    engine.setProperty('volume', volume)
    engine.setProperty('voice', 'greek')
    engine.say({msg.payload.decode()})
    engine.runAndWait()

client = mqtt.Client("RaspberryClient")
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
