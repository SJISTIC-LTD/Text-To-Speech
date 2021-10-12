The best library because you dont have to save the
text file or open the file to start the speech

pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello world")
engine.runAndWait()
from gtts import gTTS
from playsound import  playsound

mytext="Hello Geek! How are you doing??"
language='en'
myobj=gTTS(text=mytext,lang=language,slow=True)
myobj.save("welcome1.mp3")
playsound("welcome1.mp3")
#pip install SpeechRecognition
#in case of error use 'pip install pyaudio' or...
#in case of error use 'pip install pipwin' then 'pipwin install pyaudio'
#if error continued you may need to use python 3.6 or lower as the latest 
#python may not support pyaudio... 
import speech_recognition as sr
import pyttsx3

#audio of system to respond
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# simple function to recognise speech from user
def takecommand():
    #it takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print('User Said : ' , query)

    except Exception as e:
        print('exception : ',e)

        speak("Sorry, I didn't hear that, Say that again Please")
        return "None"
    return query
while True:
  query = takecommand() # whatever user says will be stored in this variable
  print("The Test got in program is : "+query)
  import speech_recognition as sr

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 50
        audio = r.listen(source)

    try:
        print('Recognizing...')
        qry = r.recognize_google(audio, language='en-in')
        print(f"user said: {qry}\n")
        
#     if any error occurs this line will run
    except Exeption as e:
    # if you don't want to print the error comment the bottom line
        print(e)
        print('Say that again please\n')
        return 'None'

    return qry
  
if __name__ == '__main__':
	while True:
  		qry = takecommand().lower()
  
# now you can use the takecommand function where you want to recognize speech
# And please experiment with the above code 
# like what pause_threshold and energy_threshold do 
pip install pyttsx3
import pyttsx3
friend = pyttsx3.init()
friend.say("you are very smart")
friend.runandwait()
from text_to_speech import speak

speak("Hello", "en", save=True, file="speech.mp3")
