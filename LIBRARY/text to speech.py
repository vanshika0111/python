# import os
# from gtts import gTTS
# mytext = "meri pyari mummy"
# language = 'hi'
# myobj = gTTS(text=mytext, lang=language,slow=False)
# myobj.save("hello.mp3")
# os.system("start hello.mp3")

import os
from gtts import gTTS
mytext = "rishika please for god's sake go and study"
language = 'en'
myobj = gTTS(text=mytext, lang=language,slow=False)
myobj.save("hello.mp3")
os.system("start hello.mp3")

