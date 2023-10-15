from gtts import gTTS
import os
import speech_recognition as sr
import openai
import sys

wakeword='chatbot'
openai.api_key = "xxx"

messages = [{"role": "system", "content": "Your name is "+wakeword+" you were developed by stem-x in June 2016 and give answers in two sentences"}]

def get_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

def speak_gtts(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

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
                text = recognizer.recognize_google(audio)
                
                if wakeword in text.lower():
                    if('exit' in text.lower()):
                        print("exiting...")
                        sys.exit()                    
                    print("Q: " + text)
                    response_from_openai = get_response(text)
                    print("A: " + response_from_openai)
                    speak_gtts(response_from_openai)  # Using gTTS instead of pyttsx3

            except sr.WaitTimeoutError:
                print("Speech not detected. Listening again...")
            except sr.UnknownValueError:
                print("Google Web Speech API could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Web Speech API service; {0}".format(e))

if __name__ == "__main__":
    main()
