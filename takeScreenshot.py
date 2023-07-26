import subprocess

class TakeScreenShot():
    def __init__(self):
        self.window = None

    def list_processes(self):
        try:
            results = subprocess.check_output("wmctrl -lp | awk '/Freestyle GunZ/ { print $1 }'",encoding="UTF-8",shell=True,stderr=subprocess.STDOUT)
            result = results.strip()
            print(result)
            self.window = result
        except subprocess.CalledProcessError as e:
            self.window = None
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        
    def active_window(self):
        try:
            active_window = subprocess.check_output("xdotool getwindowfocus getwindowname",encoding="UTF-8",shell=True,stderr=subprocess.STDOUT)
            return active_window.strip()
        except subprocess.CalledProcessError as e:
            print("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        
    def switch_window(self):
        try:
            if self.window!=None:
                print('window id',self.window)
                subprocess.check_output("wmctrl -iR "+self.window,shell=True,stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        
    def screen_shot(self):
        try:
            command ="xwd -id "+self.window+ " | convert xwd:- image.png"
            #command = "xwd -root | convert xwd:- image.png"
            
            if self.window!=None:
                print(command)
                subprocess.check_output(command,shell=True,stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        
    def window_geometry(self):
        try:
            active_window = subprocess.check_output("xdotool getwindowfocus getwindowgeometry",encoding="UTF-8",shell=True,stderr=subprocess.STDOUT)
            return active_window.strip()
        except subprocess.CalledProcessError as e:
            print("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        
# screen = TakeScreenShot()
# screen.list_processes()
# screen.switch_window()
# screen.screen_shot()