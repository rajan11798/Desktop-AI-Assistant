import google as google
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import re
import requests
import time

engine = pyttsx3.init()

voices = engine.getProperty('voices')

# testing en-in
for voice in voices:
    if voice.languages[0] == 'en-in':
        engine.setProperty('voice', 20)
        break


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    time.sleep(1)
    speak("I am Jarvis . Sir. Please tell me how may I help you")
    time.sleep(1)
    speak("I am ready to take your commands.")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anonymous70042@gmail.com', 'Dark@7004')
    #server.sendmail('anonymous70042@gmail.com', 'graj499@gmail.com', content)
    server.sendmail('anonymous70042@gmail.com', 'vikasss.js@gmail.com', content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            time.sleep(1)
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open google' in query:
            reg_ex = re.search('open youtube (.*)', query)
            url = 'https://www.youtube.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            print('Done!')
            speak('here are your results sir...')

        elif 'what\'s up' in query:
            speak('Just doing my work sir, how is your day sir...!')

        elif 'prince' in query:
            speak('He is a bull, also known as The Anonymous Bull')


        elif 'open youtube' in query:
            reg_ex = re.search('open youtube (.*)', query)
            url = 'https://www.youtube.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            speak('Here ! , is your youtube sir')

        elif 'open whatsapp' in query:
            reg_ex = re.search('open whatsapp (.*)', query)
            url = 'https://web.whatsapp.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            speak('Here, are your whatsapp messages, sir ')

        elif 'open website' in query:
            reg_ex = re.search('open website (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.' + domain
                webbrowser.open(url)
                speak('Here, is your website sir...')
            else:
                pass

        elif 'open stackoverflow' in query:
            reg_ex = re.search('open stackoverflow (.*)', query)
            url = 'https://www.stackoverflow.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            print('Done!')
            speak('Here, is your stackoverflow sir')


        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            time.sleep(1)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = " "
            os.startfile(codePath)

        elif 'gmail' or 'email' in query:
            try:
                speak('establishing coonections ..., please wait')
                time.sleep(1)
                speak('connection established sir..., now you can send email , sir')
                time.sleep(1)
                speak("What should I say?")
                time.sleep(1)
                content = takeCommand()
                #to = "yogeshrathore@gmail.com"
                to = "vikasss.js@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully...")
                break
            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able to send this email")



        elif 'joke' or 'jokes' in query:

            res = requests.get(

                'https://icanhazdadjoke.com/',

                headers={"Accept": "application/json"}

            )

            if res.status_code == requests.codes.ok:

                speak(str(res.json()['joke']))
                break

            else:

                speak('oops!I ran out of jokes')
