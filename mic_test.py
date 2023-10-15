import speech_recognition as sr

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
                print(text)
            except sr.WaitTimeoutError:
                print("Speech not detected. Listening again...")
            except sr.UnknownValueError:
                print("Google Web Speech API could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Web Speech API service; {0}".format(e))

if __name__ == "__main__":
    main()
