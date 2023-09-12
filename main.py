import time
import moves
import takeScreenshot
import speechDetection
from pynput.keyboard import Key,Listener as KeyboardListener, Controller as KeyboardController
from pynput.mouse import Button,Listener as MouseListener, Controller as MouseController
import re

import asyncio

class GameManager():
    def __init__(self):
        self.moves = moves.Moves()
        # print(moves.settings)
        self.take_screenshot = takeScreenshot.TakeScreenShot()
        self.keyboard = KeyboardController()
        self.mouse = MouseController()
        self.speech_detection = speechDetection.SpeechDetection()
        self.listener2 = MouseListener(on_click=self.on_click)
        self.listener2.start()
        self.listener = KeyboardListener(on_press=self.on_press, on_release=self.on_release) 
        self.listener.start()
        self.directions=['FORWARD','BACK','LEFT','RIGHT']

    # Some helper functions to find button presses
    def on_press(self,key):
        print(key.__dict__)

    # Unblock the program if presses fail
    def on_release(self,key):
        if hasattr(key, 'vk'):
            print('You entered a number from the numpad: ', key.char, key.vk)
            print(key.__dict__)
        else:
            print(key.__dict__)       
        
    def on_click(self,x, y, button, pressed):
        if pressed:
            print ('Mouse clicked {2}'.format(x, y, button))

    def take_screen(self):
        print("Screening")
        self.take_screenshot.screen_shot()

    def swap_window(self):
        print('Swap window')
        if self.take_screenshot.active_window()!="Freestyle GunZ":
            self.take_screenshot.switch_window()
            time.sleep(3)
            print(self.take_screenshot.active_window())

    """
    Given some words breaks them into valid commands with valid optional parameters

    Ping                                                                -> Number (1-9)
    Macro                                                               -> Number (1-8)

    Single Use:
    Jump(any single use in self.settings in moves.py)                   -> Nothing
    Rotate                                                              -> Direction x,y, or maybe include Eyetracker?

    Comboes:
    Dash, Bf, Shoot                                                     -> Direction
    Rs                                                                  -> Number of Times

    Callbacks:
    Slashing, Blocking                                                  -> Nothing
    Walking                                                             -> Direction 
    
    \b(DASH|BF|SHOOT)\b\s*(FORWARD|BACK|LEFT|RIGHT)?|\b(RS)\b\s*(\d)?|\b(PING)\b\s*(\d{1})?(?!\d)|\b(MACRO)\b\s*\b([1-8])?\b
    (?:\b(DASH|BF|SHOOT)\b\s*(FORWARD|BACK|LEFT|RIGHT)?)|(?:\b(RS)+\s*(\d)?)|(?:\b(PING)+\s*(\d{1})?(?!\d))|(?:\b(MACRO)+\s*\b([1-8])?\b)
    """
    def commands(self,guess):
        #\b(dash|bf|shot)+\b(\s*forward|back|left|right)?(\s*\d)?
        #\b(dash|bf|shot)+\b(\s*\b(forward|back|left|right)\b)?(\s*\d)?
        #\b(DASH|BF|SHOOT)+\b(\s*(FORWARD|BACK|LEFT|RIGHT)?)?(\s*(\d)?)?
        #\b(DASH|BF|SHOOT)+\b(\s*FORWARD|BACK|LEFT|RIGHT)?(\s*\d)?
        #(?:\b(DASH|BF|SHOOT)+\s*(FORWARD|BACK|LEFT|RIGHT)?\s*(\d)?)|\b(PING)|\b(MACRO)
        pattern = re.compile(r"(?:\b(DASH|BF|SHOOT)\b\s*(FORWARD|BACK|LEFT|RIGHT)?)|(?:\b(RS)+\s*(\d)?)|(?:\b(PING)+\s*(\d{1})?(?!\d))|(?:\b(MACRO)+\s*\b([1-8])?\b)")
        res=[[item for item in match.groups()]for match in pattern.finditer(guess)]
        print(res)
        return res

    def start(self):
        print('Starting')
        while True:
            try:
                self.take_screenshot.list_processes() 
                try:
                    guess = self.speech_detection.recognize_speech_from_mic()
                    print(guess)
                    
                    if guess['error'] !='Unable to recognize speech' and guess['error'] !='API unavailable':
                        commands = self.commands(guess['transcription'].upper())
                        if len(commands)!=0:
                            print('Commands: ',commands)
                            self.swap_window()

                                # if "SPEED" in guess['transcription'].upper():
                                    # moves.speedy()
                                    # moves.register_callback(moves.corresponding_event(moves.settings['USEWEAPON'],[0.001,0.001]))
                                # if "BLOCK" in guess['transcription'].upper():
                                    # moves.block()
                                    # moves.register_callback(moves.corresponding_event(moves.settings['DEFENCE'],[0.001,0.001]))
                                # if "WALK" in guess['transcription'].upper():
                                    # print('walk')
                                    # moves.register_callback(moves.corresponding_event(moves.settings['FORWARD'],[0.001,0.001],False))
                            
                            try:
                                for command in commands:
                                    print(command[0])
                                    if "STOP" == command[0]:
                                        print('Delete callbacks')
                                    elif "RS" == command[2]:
                                        self.moves.reload_shot()
                                    
                                    elif "DASH" == command[0]:
                                        if command[1] in self.directions:
                                            self.moves.dash(dir=command[1])
                                        else:
                                            self.moves.dash() 
                                    elif "BF" == command[0]:
                                        if command[1] in self.directions:
                                            self.moves.butterfly(dir=command[1])
                                        else:
                                            self.moves.butterfly() 
                                    elif "SHOOT" == command[0]:
                                        if command[1] in self.directions:
                                            self.moves.slash_shot(dir=command[1])
                                        else:
                                            self.moves.slash_shot()
                                    elif "ROTATE" == command[0]:
                                        self.moves.rotate(self.take_screenshot.window_geometry())
                            except Exception as e:
                                print('Invalid command ',str(e))

                        if self.take_screenshot.active_window()=="Freestyle GunZ":
                            self.take_screen()
                except RuntimeError as e:
                    print('Changed Active Window',e) 
            except RuntimeError as e: 
                print('Freestyle Gunz not Open',e)            

def main():
    game_manager = GameManager()
    game_manager.start()

main()