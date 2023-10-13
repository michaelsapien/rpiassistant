import paho.mqtt.client as mqtt
import speech_recognition as sr
import openai


openai.api_key = "xxx"
messages = [{"role": "system", "content": "Your name is pybot and give answers in 2 lines"}]

# MQTT Settings
MQTT_BROKER = "192.168.1.14"
MQTT_PORT = 1883
MQTT_TOPIC = "speechToTextTopic"
def get_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

def send_mqtt_message(message):
    client = mqtt.Client("WindowsClient")
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.publish(MQTT_TOPIC, message)
    client.disconnect()

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Please wait. Calibrating microphone...")
    # Calibrate the microphone to silence to avoid static noise
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print("Microphone calibrated")
    
    while True:
        print("Say something:")
        with microphone as source:
            try:
                audio = recognizer.listen(source, timeout=10)
                print("Recognizing...")
                # Use Google Web Speech API
                text = recognizer.recognize_google(audio)
                if "pybot" in text.lower():           
                    response_from_openai = get_response(text)
                    print("Q: " + text)
                    print("A: " + response_from_openai)
                    send_mqtt_message(response_from_openai)
            except sr.WaitTimeoutError:
                print("Speech not detected. Listening again...")
            except sr.UnknownValueError:
                print("Google Web Speech API could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Web Speech API service; {0}".format(e))

if __name__ == "__main__":
    main()
