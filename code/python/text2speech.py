# -*- coding: utf-8 -*-
"""
Created on Tue May 25 11:57:45 2021

@author: Robin
"""


from playsound import playsound
from gtts import gTTS
import os

x="Hello world"
  
    
tts = gTTS(text=x, lang='en')
ttsname=("name.mp3") 
tts.save(ttsname)
playsound("name.mp3")
os.remove(r"C:\Users\Robin\Desktop\project\RealTime\RealTime\name.mp3")
   