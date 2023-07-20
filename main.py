import time
import moves
import takeScreenshot
import speechDetection
from pynput.keyboard import Key,Listener as KeyboardListener, Controller as KeyboardController, KeyCode
from pynput.mouse import Button,Listener as MouseListener, Controller as MouseController

moves = moves.Moves()
print(moves.settings)
take_screenshot = takeScreenshot.TakeScreenShot()

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

listener2 = MouseListener(on_click=on_click)
listener2.start()

def run():
    global take_screenshot,moves,speech_detection
    try:
        take_screenshot.list_processes()
        try:
            while True:
            
                # take_screenshot.screen_shot()
            
                guess = speech_detection.recognize_speech_from_mic()
                print(guess)
                if guess['error'] !='Unable to recognize speech':
                    if take_screenshot.active_window()!="Freestyle GunZ":
                            take_screenshot.switch_window()
                            time.sleep(3)
                            print(take_screenshot.active_window())

                    """
                    (\w+)(?:/d)? Matches any group of words with optional number group
                    Make it one or more word
                    """
                    if "RS" in guess['transcription'].upper():
                        moves.reload_shot()
                    if "SHOT" in guess['transcription'].upper():
                        moves.slash_shot()
                    if "BLOCK" in guess['transcription'].upper():
                        moves.block()
                    if "BF" in guess['transcription'].upper():
                        moves.butterfly('FORWARD') 
                    if "DASH" in guess['transcription'].upper():
                        moves.dash('FORWARD') 
                    if "ROTATE" in guess['transcription'].upper():
                        values = take_screenshot.window_geometry()
                        moves.rotate(values)

        except RuntimeError as e:
            print('Changed Active Window',e)
            # break
    except RuntimeError as e: 
        print('Freestyle Gunz not Open',e)
        # break

if __name__ == '__main__':
    run()