import time
from pynput.keyboard import Controller,Key
from datetime import datetime

import webbrowser

cmpClass = ["https://us04web.zoom.us/j/4750912222?pwd=SHkrUU5EcUlJOGFUK1M4V003TXp2Zz09", '14:57','14:58']

keyboard = Controller()
def main():
    meetingStarted = False
    while True:
        if meetingStarted == False:
            if datetime.now().hour == int(cmpClass[1].split(":")[0]) and datetime.now().minute == int(cmpClass[1].split(":")[1]):
                webbrowser.open(cmpClass[0])
                meetingStarted = True
        elif meetingStarted == True:
            if datetime.now().hour == int(cmpClass[2].split(":")[0]) and datetime.now().minute == int(cmpClass[2].split(":")[1]):
                keyboard.press("q")
                time.sleep(1)
                keyboard.press(Key.enter)
                meetingStarted = False



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
