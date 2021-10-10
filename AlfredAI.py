import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import smtplib

print('initializing alfred')

MASTER= 'person'

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait

def wishme():
    hour=int (datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak ('good morning'+MASTER)

    if hour>=12 and hour <4:
        print('good afternoon'+MASTER)

    elif hour>=4 and hour <6:
        print('good evening'+MASTER)

    else:
        print("good night"+MASTER)

    speak('hello , iam alfred. how can i help you')    
    
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone as source:
        print('listening...')
        audio=r.listen(source)

    try:
        print('recognizing...')
        query= r.recognize_google('audio',language= 'en-in')
        print(f'user said:{query}/n')
    
    except Exception as e:
        print('can you please say that again')
        query=None
        return query()

def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    server.sendmail('abcd@gmail.com',  to,  content)
    server.close()

def main():
    speak('initializing alfred....')
    wishme()
    query=takecommand()

    if 'wikipedia' in query.lower:
        speak("searching wikipedia...")
        query=query.replace('wikipedia','')
        results = wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)

    elif'open youtube' in query.lower():
        #webbrowser.open('youtube.com')
        url='youtube.com'
        chrome_path= 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)


    elif'open google' in query.lower():
        #webbrowser.open('youtube.com')
        url='google.com'
        chrome_path= 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)


    elif'open reddit' in query.lower():
        #webbrowser.open('youtube.com')
        url='reddit.com'
        chrome_path= 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif'play music' in query.lower:
        songs_dir='C:\\Users\\Public\\Music'
        songs=os.listdir('songs_dir')
        print(songs)
        os.startfile(os.join(songs_dir,songs[0]))

    elif "the time" in query.lower():
        strTime= datetime.datetime.now().strftime('%H,%M,%S')
        speak(f'{MASTER} the time is {strTime}')

    elif 'open code' in query.lower():
        codePath = 'C:\\vs code\\Microsoft VS Code'
        os.startfile(codePath)

    elif 'email to abcd' in query.lower():
        try:
            speak('what should i send')
            content= takecommand
            to = 'abcd@gmail.com'
            sendEmail( to,  content)
            speak('email has been sent successsfully')

        except Exception as e:
            print(e)
main()
