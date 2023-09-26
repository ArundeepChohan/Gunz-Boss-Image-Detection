from enum import Enum
import time
from pynput.keyboard import Key, Controller as KeyboardController, KeyCode
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()

import findFile
findFile = findFile.FindFile()

import math

class Moves():
    def __init__(self):
        self.settings = findFile.current_settings()
        print(self.settings)

    def update(self):
        self.settings = findFile.current_settings()

    """
    <enum 'Button'> 
    <enum 'Key'> 
    <class 'str'> 
    <class 'int'>
    """
    def corresponding_event(self,key,delay=[0,0],release=True):
        print(type(key))
        if isinstance(key,Enum):
            if isinstance(key, Key):
                print('Key', key.value)
                keyboard.press(key)
                if release:
                    time.sleep(delay[0])
                    keyboard.release(key)
                    time.sleep(delay[1])
            elif isinstance(key, Button):
                print('Button', key.value)
                mouse.press(key)
                if release:
                    time.sleep(delay[0])
                    mouse.release(key)
                    time.sleep(delay[1])
        else:
            print('Key', key)
            keyboard.press(key)
            if release:
                time.sleep(delay[0])
                keyboard.release(key)
                time.sleep(delay[1])

    def dash(self,dir="FORWARD"):
        self.corresponding_event(self.settings[dir],[0.05,0.05])
        self.corresponding_event(self.settings[dir],[0.05,0.05])

    def butterfly(self,dir="FORWARD"):
        button_combinations = [self.settings['JUMP'],self.settings[dir],self.settings['USEWEAPON'],self.settings['DEFENCE']]
        print(button_combinations)
        self.corresponding_event(self.settings['JUMP'],[0.01,0.05])
        self.dash(dir)
        self.corresponding_event(self.settings['USEWEAPON'],[0.01,0.01])
        self.corresponding_event(self.settings['DEFENCE'],[0.01,0.01])
        # self.jump()
        # time.sleep(0.05)
        # self.dash(dir)
        # mouse.press(self.settings['USEWEAPON'])
        # time.sleep(0.01)
        # mouse.release(self.settings['USEWEAPON'])
        # time.sleep(0.01)
        # keyboard.press(self.settings['DEFENCE'])
        # time.sleep(0.01)
        # keyboard.release(self.settings['DEFENCE'])

    #Jump, Dash, Slash, Swap weapon, Shoot+Reload, then back to sword(optional)
    def slash_shot(self,dir="FORWARD",switch="PRIMARYWEAPON"):
        button_combinations = [self.settings['JUMP'],self.settings[dir],self.settings['MELEEWEAPON'],self.settings['USEWEAPON'],self.settings[switch],self.settings['RELOAD']]
        print(button_combinations)
        self.corresponding_event(self.settings['MELEEWEAPON'],[0.01,0.05])
        self.corresponding_event(self.settings['JUMP'],[0.01,0.05])
        self.dash(dir)
        self.corresponding_event(self.settings['USEWEAPON'],[0.05,0.01])
        self.corresponding_event(self.settings[switch],[0.05,0.05])
        self.corresponding_event(self.settings['USEWEAPON'],[0.01,0.05])
        self.corresponding_event(self.settings['RELOAD'],[0.01,0.01])
        self.corresponding_event(self.settings['MELEEWEAPON'],[0.01,0.05])

        # keyboard.type('1')
        # self.jump()
        # time.sleep(0.05)
        # self.dash(dir)
        # mouse.press(Button.left)
        # time.sleep(0.05)
        # keyboard.type('e')
        # time.sleep(0.05)
        # mouse.press(Button.left)
        # mouse.release(Button.left)
        # keyboard.type('1')

    # Slash, Switch, Shoot+Reload, Sword
    def gear_tap(self,dir="FORWARD",switch="PRIMARYWEAPON"):
        button_combinations = [self.settings['JUMP'],self.settings[dir],self.settings['MELEEWEAPON'],self.settings['USEWEAPON'],self.settings[switch],self.settings['RELOAD']]
        print(button_combinations)
        # keyboard.type('1')
        # self.jump()
        # time.sleep(0.05)
        # mouse.press(Button.left)
        # # time.sleep(0.05)
        # keyboard.type('e')
        # time.sleep(0.30)
        # mouse.release(Button.left)
        # time.sleep(0.05)
        # keyboard.type('1')
        # time.sleep(0.1)
        # self.dash(dir)

    def eflip(self,dir="FORWARD"):
        button_combinations = [self.settings[dir],self.settings['USEWEAPON2']]
        print(button_combinations)
        # keyboard.press(dir)
        # time.sleep(0.05)
        # keyboard.release(dir)
        # time.sleep(0.05)

        # keyboard.press(dir)
        # time.sleep(0.01)
        # keyboard.press('r')
        # time.sleep(0.05)
        # keyboard.release(dir)
        # time.sleep(0.01)
        # keyboard.release('r')

    def reload_shot(self,n=1):
        button_combinations = [self.settings['PRIMARYWEAPON'],self.settings['SECONDARYWEAPON'],self.settings['USEWEAPON'],self.settings['RELOAD']]
        print(button_combinations)
        for i in range(n):
            self.corresponding_event(self.settings['PRIMARYWEAPON'],[0.15,0.075])
            self.corresponding_event(self.settings['USEWEAPON'],[0.1,0.075])
            self.corresponding_event(self.settings['RELOAD'],[0.1,0.1])
            self.corresponding_event(self.settings['SECONDARYWEAPON'],[0.15,0.075])
            self.corresponding_event(self.settings['USEWEAPON'],[0.1,0.075])
            self.corresponding_event(self.settings['RELOAD'],[0.1,0.1])
            
            # keyboard.type('2')
            # time.sleep(0.10)
        
            # mouse.press(self.settings['USEWEAPON'])
            # time.sleep(0.20)
            # mouse.release(self.settings['USEWEAPON'])
            # time.sleep(0.10)
            
            # mouse.press(self.settings['RELOAD'])
            # time.sleep(0.20)
            # mouse.release(self.settings['RELOAD'])

            # keyboard.type('3')
            # time.sleep(0.10)
            # mouse.press(self.settings['USEWEAPON'])
            # time.sleep(0.20)
            # mouse.release(self.settings['USEWEAPON'])
            # time.sleep(0.10)

            # mouse.press(self.settings['RELOAD'])
            # time.sleep(0.20)
            # mouse.release(self.settings['RELOAD'])

    def ping(self,n=1):
        self.corresponding_event(self.settings['PINGSYSTEM'])

    #https://stackoverflow.com/questions/3286089/how-to-dynamically-compose-and-access-class-attributes-in-python
    def macro(self,n=1):
        self.corresponding_event(getattr(Key, 'f'+n))

    """
    Will use the window geometry from active window to find position? 
    1920x1080

    (todo)
    """
    def rotate(self,values,UP=0,DOWN=0,LEFT=0,RIGHT=0):
        print(values,UP,DOWN,LEFT,RIGHT)
        # Each degree has a x,y
        x=1920/360
        y=1080/360
        print('Now we have moved it to {0}'.format(mouse.position))
        mouse.move((-LEFT*x)+(RIGHT*x),(UP*y)+(-DOWN*y))
        # time.sleep(2)
        # print('Now we have moved it to {0}'.format(mouse.position))


# Todo Add Callbacks

    # """
    # Walking, Speedying, Blocking all can repeated until the user says stop.
    # For walking you don't let go of the key. Send a release variable to not click 
    # the key inside corresponding event. Check a [] for just speedy/blocking and call them again. 
    # (todo)
    # """
    # def speedy(self):
    #     button_combinations = [self.settings['USEWEAPON']]
    #     print(button_combinations)
    #     for i in range(10000):
    #         self.corresponding_event(self.settings['USEWEAPON'],[0.001,0.001])
    #         # mouse.press(Button.left)
    #         # time.sleep(0.001)
    #         # mouse.release(Button.left)
    #         # time.sleep(0.001)

    # def block(self):
    #     button_combinations = [self.settings['DEFENCE']]
    #     print(button_combinations)
    #     for i in range(10000):
    #         self.corresponding_event(self.settings['DEFENCE'],[0.001,0.001])
    #         # mouse.press(Button.right)
    #         # time.sleep(0.001)
    #         # mouse.release(Button.right)
    #         # time.sleep(0.001)