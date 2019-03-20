import time
import datetime
from pygame import mixer
def music():
    mixer.init()
    mixer.music.load('med.mp3')
    mixer.music.play()
def get_current_time():
    cur_time=datetime.datetime.now()
    hour=cur_time.hour
    minute=cur_time.minute
    second=cur_time.second
    return (hour,minute,second)
def reminder_time(hour,minute,second):
    while True:
        if tuple([hour,minute,second])== get_current_time():
            music()
            break
reminder_time(14,37,40)

    
