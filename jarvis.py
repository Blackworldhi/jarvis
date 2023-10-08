import pyttsx3
import speech_recognition as sr
import datetime
import os
import pywhatkit
import pyautogui
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',200)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()


def commands():
  r=sr.Recognizer()
  with sr.Microphone() as source:
      print("Listening.....")
      r.pause_threshold=1
      r.adjust_for_ambient_noise(source, duration=1)
      audio = r.listen(source)
  try:
    print("Wait for Few Moments....")
    query=r.recognize_google(audio, language='en-in')
    print(f"You just said: {query}/n")
  except Exception as e:
     print(e)
     speak("please Tell me again")
     query="none"
  return query


speak("hello sir")
speak("how can i help you")


if __name__ == "__main__":

   query=commands().lower()
   if 'time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      print(strTime)
      speak(f"Sir,the time is {strTime}")


   elif 'open google' in query:
      speak("Opening google sir...")
      os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

   elif 'play' in query:
      query=query.replace('play', '')
      speak('playing' + query)
      pywhatkit.playonyt(query)
      
   elif 'type' in query:
      speak("Please tell me what should i write")
      while True:
         writeInNotepad=commands()
         if writeInNotepad=='exit typing':
             speak("Done sir")
         else:
              pyautogui.write(writeInNotepad)
      
   elif 'exit' in query:
      speak("I'm Leaving sir, bye!")
      quit()

   elif 'open youtube' in query:
      speak("Opening youtube...")
      webbrowser.open("https://www.youtube.com/")
  
   elif 'open spotify' in query:
      speak("Opening spotify...")
      webbrowser.open("https://open.spotify.com/collection/tracks")
