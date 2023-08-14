#firstly - pip install pyttsx3

import pyttsx3

print("!!!!!!!   Welcome to Robo Speaker   !!!!!!!")
engine = pyttsx3.init()

while True :
    enter = input("What would you like me to speak : ")
    if enter == "exit" :
        engine.say("Goodbye my dear Friend")
        engine.runAndWait()
        break
    engine.say(enter)
    engine.runAndWait()  