import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import time


def init():
    print(f"\nWelcome to Bilingual Oral Practice.\n")
    print(f'This machine support the following voice: ')
    for idx, v in enumerate(voices):
        print(f"Option {idx + 1}: {v.name}")
    print(f'Please pick one Language: ')
    choice = input()
    while not choice.isdigit() or int(choice) not in range(1, len(voices) + 1):
        print(f'Please choose only from 1 - {len(voices)}: ')
        choice = input()
    choice = int(choice)
    print(f'You choose {voices[choice - 1].id}')
    engine.setProperty('voice', voices[choice - 1].id)
    print(f'Please choose voice speed: 1:slow, 2:fast: ')
    speed = input()
    while speed not in ['1', '2']:
        print(f'Please choose only 1 or 2: ')
        speed = input()
    speed = 120 if speed == '1' else 200
    engine.setProperty("rate", speed)
    print(f'Please select the content file.')


def talk(text):
    if isinstance(text, list):
        for w in text:
            engine.say(w)
            engine.runAndWait()
    else:
        engine.say(text)
        engine.runAndWait()


def inputVoice():
    print('Listening:')
    with sr.Microphone() as source:
        audio = listener.listen(source)
        voice_data = ''
        try:
            voice_data = listener.recognize_google(audio, language='cmn-Hans-CN')
        except:
            pass
    print('Done Listening')
    return voice_data.lower()

def checkSpeak(root, index):
    voiceInput = inputVoice()
    style = ttk.Style()
    style.configure("BW.TLabel", foreground="red")
    ttk.Label(root, text=voiceInput, style='BW.TLabel', font=("Roboto", 30), justify='center').grid(row=index, column=3)

def readFile():
    root = tk.Tk()
    filename = askopenfilename()
    with open(filename, encoding="utf8") as my_file:
        arr = my_file.readlines()
    root.destroy()
    my_file.close()
    return arr


def test(arr):
    root = tk.Tk()
    root.title('Say Out Loud')
    root.geometry('800x600')
    for idx, ele in enumerate(arr):
        tk.Label(root, text=ele, font=("Roboto", 30), justify='center').grid(row=idx, column=0)
        tk.Button(root, text='Listen', command=lambda text=ele: talk(text)).grid(row=idx, column=1)
        tk.Button(root, text='Speak', command=lambda index=idx: checkSpeak(root, index)).grid(row=idx, column=2)
    root.mainloop()


if __name__ == '__main__':
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    init()
    time.sleep(0.5)
    textArr = readFile()
    test(textArr)
