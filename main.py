import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import smtplib
import feedparser
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)

wikipedia.set_lang("pt")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def escutar():
    hora = int(datetime.datetime.now().hour)
    if hora >= 0 and hora < 12:
        speak("Bom dia")
    elif hora >= 12 and hora < 18:
        speak("Boa tarde")
    else:
        speak("Boa noite")


def comandos():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Escutando")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizando...")
        query = r.recognize_google(audio, language="pt-BR")
        print(f"Usuário disse: {query}")

    except Exception as e:
        print(e)
        print("Não consigo escutar sua voz")
        return "None"
    
    return query

## MAIN ##
if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    escutar()

    while True:

        query = comandos().lower()

        ##### BUSCA NA WIKI ###

        if 'buscar sobre' in query:            
            query = query.replace("buscar sobre", "")
            speak(f"Buscando sobre {query}")
            results = wikipedia.summary(query, sentences = 3)
            print(results)
            speak(results)
