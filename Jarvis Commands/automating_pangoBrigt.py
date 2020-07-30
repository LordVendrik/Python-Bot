import pyautogui,time,pyttsx3,speech_recognition as sr


def SetBrightness():
    p = None
    pyautogui.moveTo((1670,1054),duration = 0.25)
    pyautogui.click()

    #checking for pango icon on screen
    while p is None:
        p = pyautogui.locateOnScreen('C:\Python37\p.PNG',grayscale = False,confidence = 0.8)
    pyautogui.moveTo((p[0]+ (p[2]/2) , p[1]+ ((p[3]/2))),duration = 0.25)
    pyautogui.click()

    #checking for Choose Fade Out Color box on screen
    p = None
    while p is None:
        p = pyautogui.locateOnScreen('C:\Python37\Op.png',grayscale = False,confidence = 0.8)

    pyautogui.moveTo((p[0]+ (p[2]/2) , p[1]+ ((p[3]/2))),duration = 0.25)
    time.sleep(1)
    pyautogui.moveTo((p[0]+ 363 , p[1]+ ((p[3]/2))),duration = 0.25)
    pyautogui.moveTo(p[0]+ 363 , p[1] - 160,duration=0.25)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo((1670,1054),duration = 0.25)
    pyautogui.click()

    #checking for pango icon on screen 
    p = None
    while p is None:
        p = pyautogui.locateOnScreen('C:\Python37\p.PNG',grayscale = False,confidence = 0.8)

    pyautogui.moveTo((p[0]+ (p[2]/2) , p[1]+ ((p[3]/2))),duration = 0.25)
    pyautogui.click()

    #checking for Choose Fade Out Color on screen
    p = None
    while p is None:
        p = pyautogui.locateOnScreen('C:\Python37\Op.png',grayscale = False,confidence = 0.8)

    pyautogui.moveTo((p[0]+ (p[2]/2) , p[1]+ ((p[3]/2))),duration = 0.25)
    engine = pyttsx3.init()
    engine.say("Sir!!! Tell me what will be level of Brightness")
    engine.runAndWait()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        level = r.recognize_google(audio)
        print(level)
    except Exception as e:
        return "can't Listen"
    
    if level == "50":
        pyautogui.moveTo(p[0]+ (p[2]/2) , p[1] - 90,duration = 0.25)
    elif level == "60":
        pyautogui.moveTo(p[0]+ (p[2]/2) , p[1] - 112.5,duration = 0.25)
    elif level == "70":
        pyautogui.moveTo(p[0]+ (p[2]/2) , p[1] - 135,duration = 0.25)
    elif level == "80":
        pyautogui.moveTo(p[0]+ (p[2]/2) , p[1] - 157.5,duration = 0.25)
    elif level == "90":
        pyautogui.moveTo(p[0]+ (p[2]/2) , p[1] - 180,duration = 0.25)
    elif level == "100":
        pyautogui.moveTo(p[0]+ (p[2]/2) , p[1] - 202.5,duration = 0.25)

    pyautogui.click()


