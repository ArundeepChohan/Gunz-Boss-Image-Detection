import os
import sys

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
        
#print(os.path.abspath(os.sep))
os.chdir(os.path.abspath(os.sep))
cwd = os.getcwd()

from pathlib import Path
from bs4 import BeautifulSoup as bs
from pynput.keyboard import Key,Listener as KeyboardListener, Controller as KeyboardController
from pynput.mouse import Button,Listener as MouseListener, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()
"""
Use default settings in case config.xml is missing. 
Furthermore find a way to transcript the values gotten from the file into mouse/keyboard values
"""
moves_setting={
'useweapon':'e',
'useweapon2':'q',
'prevousweapon':-1,
'nextweapon': -1,
'foward':'w',
'back':'s',
'left':'a',
'right':'d',
'sword':'1',
'primaryweapon':'2',
'secondaryweapon':'3',
'item1':'4',
'item2':'5',
'communityitem1':-1,
'communityitem2':-1,
'reload':'r',
'jump':-1,
'score':-1,
'menu':-1,
'taunt':-1,
'bow':-1,
'wave':-1,
'laugh':-1,
'cry':-1,
'dance':-1,
'screenshot':-1,
'record':-1,
'movingpicture':-1,
'defence':-1,
'togglechat':-1,
'mousesensitivitydec':-1,
'mousesensitivityinc':-1,
'previoussong':-1,
'nextsong':-1,
'teamchat':-1,
'pingsystem':-1,
}
for path in Path(cwd).rglob('*Freestyle GunZ'):
    #print(path)
    os.chdir(path)
    cwd = os.getcwd()
    try:
        config_path=find('config.xml',os.getcwd())
        if config_path != None:
            print(config_path)
            content = []
            with open(config_path, "r") as file:
                soup = bs(file.read(), features='lxml')
                print(soup)
            break

    # Caching the exception   
    except:
        print("Something wrong with specified\
            directory. Exception- ", sys.exc_info())
            


        
