import pyttsx3
import sys
if len(sys.argv) < 2:
    print('give the words to speak. like.. python3 testspeaker.py "words to tell"')
    sys.exit()

print(sys.argv[0])
engine = pyttsx3.init()

voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

engine.setProperty('rate', 120)
engine.setProperty('volume', volume)

engine.say(sys.argv[1])
engine.runAndWait()
