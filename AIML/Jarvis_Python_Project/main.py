import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

recognizer = sr.Recognizer() # Initialize recognizer
engine = pyttsx3.init() # Initialize text to speech
newsapi = "https://newsapi.org/v2/top-headlines?country=us&apiKey=0bc165d800144593ac17ec6dc64f5721"
myApiKey = "0bc165d800144593ac17ec6dc64f5721"

def speak(text):
    engine.say(text)
    engine.runAndWait() #Otheriwse it exists without saying

def aiProcess(command):
    client = OpenAI(
    api_key="org-7pjyovieWtsPNyJE567NdtjM",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual ssistant named Jarvis, created by your Master Tanishq Thuse, you are skilled in explaining general tasks like Alexa and google cloud and complex programming concepts with creative flair."},
        {"role": "user", "content": "What is coding?"}
    ]
    )

    print(completion.choices[0].message.content)

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    elif("open linkedin" in c.lower()):
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif("open college website" in c.lower()):
        speak("Opening college website")
        webbrowser.open("https://learner.vierp.in/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif c.lower().startswith("abp"):
        webbrowser.open("https://www.youtube.com/watch?v=m0MD6Ukm0cQ")
    elif "news" in c.lower():
        speak("Latest news")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={myApiKey}")
        if(r.status_code == 200):
            #Parsing the JSON data
            #Parsing is the process of converting data from one format to another
            #Here the format is converted to json
            data = r.json()
            
            #Extracting the news from the JSON data
            articles = data.get('articles', [])

            #Print the headlines
            for article in articles:
                print(article['title'])
                speak(article['title'])
    # else:
        #Let OpenAI handle the request



if __name__ == "__main__":
    speak("Initialising Jarvis")

    while True:
        # Listen for the wake word "Jarvis"
        #Obtain audio from the microphone
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source: #Use the microphone as the audio source
                print("Listening...")       #Print some text to let the user know that Jarvis is listening
                audio = r.listen(source, timeout=2, phrase_time_limit=1)  #Listen for the audio from the microphone


            print("recognizing...")
            #Use the recognizer to convert the audio to text
            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "jarvis"):
                # Listen for the command
                speak("Yes, how can I help you?")

                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis is Active...")
                    #timeout is how much time it's waiting for the user to start speaking
                    #phrase_time_limit is how much time it's waiting for the user to complete speak 
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print(e)



        # except sr.UnknownValueError:
        #     print("Jarvis did not understand what you said")
        # except sr.RequestError as e:
        #     print("Sorry, the service is down".format(e))