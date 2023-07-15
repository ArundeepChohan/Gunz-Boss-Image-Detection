import time
import moves
import takeScreenshot
from pynput.keyboard import Key,Listener as KeyboardListener, Controller as KeyboardController, KeyCode
from pynput.mouse import Button,Listener as MouseListener, Controller as MouseController

moves = moves.Moves()
print(moves.settings)
takeScreenshot = takeScreenshot.TakeScreenShot()

keyboard = KeyboardController()
mouse = MouseController()

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

# def on_click(x, y, button, pressed):
#     if pressed:
#         print ('Mouse clicked {2}'.format(x, y, button))


# with MouseListener(on_click=on_click) as listener:
#     listener.join()


def run():
    try:
        takeScreenshot.list_processes()
        try:
            if takeScreenshot.active_window()!="Freestyle GunZ":
                takeScreenshot.switch_window()
                time.sleep(5)
                print(takeScreenshot.active_window())
            moves.butterfly('FORWARD') 
            # eflip('w')
            # reload_shot()
            # butterfly('w')
            # slash_shot('w') 
            # gear_tap()
            # speedy()
            # block()
            # takeScreenshot.screen_shot()
        except RuntimeError as e:
            print('Changed Active Window',e)
            # break
    except RuntimeError as e: 
        print('Freestyle Gunz not Open',e)
        # break

if __name__ == '__main__':
    run()