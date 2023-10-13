import pyttsx3

import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

engine.setProperty('rate', 120)
engine.setProperty('volume', volume)

engine.say("testing speaker")
engine.runAndWait()
