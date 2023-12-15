import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def greet_user():
    speak("Hello! How can I assist you today?")

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The current time is {current_time}")

def get_date():
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {current_date}")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here is what I found for {query} on the web.")

def main():
    while True:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print('Listening...')
            audio = recognizer.listen(source)

        try:
            print('Recognizing...')
            command = recognizer.recognize_google(audio).lower()
            print('You said:', command)

            if 'hello' in command:
                greet_user()
            elif 'your name' in command:
                speak("I am a voice assistant created by OpenAI.")
            elif 'time' in command:
                get_time()
            elif 'date' in command:
                get_date()
            elif 'search' in command:
                query = command.replace('search', '').strip()
                search_web(query)
            elif 'exit' in command:
                speak("Goodbye!")
                break  # exit the loop
            else:
                speak("I'm sorry, I didn't understand that.")

        except sr.UnknownValueError:
            print('Sorry, I could not understand the audio.')

        except sr.RequestError as e:
            print(f'Request failed; {e}')

if __name__ == "__main__":
    main()
