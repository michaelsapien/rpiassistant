import speech_recognition as sr
import pyttsx3
import openai

#Initializing pyttsx3
listening = True
engine = pyttsx3.init()

#Set your openai api key and customizing the chatgpt role
openai.api_key = "xxx"
messages = [{"role": "system", "content": "Your name is pybot and give answers in 2 lines"}]

#Customizing The output voice
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')


def get_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

while True:
    question=input("enter question: ")
    response_from_openai = get_response(question)
    print(response_from_openai)