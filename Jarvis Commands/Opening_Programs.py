import regex as r
import os
import pyttsx3,subprocess
import speech_recognition as sr


def OpenProgram(filename,done):
    engine = pyttsx3.init()
    r = sr.Recognizer()

    #Open And Read FIle
    with open(r'C:\Users\ACER\Desktop\locations.txt') as L:
        d = L.read()

    #saving data in a list
    li = list(e.split(",") for e in d.split("\n"))

    #Saving speech into string variable
    da = filename

    Exes = []

    #matching for pattern
    for i in range(len(li)-2):
        if da.upper() in li[i][1].upper():
            Exes.append([li[i][0],li[i][1]])

    if len(Exes) > 1:
        engine.say("Sir!!!!!! multiple match found which one should i run in this list")
        engine.runAndWait()
        for i in range(len(Exes)):
            print(Exes[i][0])
        with sr.Microphone() as source:
            com = ""
            print("Reply !!!!!!!")
            audio = r.listen(source)
            try:
                com = r.recognize_google(audio)
                print(com)
            except Exception as e:
                print("can't Listen")

        if com == "first":
            number = 1
        elif com == "second":
            number = 2
        elif com == "third":
            number = 3
        elif com == "fourth":
            number = 4
        elif com == "fifth":
            number = 5
        elif com == "sixth":
            number = 6
        elif com == "seventh":
            number = 7    
        
        engine.say("Ok !!!!!!!!!!! Sir running")
        engine.runAndWait()
        subprocess.Popen(os.path.join(Exes[number-1][1],Exes[number-1][0]))
        

    elif Exes == 1:
        subprocess.Popen(os.path.join(Exes[0][1],Exes[0][0]))

    else :
        print("No Match FOund")
        x = da.split(" ")
        if len(x) == 2:
            newWord = x[0] + x[1]
        elif len(x) == 3:
            newWord = x[0]+x[1]+x[2]

        if done == False and len(x) != 1:
            OpenProgram(newWord,True)

        if done == True:
            engine.say("No Match Found !!!!!! Sir")
            engine.runAndWait()




