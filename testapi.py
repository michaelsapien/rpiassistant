import speech_recognition as sr
import pyttsx3
import openai

#Set your openai api key and customizing the chatgpt role
openai.api_key = "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"
messages = [{"role": "system", "content": "Your name is pybot and give answers in 2 lines"}]



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