import subprocess
import os 
import time

PROCNAME = "Freestyle GunZ"

from pynput.keyboard import Key,Listener as KeyboardListener, Controller as KeyboardController, KeyCode
from pynput.mouse import Button,Listener as MouseListener, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()

def dash(dir):
    # keyboard.press(dir)
    # time.sleep(0.05)
    # keyboard.release(dir)
    # time.sleep(0.05)
    # keyboard.press(dir)
    # time.sleep(0.05)
    # keyboard.release(dir)
    keyboard.type(dir)
    keyboard.type(dir)

def jump():
    keyboard.press(Key.space)
    keyboard.release(Key.space)

def reload_shot():
    for i in range(5):
        keyboard.type('2')
        time.sleep(0.10)
        mouse.press(Button.left)
        time.sleep(0.20)
        mouse.release(Button.left)
        time.sleep(0.10)
        mouse.press(Button.button9)
        time.sleep(0.20)
        mouse.release(Button.button9)

        keyboard.type('3')
        time.sleep(0.10)
        mouse.press(Button.left)
        time.sleep(0.20)
        mouse.release(Button.left)
        time.sleep(0.10)
        mouse.press(Button.button9)
        time.sleep(0.10)
        mouse.release(Button.button9)

def butterfly(dir):
    jump()
    time.sleep(0.05)
    dash(dir)
    mouse.press(Button.left)
    time.sleep(0.01)
    mouse.release(Button.left)
    time.sleep(0.01)
    mouse.press(Button.right)
    time.sleep(0.01)
    mouse.release(Button.right)
    time.sleep(0.01)

#Jump, Dash, Slash, Swap weapon, Shoot, then back to sword(optional)
def slash_shot(dir):
    keyboard.type('1')

    jump()
    time.sleep(0.05)
    dash(dir)

    mouse.press(Button.left)
    time.sleep(0.05)
    keyboard.type('e')
    time.sleep(0.05)
    mouse.press(Button.left)
    mouse.release(Button.left)

    keyboard.type('1')

# slash, switch, shoot+reload, sword
def gear_tap(dir):
    keyboard.type('1')

    jump()
    time.sleep(0.05)

    mouse.press(Button.left)
    # time.sleep(0.05)
    keyboard.type('e')
    time.sleep(0.30)
    mouse.release(Button.left)
    time.sleep(0.05)
    keyboard.type('1')
    time.sleep(0.1)
    
    dash(dir)

def speedy():
    for i in range(10000):
        mouse.press(Button.left)
        time.sleep(0.001)
        mouse.release(Button.left)
        time.sleep(0.001)

def block():
    for i in range(10000):
        mouse.press(Button.right)
        time.sleep(0.001)
        mouse.release(Button.right)
        time.sleep(0.001)

# I think it's 1 second jump length
def jump_time():
    for i in range(10):
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        time.sleep(1)

# dash with alt fire (todo)
def eflip(dir):
    
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

def move_to_cordinates():
    for i in range(100):
        keyboard.press('w')
        time.sleep(0.05)
        keyboard.release('w')
        time.sleep(0.05)
        keyboard.press('w')
        time.sleep(0.15)
        keyboard.release('w')

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

try:
    results = subprocess.check_output("wmctrl -lp | awk '/Freestyle GunZ/ { print $1 }'",shell=True,stderr=subprocess.STDOUT)
    result = results.decode("ascii")
    print(result)
    switch_to_window = subprocess.check_output("wmctrl -iR "+result,shell=True,stderr=subprocess.STDOUT)
    time.sleep(5)
    # move_to_cordinates()
    # reload_shot()
    butterfly('w')
    # slash_shot('w')
    # gear_tap()
    # speedy()
    # block()
    # eflip('w')
    #"xwd -id"+result+ "| convert xwd:- image.png"
    command = "xwd -root | convert xwd:- image.png"
    screenshot_window = subprocess.check_output(command,shell=True,stderr=subprocess.STDOUT)

except subprocess.CalledProcessError as e:
    raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
