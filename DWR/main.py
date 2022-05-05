#pip install pyttsx3
#pip install plyer

from importlib import import_module

import pyttsx3 #(python text-to-speech version 3)used to convert text to speech 
from plyer import notification # Create a simple desktop notifier
import_module
import time

engine = pyttsx3.init('sapi5')#object Creation
voices = engine.getProperty('voices') # getting details of current speaking rate 
engine.setProperty('voice', voices[1].id) # setting up new voice rate 
def speak (audio): # to speak the written text 
    engine.say (audio)
    engine.runAndWait ()

if __name__ == "__main__":
    from webbrowser import open
    open('index.html')
    while True:
        notification.notify(
        app_name = "Drinkify",
        app_icon = "C:\Users\aksha\Python\glass-ico.ico",
        title = " Please Drink Water ",
        message = " Do you know ? Water helps in maintaining the tempreture of body and keeps us cool ",
        timeout = 12
    )
        speak("! Dear User ! please drink water and stay hydrated, Water helps in maintaining the tempreture of body and keeps us cool")
        import pyautogui
        pyautogui.keyDown("win")
        pyautogui.press("5")
        pyautogui.keyUp("win")
        time.sleep(60*60) # it will notify in every hour