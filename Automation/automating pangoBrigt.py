import pyautogui,time

time.sleep(5)

pyautogui.moveTo((1670,1054),duration = 0.25)
pyautogui.click()
p = pyautogui.locateOnScreen('C:\Python37\p.PNG',grayscale = False,confidence = 0.8)
pyautogui.moveTo((p[0]+ (p[2]/2) , p[1]+ ((p[3]/2))),duration = 0.25)
pyautogui.click()
p = pyautogui.locateOnScreen('C:\Python37\Op.png',grayscale = False,confidence = 0.8)
pyautogui.moveTo((p[0]+ (p[2]/2) , p[1]+ ((p[3]/2))),duration = 0.25)
time.sleep(1)
pyautogui.moveTo((p[0]+ 363 , p[1]+ ((p[3]/2))),duration = 0.25)
pyautogui.moveTo(p[0]+ 363 , p[1] - 160,duration=0.25)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo((1670,1054),duration = 0.25)
pyautogui.click()
p = pyautogui.locateOnScreen('C:\Python37\p.PNG',grayscale = False,confidence = 0.8)
pyautogui.moveTo((p[0]+ (p[2]/2) , p[1]+ ((p[3]/2))),duration = 0.25)
pyautogui.click()
p = pyautogui.locateOnScreen('C:\Python37\Op.png',grayscale = False,confidence = 0.8)
pyautogui.moveTo((p[0]+ (p[2]/2) , p[1]+ ((p[3]/2))),duration = 0.25)
pyautogui.moveTo(p[0]+ (p[2]/2) , p[1] - 90,duration = 0.25)
pyautogui.click()
