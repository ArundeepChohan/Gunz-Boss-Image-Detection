import time
import moves
import takeScreenshot
import speechDetection
from pynput.keyboard import Key,Listener as KeyboardListener, Controller as KeyboardController
from pynput.mouse import Button,Listener as MouseListener, Controller as MouseController

# moves = moves.Moves()
# # print(moves.settings)
# take_screenshot = takeScreenshot.TakeScreenShot()

# keyboard = KeyboardController()
# mouse = MouseController()
# speech_detection = speechDetection.SpeechDetection()

# # Some helper functions to find button presses
# def on_press(key):
#     print(key.__dict__)

# # Unblock the program if presses fail
# def on_release(key):
#     if hasattr(key, 'vk'):
#         print('You entered a number from the numpad: ', key.char, key.vk)
#         print(key.__dict__)

#     else:
#         print(key.__dict__)       
        
# listener = KeyboardListener(on_press=on_press, on_release=on_release) 
# listener.start()

# def on_click(x, y, button, pressed):
#     if pressed:
#         print ('Mouse clicked {2}'.format(x, y, button))

# listener2 = MouseListener(on_click=on_click)
# listener2.start()

# """

# """
# def run():
#     global take_screenshot,moves,speech_detection
    
#     try:
#         take_screenshot.list_processes()
#         try:
#             while True:
#                 take_screenshot.screen_shot()
#                 guess = speech_detection.recognize_speech_from_mic()
#                 print(guess)
#                 if guess['error'] !='Unable to recognize speech':
#                     if take_screenshot.active_window()!="Freestyle GunZ":
#                         take_screenshot.switch_window()
#                         time.sleep(3)
#                         print(take_screenshot.active_window())

#                     """
#                     (\w+)(?:/d)? Matches any group of words with optional number group
#                     Make it one or more word
#                     """
#                     # if "SPEED" in guess['transcription'].upper():
#                         # moves.speedy()
#                         # moves.register_callback(moves.corresponding_event(moves.settings['USEWEAPON'],[0.001,0.001]))
#                     # if "BLOCK" in guess['transcription'].upper():
#                         # moves.block()
#                         # moves.register_callback(moves.corresponding_event(moves.settings['DEFENCE'],[0.001,0.001]))
#                     # if "WALK" in guess['transcription'].upper():
#                         # print('walk')
#                         # moves.register_callback(moves.corresponding_event(moves.settings['FORWARD'],[0.001,0.001],False))
                        
#                     """
#                     Make a way to stop continuous actions (todo) unrelease button.
#                     """
#                     if "STOP" in guess['transcription'].upper():
#                         print('Delete callbacks')
#                         # moves._callbacks = []
                    
#                     if "RS" in guess['transcription'].upper():
#                         moves.reload_shot()
#                     if "SHOT" in guess['transcription'].upper():
#                         moves.slash_shot()
#                     if "BF" in guess['transcription'].upper():
#                         moves.butterfly('FORWARD') 
#                     if "DASH" in guess['transcription'].upper():
#                         moves.dash('FORWARD') 

#                     if "ROTATE" in guess['transcription'].upper():
#                         values = take_screenshot.window_geometry()
#                         moves.rotate(values)
                        
#         except RuntimeError as e:
#             print('Changed Active Window',e)
#             # break
#     except RuntimeError as e: 
#         print('Freestyle Gunz not Open',e)
#         # break


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

    def start(self):
        print('Starting')
        while True:
            self.take_screenshot.list_processes()    
            guess = self.speech_detection.recognize_speech_from_mic()
            print(guess)
            if guess['error'] !='Unable to recognize speech':
                self.swap_window()

                """
                    (\w+)(?:/d)? Matches any group of words with optional number group
                    Make it one or more word
                    """
                    # if "SPEED" in guess['transcription'].upper():
                        # moves.speedy()
                        # moves.register_callback(moves.corresponding_event(moves.settings['USEWEAPON'],[0.001,0.001]))
                    # if "BLOCK" in guess['transcription'].upper():
                        # moves.block()
                        # moves.register_callback(moves.corresponding_event(moves.settings['DEFENCE'],[0.001,0.001]))
                    # if "WALK" in guess['transcription'].upper():
                        # print('walk')
                        # moves.register_callback(moves.corresponding_event(moves.settings['FORWARD'],[0.001,0.001],False))
                        
                """
                    Make a way to stop continuous actions (todo) unrelease button.
                """
                if "STOP" in guess['transcription'].upper():
                    print('Delete callbacks')
                if "RS" in guess['transcription'].upper():
                    self.moves.reload_shot()
                if "SHOT" in guess['transcription'].upper():
                    self.moves.slash_shot()
                if "BF" in guess['transcription'].upper():
                    self.moves.butterfly('FORWARD') 
                if "DASH" in guess['transcription'].upper():
                    self.moves.dash('FORWARD') 

                if "ROTATE" in guess['transcription'].upper():
                    values = self.take_screenshot.window_geometry()
                    self.moves.rotate(values)
            if self.take_screenshot.active_window()=="Freestyle GunZ":
                self.take_screen()

def main():
    game_manager = GameManager()
    game_manager.start()

main()