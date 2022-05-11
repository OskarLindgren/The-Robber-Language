from gtts import gTTS
from time import sleep
import os
import pyglet

konsonanter = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"
print("Press [Crtl + C] at any point to exit the program")

from configparser import ConfigParser
config = ConfigParser()


while True:
    cur_tts = input("Write something!\n")
    
    for n in konsonanter:
        new = str(n + "o" + n)
        cur_tts = cur_tts.replace(n, new)
    print(cur_tts)
    

    lang = 'en'
    tld = 'us'
    dir = "C:/temp"
    sound_file = f"{dir}/text.mp3"


    tts = gTTS(cur_tts, lang=lang, tld=tld)
    tts.save(sound_file)
    
    speech = pyglet.media.load(sound_file)
    speech.play()
    
    
    sleep(speech.duration)
    os.remove(sound_file)