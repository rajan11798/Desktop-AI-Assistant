import google as google
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import re
import requests
import time


engine = pyttsx3.init()

voices = engine.getProperty('voices')

#testing en-in
for voice in voices:
    if voice.languages[0] == 'en-in':
        engine.setProperty('voice', 60)
        break


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")
    #speak("I am ready to take your commands........")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open whatsapp' in query:
            reg_ex = re.search('open whatsapp (.*)', query)
            url = 'https://web.whatsapp.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            speak('Here, are your whatsapp messages, sir ')


        elif 'joke' in query:

            res = requests.get(

                'https://icanhazdadjoke.com/',

                headers={"Accept": "application/json"}

            )

            if res.status_code == requests.codes.ok:

                takeCommand(str(res.json()['joke']))

            else:

                takeCommand('oops!I ran out of jokes')


        elif 'open google' in query:
            reg_ex = re.search('open google (.*)', query)
            url = 'https://www.google.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            print('Done!')

        elif 'open youtube' in query:
            reg_ex = re.search('open youtube (.*)', query)
            url = 'https://www.youtube.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            print('Done!')

        elif 'open stackoverflow' in query:
            reg_ex = re.search('open stackoverflow (.*)', query)
            url = 'https://www.stackoverflow.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            print('Done!')


        #elif 'play music' in query:
        #   music_dir = '/home/gaurav/Music'
        #   songs = os.listdir(music_dir)
        #   os.system()(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        #elif 'open code' in query:
        #   codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #   os.startfile(codePath)

        elif 'email' or 'gmail' in command:
            speak('What is the subject?')
            time.sleep(1)
            subject = query()
            speak('What should I say?')
            time.sleep(1)
            message = query()
            content = 'Subject: {}\n\n{}'.format(subject, message)

            # init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            # identify to server
            mail.ehlo()

            # encrypt session
            mail.starttls()

            # login
            mail.login('anonymous70042@gmail.com', 'Dark@7004')

            # send message
            mail.sendmail('anonymous70042@gmail.com', 'graj499@gmail.com', content)

            # end mail connection
            mail.close()

            talk('Email sent.')

