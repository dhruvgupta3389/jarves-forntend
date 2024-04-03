from tkinter import *
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

root = Tk()
root.geometry("600x450")
root.title("LISA 1.0")

response_label = Label(root, text="", font=("Helvetica", 14))
response_label.pack(pady=20)

def speak(audio):
    response_label.config(text=audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Lisa. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        response_label.config(text="Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        response_label.config(text="Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        response_label.config(text=f"User said: {query}")
    except Exception as e:
        response_label.config(text="Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('@gmail.com', '287')
    server.sendmail('@gmail.com', to, content)
    server.close()

def process_command():
    query = takeCommand().lower()

    try:
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\DELL\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\OneDrive\\Desktop\\coding\\.vscode\\.vscode\\Vishal"
            os.startfile(codePath)
        elif 'email to vaishnavi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vaishnavi20@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry, I am not able to send this email")
        elif 'what about you' in query:
            speak("I am Lisa! What should I help you with.")
        elif 'quit the program' in query or 'bye' in query:
            speak("Quitting")
            speak("Thank you, Have a nice day.")
            root.destroy()
    except wikipedia.exceptions.DisambiguationError as e:
        speak("Wikipedia search resulted in a disambiguation page. Please provide more specific information.")
    except wikipedia.exceptions.PageError as e:
        speak("Sorry, no information found on Wikipedia for the given query.")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")

# Create a button to start the assistant
start_btn = Button(root, text="Start", command=wishMe)
start_btn.pack(pady=20)

# Create a button to process the command
process_btn = Button(root, text="Process Command", command=process_command)
process_btn.pack(pady=10)

root.mainloop()
