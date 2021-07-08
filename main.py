import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'beep boop' in command:
                command = command.replace('beep boop', '')
                print(command)
    except:
        pass
    return command


def run_beep():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('now playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time + 'Beep Boop')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info + 'Beep Boop')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'launch surpass' in command:
        talk('Launching Surpass. Beep Boop')
        talk('Welcome to Surpass, your assessment friend. Beep Boop')
        talk('Would you like to take a test or hear the results of a previous test? Beep Boop')
        talk("Say 'one' for taking a test. And 'two' for results")
    else:
        talk('Error. Please say the command again. Beep Boop')


while True:
    command = take_command()
    run_beep()
    if 'One' in command:
        talk('Are you sure you would like to take a test?')
    if 'two' in command:
        talk('Are you sure you would like to hear the results of a previous test?')
