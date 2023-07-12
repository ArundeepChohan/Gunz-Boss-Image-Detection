import os
import sys

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
        
#print(os.path.abspath(os.sep))
os.chdir(os.path.abspath(os.sep))
cwd = os.getcwd()
print('Root folder of the os system: ',cwd)

from pathlib import Path
from bs4 import BeautifulSoup as bs
from pynput.keyboard import Key,Listener as KeyboardListener, Controller as KeyboardController
from pynput.mouse import Button,Listener as MouseListener, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()

"""
Use default settings in case config.xml is missing. 
Furthermore find a way to transcript the values gotten from the file into mouse/keyboard values
<enum 'Key'> <class 'str'> <enum 'Button'>

"""
moves_setting = {
'USEWEAPON':'e',
'USEWEAPON2':'q',
'PREVOUSWEAPON':-1,
'NEXTWEAPON': -1,
'FORWARD':'w',
'BACK':'s',
'LEFT':'a',
'RIGHT':'d',
'MELEEWEAPON':'1',
'PRIMARYWEAPON':'2',
'SECONDARYWEAPON':'3',
'ITEM1':'4',
'ITEM2':'5',
'COMMUNITYITEM1':-1,
'COMMUNITYITEM2':-1,
'RELOAD':'r',
'JUMP': Key.space,
'SCORE':-1,
'MENU':-1,
'TAUNT':-1,
'BOW':-1,
'WAVE':-1,
'LAUGH':-1,
'CRY':-1,
'DANCE':-1,
'SCREENSHOT': Key.f12,
'RECORD': Key.f11,
'MOVINGPICTURE':-1,
'DEFENCE': Key.shift,
'TOGGLECHAT':-1,
'MOUSESENSITIVITYDEC':-1,
'MOUSESENSITIVITYINC':-1,
'PREVIOUSSONG':-1,
'NEXTSONG':-1,
'TEAMCHAT':-1,
'PINGSYSTEM':Key.alt,
}

config_path = None
paths = Path(cwd).rglob('*Freestyle GunZ')

for path in paths:
    #print(path)
    os.chdir(path)
    cwd = os.getcwd()
    try:
        config_path = find('config.xml',os.getcwd())
        if config_path != None:
            print(config_path)
            with open(config_path, "r") as file:
                soup = bs(file.read(),'xml')
                for key in moves_setting:
                    print(key,soup.find(key).contents)
            break
            
    # Caching the exception   
    except:
        print("Something wrong with specified\
            directory. Exception- ", sys.exc_info())
            



        
