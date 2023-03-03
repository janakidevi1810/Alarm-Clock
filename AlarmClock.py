from datetime import datetime   
import pyttsx3 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
        
def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"
while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
    
    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        print("count 1")
        if alarm_hour == current_hour:
            print("count 2")
            if alarm_min == current_min:
                print("count 3")
                if alarm_sec == current_sec:
                    print("Wake Up!")
                    speak("it is time to wake up")
                    break