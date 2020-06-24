import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import time

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('YVGKHH-97XXLTX5EJ')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
engine.setProperty('rate',130)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning Boss')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon Boss')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening Boss')

greetMe()

# speak('Hello Boss')
# speak('How may I help you?')


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()

        if 'open youtube' in query:
            speak('Here it is')
            webbrowser.open('www.youtube.com')

        elif 'what is your name' in query:
            speak('My name is Iris, what\'s your\'s')
            name=myCommand();
            name=name.replace('I am ','')
            speak('Hi,'+name+', Glad to have a conversation with u')

        elif 'who are you' in query:
            speak('I am Gowtham\'s personal assistant')

        elif 'open google' in query:
            speak('Here it is')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('Here it is')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("gowara333@gmail.com", 'Mahtwogs333')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Boss!I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Boss, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Boss')

        elif 'hi' in query:
            speak('Hi Boss')

        elif 'bye' in query:
            speak('Bye Boss, have a good day.')
            sys.exit()

        elif 'play some music' in query:
            music_folder = 'C:\\Users\\gowar\\Music\\'
            music = ['Kala_Chashma']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            speak('Okay, here is your music! Enjoy!')
        elif 'search' in query:
            speak('What are you searching for?')
            search=myCommand()
            url='https://google.com/search?q=' + search
            speak('here is what I found for  '+search )
            webbrowser.get().open(url)
            print('here is what I found for ' + search )

        time.sleep(3)
        speak('Anyother')
