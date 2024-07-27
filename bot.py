import speech_recognition as sr
import subprocess
import webbrowser
import pyowm
import translators as ts
import gpt 
import gtts
import os

recognizer = sr.Recognizer()

owm = pyowm.OWM('5817d6a145c443107efc34417e35c2ac')

def capture_voice_input():
    with sr.Microphone() as source:
        print("Слухаю...")
        audio = recognizer.listen(source)
    return audio

def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio,language="uk-UK")
        print("Ви сказали: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Вибачте, але я Вас не розумію.")
    except sr.RequestError as e:
        text = ""
        print("Помилка; {0}".format(e))
    return text

def process_voice_command(text):

    if "привіт" in text.lower():
        return ("Привіт! Як я можу Вам допомогти?")

    elif "як справи" in text.lower():
        return ("Супер, а у Вас?")
    
    elif "дякую" in text.lower():
        return ("Радий був Вам допомогти, якщо є питання готовий вислухати!")

    elif "калькулятор" in text.lower():
        subprocess.call(['calc'])

    elif "логіка" in text.lower():
        webbrowser.open("https://learn.logikaschool.com/login")
    
    elif "youtube" in text.lower():
        webbrowser.open(f"https://youtube.com/results?search_query={text.lower()[7:]}")

    elif "хром" in text.lower() or "chrome" in text.lower():
        subprocess.call(["C:\Program Files\Google\Chrome\Application\chrome.exe"])

    elif "погода" in text.lower():
        place = text[7:]
        place = ts.translate_text(place, from_language='uk', to_language='en')
        observation = owm.weather_manager().weather_at_place(place)
        location = observation.location
        weather = observation.weather
        weather = "Температура (градусів Цельсію): " + str(int(weather.temperature('celsius')['temp']))
        try:
            myobj = gtts.gTTS(text=weather, lang='uk', slow=False)
            myobj.save("weather.mp3")
            os.system("weather.mp3")
        except Exception as ex:
            print( ex)
            raw_input()
        return weather

    elif "джарвіс" in text.lower() or "jarvis" in text.lower():
        result = gpt.generate(text+ " and translate into Ukrainian. Don't print English words")
        try:
            myobj = gtts.gTTS(text=result, lang='uk', slow=False)
            myobj.save("result.mp3")
            os.system("result.mp3")
        except Exception as ex:
            print( ex)
            raw_input()
        return result

    elif "напиши код" in text.lower():
        code = gpt.generate(text + " і виведи тільки код без інших слів")[3:-3]
        with open('generated_code.py', 'w',encoding='utf-8') as file:
            file.write(code)
        return ("Код готовий, можете тестувати)")
    elif "стоп" in text.lower() or "прощавай" in text.lower() or "бувай" in text.lower():
        return True
    else:
        print("Я Вас не розумію. Повторіть Ваш запит")
    return False

def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)
    return end_program

if __name__ == "__main__":
    main()