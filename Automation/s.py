import pyperclip
import re

text = str(pyperclip.paste())

ph = re.compile(r'#write what you want to find',re.I)

mo = ph.findall(text)

if len(mo) > 0:
    for i in range(len(mo)):
        print('Mobile NUmber (' +str(i) +')' +mo[i])
else:
    print('No NUmber found')
