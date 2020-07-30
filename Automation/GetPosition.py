import pyautogui
from os import system
print('Press Ctrl-C to Quit')
try:
    while True:
        x,y = pyautogui.position()
        positionStr = 'X: ' +str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print (positionStr)
        positionStr = positionStr.rstrip("\n")
        

except KeyboardInterrupt:
            print('\nDone')
