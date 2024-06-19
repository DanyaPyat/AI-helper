import os
import webbrowser
import sys
import subprocess
import pyttsx3

try:
    import requests
except:
    pass

engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0')


def speaker(text):
    engine.say(text)
    engine.runAndWait()


def browser():
    webbrowser.open('https://www.youtube.com', new=2)


def game():
    try:
        subprocess.call('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Badlion Client.lnk', shell=True)
        speaker('Ну как игра?')
    except:
        speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
    os.system('shutdown \s')
    # print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():
    try:
        params = {'q': 'London', 'units': 'metric', 'lang': 'ru', 'appid': '8c566e45b1c65d544d1be6395db6e688'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
    sys.exit()


def passive():
    pass
