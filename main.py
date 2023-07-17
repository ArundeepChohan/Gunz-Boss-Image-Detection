import time
import moves
import takeScreenshot
import speechDetection
from pynput.keyboard import Key,Listener as KeyboardListener, Controller as KeyboardController, KeyCode
from pynput.mouse import Button,Listener as MouseListener, Controller as MouseController

moves = moves.Moves()
print(moves.settings)
takeScreenshot = takeScreenshot.TakeScreenShot()

keyboard = KeyboardController()
mouse = MouseController()

speech_detection = speechDetection.SpeechDetection()

# Some helper functions to find button presses
def on_press(key):
    print(key.__dict__)

# Unblock the program if presses fail
def on_release(key):
    if hasattr(key, 'vk'):
        print('You entered a number from the numpad: ', key.char, key.vk)
        print(key.__dict__)

    else:
        print(key.__dict__)       
        
listener = KeyboardListener(on_press=on_press, on_release=on_release) 
listener.start()

def on_click(x, y, button, pressed):
    if pressed:
        print ('Mouse clicked {2}'.format(x, y, button))

with MouseListener(on_click=on_click) as listener:
    listener.join()

def run():
    global takeScreenshot,moves,speech_detection
    try:
        takeScreenshot.list_processes()
        try:
            while True:
                
                # moves.butterfly('FORWARD') 
                # moves.eflip('FORWARD')
                # moves.reload_shot()
                # moves.butterfly('FORWARD')
                # moves.slash_shot('FORWARD') 
                # moves.gear_tap()
                # moves.speedy()
                # moves.block()
                # takeScreenshot.screen_shot()
            
                guess = speech_detection.recognize_speech_from_mic()
                print(guess)
                if guess['error'] !='Unable to recognize speech':
                    if takeScreenshot.active_window()!="Freestyle GunZ":
                            takeScreenshot.switch_window()
                            time.sleep(3)
                            print(takeScreenshot.active_window())
                    if "FORWARD" in guess['transcription'].upper():
                        moves.butterfly('FORWARD') 

        except RuntimeError as e:
            print('Changed Active Window',e)
            # break
    except RuntimeError as e: 
        print('Freestyle Gunz not Open',e)
        # break

if __name__ == '__main__':
    run()