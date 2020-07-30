import pyttsx3
import automating_pangoBrigt as ap
import time
import speech_recognition as sr
import Opening_Programs as op

engine = pyttsx3.init()
engine.say("Welcome !!!!!! Sir Tell me What can i do")
engine.runAndWait()

r = sr.Recognizer()


with sr.Microphone() as source:
    com = ""
    r.adjust_for_ambient_noise(source)
    while com != "no help":

        print("Say something!")
        audio = r.listen(source)
        try:
            com = r.recognize_google(audio)
        except Exception as e:
             print("can't Listen")
        
        if com == "Set brightness":
            engine.say("Setting Brightness")
            engine.runAndWait()
            time.sleep(1)
            ap.SetBrightness()
            engine.say("Done !!! Anything else, Sir")
            engine.runAndWait()

        elif "open" in com:
            engine.say("Opening !!!!!!! Sir wait")
            engine.runAndWait()
            time.sleep(1)
            programName = com[6:len(com)]
            print(com)
            op.OpenProgram(programName,False)
            engine.say("Anything else, Sir")
            engine.runAndWait()
            

        elif com == "no help":
            engine.say("Ok!!!!! Leaving Sir")
            engine.runAndWait()

        else:
            engine.say("Sir !!! I think this command is not in my library or you mistyped it")
            engine.runAndWait()
            
        





