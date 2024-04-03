import os
import eel
from inten import intents as a

from engine.features import *
eel.init("www")
from tqdm import tqdm
from time import sleep
def loard():
    for loarding in tqdm(range(100)):
        sleep(0.05)
loard()
playAssistantSound()
os.system('start msedge.exe --app="http://localhost:8000/index.html"')
eel.start('index.html', mode=None, host='localhost', block=True)
from engine.command import *