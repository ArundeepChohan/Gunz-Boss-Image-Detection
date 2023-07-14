import os
import sys
from pathlib import Path
from bs4 import BeautifulSoup as bs
from pynput.keyboard import Key,Listener as KeyboardListener, Controller as KeyboardController, KeyCode
from pynput.mouse import Button,Listener as MouseListener, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()

class FindFile():
    def __init__(self):
        """
        Corresponding key/mouse to 
        
        NUMPAD 
        3 	    51 0063 0x33
        0 	    48 0060 0x30
        . 	    46 0056 0x2e
        ENTER   13 0015 0x0d
        2 	    50 0062 0x32
        1 	    49 0061 0x31
        4 	    52 0064 0x34
        5 	    53 0065 0x35
        6 	    54 0066 0x36
        + 	    43 0053 0x2b
        9 	    57 0071 0x39
        8 	    56 0070 0x38
        7 	    55 0067 0x37
        / 	    47 0057 0x2f
        * 	    42 0052 0x2a
        - 	    45 0055 0x2d

        """
        self.moves_list={
        '1' : Key.esc,
        '2' : '1',
        '3' : '2',
        '4' : '3',
        '5' : '4',
        '6' : '5',
        '7' : '6',
        '8' : '7',
        '9' : '8',
        '10': '9',
        '11': '0',
        '12': '-',
        '13': '=',
        '14': Key.backspace,
        '15': Key.tab,
        '16': 'q',
        '17': 'w',
        '18': 'e',                           
        '19': 'r',                              
        '20': 't',                                
        '21': 'y',                                
        '22': 'u',                                
        '23': 'i',                                
        '24': 'o',                                
        '25': 'p',
        '26': '[',                              
        '27': ']',                               
        '28': Key.enter,                  
        '29': Key.ctrl_l,                    
        '30': 'a',                                
        '31': 's',                                
        '32': 'd',                                
        '33': 'f',                                
        '34': 'g',                                
        '35': 'h',                                
        '36': 'j',                                
        '37': 'k',                                
        '38': 'l',                                
        '39': ';',                             
        '40': "'",                             
        '41': '`',                              
        '42': Key.shift_l,
        '44': 'z',
        '45': 'x',
        '46': 'c',
        '47': 'v',
        '48': 'b',
        '49': 'n',
        '50': 'm',
        '51': ',', 
        '52': '.', 
        '53': '/', 
        '54': Key.shift_r,
        '55': 0x2A,
        '56': Key.alt_l,
        '57': Key.space,
        '58': Key.caps_lock,
        '59': Key.f1,
        '60': Key.f2,
        '61': Key.f3,
        '62': Key.f4,
        '63': Key.f5,
        '64': Key.f6,
        '65': Key.f7,
        '66': Key.f8,
        '67': Key.f9,
        '68': Key.f10,
        '69': Key.num_lock,
        '70': Key.scroll_lock,
        '71': Key.home,
        '72': Key.up,
        '73': Key.page_up,
        '74': 0x2d,            
        '75': Key.left,
        '76': 0x35,            
        '77': Key.right,     
        '78': 0x2b,            
        '79': Key.end,        
        '80': Key.down,     
        '81': Key.page_down,       
        '82': Key.insert,    
        '83': Key.delete,

        '87': Key.f11,
        '88': Key.f12,

        '256': Button.scroll_up,
        '257': Button.scroll_down,
        '258': Button.left,                
        '259': Button.right,
        '260': Button.middle,
        '261': Button.button10,
        '262': Button.button9,

        }
       
        self.default_moves_setting = {
        'USEWEAPON':Button.left,
        'USEWEAPON2':Button.right,
        'PREVOUSWEAPON':-1,
        'NEXTWEAPON': -1,
        'FORWARD':'w',
        'BACK':'s',
        'LEFT':'a',
        'RIGHT':'d',
        'MELEEWEAPON':'1',
        'PRIMARYWEAPON':'2',
        'SECONDARYWEAPON':'3',
        'ITEM1':'4',
        'ITEM2':'5',
        'COMMUNITYITEM1':-1,
        'COMMUNITYITEM2':-1,
        'RELOAD':'r',
        'JUMP': Key.space,
        'SCORE':Key.tab,
        'MENU':-1,
        'TAUNT':-1,
        'BOW':-1,
        'WAVE':-1,
        'LAUGH':-1,
        'CRY':-1,
        'DANCE':-1,
        'SCREENSHOT': Key.f12,
        'RECORD': Key.f11,
        'MOVINGPICTURE':-1,
        'DEFENCE': Key.shift,
        'TOGGLECHAT':-1,
        'MOUSESENSITIVITYDEC':'[',
        'MOUSESENSITIVITYINC':']',
        'PREVIOUSSONG':-1,
        'NEXTSONG':-1,
        'TEAMCHAT':-1,
        'PINGSYSTEM':Key.alt,
        }
    
    def find(self,name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
            
    def switch_to_root(self):
        print('Root folder of the os system: ',os.path.abspath(os.sep))
        os.chdir(os.path.abspath(os.sep))
        
    """
        Use default settings in case config.xml is missing. 
        Furthermore find a way to transcript the values gotten from the file into mouse/keyboard values
        <enum 'Key'> <class 'str'> <enum 'Button'>
    """
    def current_settings(self):
        self.switch_to_root()
        cwd = os.getcwd()
    
        config_path = None
        moves_setting = self.default_moves_setting.copy()
        paths = Path(cwd).rglob('*Freestyle GunZ')
        
        for path in paths:
            #print(path)
            os.chdir(path)
            cwd = os.getcwd()
            try:
                config_path = self.find('config.xml',os.getcwd())
                if config_path != None:
                    print(config_path)
                    with open(config_path, "r") as file:
                        soup = bs(file.read(),'xml')
                        for key in moves_setting:
                            move_code = soup.find(key).contents[0]
                            print(key,move_code)
                            if move_code !="-1":
                                moves_setting[key] = self.moves_list[move_code]
                            else:
                                moves_setting[key] = -1
                    break
                    
            # Caching the exception   
            except:
                print("Something wrong with specified\
                    directory. Exception- ", sys.exc_info())
                pass

        return moves_setting
    
settings = FindFile()
print(settings.current_settings())                  
print(type(Button.left),type(Key.enter),type('w'),type(0x2A))
