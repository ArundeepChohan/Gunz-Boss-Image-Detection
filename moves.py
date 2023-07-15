import time
from pynput.keyboard import Key,Listener as KeyboardListener, Controller as KeyboardController, KeyCode
from pynput.mouse import Button,Listener as MouseListener, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()

import findFile
findFile = findFile.FindFile()

class Moves():
    def __init__(self):
        self.settings = findFile.current_settings()

    def update(self):
        self.settings = findFile.current_settings()

    """
    <enum 'Button'> 
    <enum 'Key'> 
    <class 'str'> 
    <class 'int'>
    """
    def corresponding_event(self,key):
       print(type(key))

    def dash(self,dir):
        # keyboard.type(self.settings[dir])
        # keyboard.type(self.settings[dir])
        keyboard.press(self.settings[dir])
        time.sleep(0.05)
        keyboard.release(self.settings[dir])
        time.sleep(0.05)
        keyboard.press(self.settings[dir])
        time.sleep(0.05)
        keyboard.release(self.settings[dir])

    def jump(self):
        self.corresponding_event(self.settings['JUMP'])
        keyboard.press(self.settings['JUMP'])
        keyboard.release(self.settings['JUMP'])

    def reload_shot(self):
        button_combinations = [self.settings['PRIMARYWEAPON'],self.settings['SECONDARYWEAPON'],self.settings['USEWEAPON'],self.settings['RELOAD']]
        print(button_combinations)
        for i in range(5):
            keyboard.type('2')
            time.sleep(0.10)
            mouse.press(self.settings['USEWEAPON'])
            time.sleep(0.20)
            mouse.release(self.settings['USEWEAPON'])
            time.sleep(0.10)
            mouse.press(self.settings['RELOAD'])
            time.sleep(0.20)
            mouse.release(self.settings['RELOAD'])

            keyboard.type('3')
            time.sleep(0.10)
            mouse.press(self.settings['USEWEAPON'])
            time.sleep(0.20)
            mouse.release(self.settings['USEWEAPON'])
            time.sleep(0.10)
            mouse.press(self.settings['RELOAD'])
            time.sleep(0.20)
            mouse.release(self.settings['RELOAD'])

    def butterfly(self,dir):
        button_combinations = [self.settings['JUMP'],self.settings[dir],self.settings['USEWEAPON'],self.settings['DEFENCE']]
        print(button_combinations)
        self.jump()
        time.sleep(0.05)
        self.dash(dir)
        mouse.press(self.settings['USEWEAPON'])
        time.sleep(0.01)
        mouse.release(self.settings['USEWEAPON'])
        time.sleep(0.01)
        keyboard.press(self.settings['DEFENCE'])
        time.sleep(0.01)
        keyboard.release(self.settings['DEFENCE'])

    #Jump, Dash, Slash, Swap weapon, Shoot, then back to sword(optional)
    def slash_shot(self,dir):
        keyboard.type('1')
        self.jump()
        time.sleep(0.05)
        self.dash(dir)
        mouse.press(Button.left)
        time.sleep(0.05)
        keyboard.type('e')
        time.sleep(0.05)
        mouse.press(Button.left)
        mouse.release(Button.left)
        keyboard.type('1')

    # slash, switch, shoot+reload, sword
    def gear_tap(self,dir):
        keyboard.type('1')
        self.jump()
        time.sleep(0.05)
        mouse.press(Button.left)
        # time.sleep(0.05)
        keyboard.type('e')
        time.sleep(0.30)
        mouse.release(Button.left)
        time.sleep(0.05)
        keyboard.type('1')
        time.sleep(0.1)
        
        self.dash(dir)

    def speedy(self):
        for i in range(10000):
            mouse.press(Button.left)
            time.sleep(0.001)
            mouse.release(Button.left)
            time.sleep(0.001)

    def block(self):
        for i in range(10000):
            mouse.press(Button.right)
            time.sleep(0.001)
            mouse.release(Button.right)
            time.sleep(0.001)

    # I think it's 1 second jump length
    def jump_time(self):
        for i in range(10):
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            time.sleep(1)

    # dash with alt fire (todo)
    def eflip(self,dir):
        
        keyboard.press(dir)
        time.sleep(0.05)
        keyboard.release(dir)
        time.sleep(0.05)
        keyboard.press(dir)
        time.sleep(0.01)
        keyboard.press('r')
        time.sleep(0.05)
        keyboard.release(dir)
        time.sleep(0.01)
        keyboard.release('r')
        # mouse.click(Button.button10)
        # mouse.press(Button.button10)
        # mouse.release(Button.button10)