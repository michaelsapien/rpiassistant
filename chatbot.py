import speech_recognition as sr
import openai
import pyttsx3
import sys

bot_name='panvi'
openai.api_key = "xxx"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')


messages = [{"role": "system", "content": "Your name is "+bot_name+" you were developed by stemx in June 2016. STEMx group were one of the first to introduce cutting edge technology in k-12 education and trainings since 2016.Two years back we introduced hands-on LEGO Robotics, Coding, and early concepts of STEM. Today our online STEM program has no limit to region, as we have students from India, Dubai, USA, Singapore, England, Nepal, SA, Canada, and Japan. 1,00,000+ students across India experienced STEM Education through STEMx 100+ Schools across India 10+ Channel partners across India 4 STEMx Studios across south India Online STEM Program in 7+ countries Students won national & international awards in Robotics  Competition Strong STEMx alumni community For more than 7+ Years  Founders of STEMx have been working with parents, teachers, schools, and governments to deliver playful learning experiences that bring  STEM subjects like Robotics, Coding, 3D Printing, Electronics & Drones to life  for the students and make learning fun and impactful and you should support Institute by giving Live campus tour for new prospects to parents, Can be an assistant teacher in classroom,Take students attendance and institute's receptionist"}]#give answers in two sentences

def get_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

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
                if bot_name in text.lower():           
                    if('exit' in text.lower()):
                        sys.exit()
                    response_from_openai =  (text)
                    print("Q: " + text)
                    print("A: " + response_from_openai)
                    engine.setProperty('rate', 120)
                    engine.setProperty('volume', volume)
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
