
from gtts import gTTS
import os 
mytext ='This is a to remind you about your health problems'

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("med.mp3") 

os.system("mpg321 new.mp3") 
