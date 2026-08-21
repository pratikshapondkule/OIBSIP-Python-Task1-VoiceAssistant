import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""

    except sr.RequestError:
        speak("Sorry, there is a problem with the speech service.")
        return ""


def voice_assistant():
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:
        command = listen()

        if "hello" in command or "hi" in command:
            speak("Hello! How are you?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + current_date)

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open facebook" in command:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")

        elif "search" in command:
            search_query = command.replace("search", "").strip()

            if search_query:
                speak("Searching for " + search_query)
                webbrowser.open(
                    "https://www.google.com/search?q=" +
                    search_query.replace(" ", "+")
                )

        elif "stop" in command or "exit" in command or "bye" in command:
            speak("Goodbye! Have a nice day.")
            break

        elif command == "":
            continue

        else:
            speak("I don't know that command yet.")


# Start assistant
if __name__ == "__main__":
    voice_assistant()