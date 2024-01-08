import os
import random
import speech_recognition
import Brain
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
connection=Brain.Connection
commands_dict = {
    'commands': {
        'On_light': ['включи свет', 'включайся'],
        'Off_light': ['выключи свет', 'выключайся'],
        'Start_rele': ['реле', 'включи реле']
    }
}
def listen_command():
    """The function will return the recognized command"""
    
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            
        return query
    except speech_recognition.UnknownValueError:
        return 'Damn... Не понял что ты сказал :/'
    


query = listen_command()
    
for k, v in commands_dict['commands'].items():
    if query in v:
        print(globals()[k]())
  
  