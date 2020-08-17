import pyttsx3


data = input("enter the text i want to user input:")
engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()