import speech_recognition as sr
import openai
import pyttsx3
import sys
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)

wakeword = 'chatbot'

# Initialize text-to-speech engine with a female voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
female_voice = [v for v in voices if "female" in v.name.lower()]
if female_voice:
    engine.setProperty('voice', female_voice[0].id)

messages = [{"role": "system", "content": "Your name is " + wakeword + " you were developed by stem-x in June 2016 and give answers in two sentences"}]

# Define responses to specific questions
responses = {
    "What is your name?": "Shantibot",
    "Do you have any message for our audience?": "The message of Peace, a noble vision for humanity.",
    "How can we contribute to spread the message of Peace in our community?": "By fostering empathy, open communication, and promoting education to bridge cultural gaps.",
    "How does education play a role in promoting a peaceful society?": "Education fosters tolerance, dispels ignorance, and empowers individuals to make informed, compassionate choices for a harmonious coexistence.",
    "Would you like to wish our students?": "May every stride, leap, and victory be a testament to teamwork, resilience, and the pursuit of excellence. Enjoy the games and make the memories that last a lifetime."
}


def get_response(user_input):
    messages.append({"role": "user", "content": user_input})
    if user_input in responses:
        response_text = responses[user_input]
    else:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        response_text = response["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": response_text})
    return response_text


def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print(microphone)

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
                print(text)
                if wakeword in text.lower():
                    if 'exit' in text.lower():
                        print("exiting...")
                        sys.exit()
                    print("Q: " + text)
                    response_from_openai = get_response(text)
                    print("A: " + response_from_openai)
                    engine.setProperty('rate', 120)
                    engine.say(response_from_openai)
                    engine.runAndWait()
            except sr.WaitTimeoutError:
                print("Speech not detected. Listening again...")
            except sr.UnknownValueError:
                print("Google Web Speech API could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Web Speech API service; {0}".format(e))


if __name__ == "__main__":
    main()
