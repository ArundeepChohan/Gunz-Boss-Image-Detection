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
        print('Screening')
        self.take_screenshot.screen_shot()

    def swap_window(self):
        print('Swap window')
        if self.take_screenshot.active_window()!="Freestyle GunZ":
            self.take_screenshot.switch_window()
            time.sleep(3)
            print(self.take_screenshot.active_window())

    """
    Given some words breaks them into valid commands with valid optional parameters

    Comboes:
    Dash, Bf, Shoot                                                     -> Direction
    Rs                                                                  -> Number of Times

    Ping                                                                -> Number (1-9)
    Macro                                                               -> Number (1-8)

    Single Use:
    Jump(any single use in self.settings in moves.py)                   -> Nothing
    Rotate                                                              -> Direction x,y, or maybe include Eyetracker?

    Callbacks:
    Slashing, Blocking                                                  -> Nothing
    Walking                                                             -> Direction 
    
    (?:\b(DASH|BF|SHOOT)\b\s*(FORWARD|BACK|LEFT|RIGHT)?)|(?:\b(RS)+\s*(\d)?)|(?:\b(PING)+\s*(\d{1})?(?!\d))|(?:\b(MACRO)+\s*\b([1-8])?\b)|((?:M(?:OUSE\sSENSITIVITY\s(?:DE|IN)C|ENU)|(?:COMMUNITY\s)?ITEM\s[12]|SECONDARY\sWEAPON|PR(?:EVIOUS\s(?:WEAPON|SONG)|IMARY\sWEAPON)|MOVING\sPICTURE|USE\sWEAPON\s[2]|MELEE\sWEAPON|(?:SCREEN\sSHOT)|T(?:OGGLE\sCHA|(?:EAM\sCHA|AUN))T|NEXT\sWEAPON|USE\sWEAPON|NEXT\sSONG|(?:D(?:EFE|A)NC|WAV)E|FORWARD|LEFT|RIGHT|RELOAD|RECORD|LAUGH|SCORE|B(?:ACK|OW)|JUMP|CRY))|(?:\b(ROTATE)\b(?!$)(?:\s*(?:(?:UP)\s*([1-9]|[1-9][0-9]|[12][0-9]{2}|3[0-5][0-9]|360)?)?\s*(?:(?:DOWN)\s*([1-9]|[1-9][0-9]|[12][0-9]{2}|3[0-5][0-9]|360)?)?\s*(?:(?:LEFT)\s*([1-9]|[1-9][0-9]|[12][0-9]{2}|3[0-5][0-9]|360)?)?\s*(?:(?:RIGHT)\s*([1-9]|[1-9][0-9]|[12][0-9]{2}|3[0-5][0-9]|360)?)?\s*)+)
    """
    def commands(self,guess):
        pattern = re.compile(r"(?:\b(DASH|BF|SHOOT)\b\s*(FORWARD|BACK|LEFT|RIGHT)?)|(?:\b(RS)+\s*(\d)?)|(?:\b(PING)+\s*(\d{1})?(?!\d))|(?:\b(MACRO)+\s*\b([1-8])?\b)|((?:M(?:OUSE\sSENSITIVITY\s(?:DE|IN)C|ENU)|(?:COMMUNITY\s)?ITEM\s[12]|SECONDARY\sWEAPON|PR(?:EVIOUS\s(?:WEAPON|SONG)|IMARY\sWEAPON)|MOVING\sPICTURE|USE\sWEAPON\s[2]|MELEE\sWEAPON|(?:SCREEN\sSHOT)|T(?:OGGLE\sCHA|(?:EAM\sCHA|AUN))T|NEXT\sWEAPON|USE\sWEAPON|NEXT\sSONG|(?:D(?:EFE|A)NC|WAV)E|FORWARD|LEFT|RIGHT|RELOAD|RECORD|LAUGH|SCORE|B(?:ACK|OW)|JUMP|CRY))|(?:\b(ROTATE)\b(?!$)(?:\s*(?:(?:UP)\s*([1-9]|[1-9][0-9]|[12][0-9]{2}|3[0-5][0-9]|360)?)?\s*(?:(?:DOWN)\s*([1-9]|[1-9][0-9]|[12][0-9]{2}|3[0-5][0-9]|360)?)?\s*(?:(?:LEFT)\s*([1-9]|[1-9][0-9]|[12][0-9]{2}|3[0-5][0-9]|360)?)?\s*(?:(?:RIGHT)\s*([1-9]|[1-9][0-9]|[12][0-9]{2}|3[0-5][0-9]|360)?)?\s*)+)")
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
                        
                        commands = self.commands(guess['transcription'])
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
                                    print("command", command)
                                    if "DASH" == command[0]:
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
                                    elif "RS" == command[2]:
                                        if command[3]!=None:
                                            self.moves.reload_shot(command[3])
                                        else:
                                            self.moves.reload_shot()
                                    elif "PING" == command[4]:
                                        self.moves.ping(command[5])
                                    elif "MACRO" == command[6]:
                                        self.moves.macro(command[7])
                                    elif command[8] != None:
                                        print('Single use: ',self.moves.settings[command[8].replace(" ", "")])
                                        self.moves.corresponding_event(self.moves.settings[command[8].replace(" ", "")],[.01,.01])
                                    elif "ROTATE" == command[9]:
                                        print(command[10],command[11],command[12],command[13])
                                        print(0 if command[10] is None else float(command[10]))
                                        self.moves.rotate(self.take_screenshot.window_geometry()
                                                          ,0 if command[10] is None else float(command[10])
                                                          ,0 if command[11] is None else float(command[11])
                                                          ,0 if command[12] is None else float(command[12])
                                                          ,0 if command[13] is None else float(command[13]))

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