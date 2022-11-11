# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 00:23:28 2022

@author: Mohammed Islam
"""

import speech_recognition as sr

### SPEECH RECOGNITION USING SPHINX ###
--------------------------------------------------------------
def init_func(inquiry):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(inquiry)
        audio = r.listen(source)
    
    try:
        spch = r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    
    return spch

### PARSING TEXT FUNCTION ###
--------------------------------------------------------------
        
def parse(atext,wtext):
    if wtext in atext:
        return wtext
    else:
        return False
 
### TASK CHOOSING FUNCTION ###
--------------------------------------------------------------

def choose(x):
    return {
            'turn on the lights': 1,
            'play a song': 2,
            'what time is it': 3
            }.get(x, 9)
    
### INITIALIZATION ###    
--------------------------------------------------------------

assistantName = 'jarvis'

x = init_func('Say Something')
y = parse(x, assistantName)
if y == assistantName:
    a = init_func('What do you want me to do?')
    b = choose(a)
    print(b)
else:
    print("no")
