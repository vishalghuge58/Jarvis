import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak a message
def speak(message):
    engine.say(message)
    engine.runAndWait()

# Define a function to listen for user input
def listen():
    with sr.Microphone() as source:
        print("How can I assist you?")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said: " + command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError:
        print("Sorry, I could not process your request at this time.")

# Main loop to listen for user input and respond
while True:
    command = listen().lower()

    if "hello" in command:
        speak("Hello there!")
    elif "what's the weather like" in command:
        speak("I'm sorry, I cannot get the weather at the moment.")
    elif "exit" in command:
        speak("Goodbye!")
        break
    elif "google" in command:
        webbrowser.open("google.com")
    else:
        speak("I'm sorry, I didn't understand that.")
