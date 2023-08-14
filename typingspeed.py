#Typinf speed checker

from time import *
import random as r

def mistake(paratext, usertext):
    error = 0
    for i in range(0,len(paratext)):
        try:
            if paratext[i] != usertext[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def typingspeed(time_s, time_e, userinput):
    timedelay = round((time_e - time_s), 3)
    speed = len(userinput)/timedelay
    return round(speed)



textlist = ["Hello bro","Business meetings, and professional recordings can contain sensitive data, so security is something a transcription company should not overlook when providing services. Companies should therefore follow the various laws and industry best practice, especially so when serving law firms, government agencies or courts.", "Medical Transcription specifically is governed by HIPAA, which elaborates data security practices and compliance measures to be strictly followed, failure of which leads to legal action and penalties.", "Transcription security includes maintaining confidentiality of the data through information security practices including limiting access with passwords and ensuring a secure environment for data and appropriate methods of disposal of all materials and deletion of files.", "Personnel may be required to sign non-disclosure agreements on a regular basis as well as take various oaths regarding confidentiality and accuracy."]

text = r.choice(textlist)
print("!!!! Typing Speed Checker !!!!")
print()
print("Text to type: \n", text)
print()
print()
a = int(input("Type 1 and press enter to start timer or type 0 to end test : "))
if a == 1:
    time_1 = time()
    textinput = input("Enter text : ")
    time_2 = time()

    print("Speed: ", typingspeed(time_1, time_2, textinput), "char/sec")
    print("Mistake: ", mistake(text, textinput))
elif a == 0:
    print("Your test is ended")


