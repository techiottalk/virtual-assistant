import speech_recognition as sr
import os
from gtts import gTTS
import wolframalpha as wa
import wikipedia as wiki
import time

fn="hello1.mp3"
app_id = "YRRQ8V-P93VL22LR2"   #wolframalpha_api_id
welcome="hello i am assitant how can i help you "
ts=gTTS(welcome,lang="en",slow=False)
ts.save(fn)
os.system(fn)
time.sleep(3)
r = sr.Recognizer();
with sr.Microphone() as source:
     print(welcome)
     audio = r.listen(source);
try:
    inp = r.recognize_google(audio)
    print(inp)
except Exception as e:
       pass

try:
    # wolframalpha
    t = ['time','what is time','tell me time']
    if inp in t:
        answer=localtime = time.asctime( time.localtime(time.time()) )
    elif inp == 'who are you':
        answer = 'i am assistant'

    else:
          client = wa.Client(app_id)
          res = client.query(inp)
          answer = next(res.results).text
except:
    answer=wiki.summary(inp,sentences=2)


ts=gTTS(answer,lang="en",slow=False)
ts.save(fn)

print(answer)
os.system(fn)
time.sleep(20)
os.remove(fn)
