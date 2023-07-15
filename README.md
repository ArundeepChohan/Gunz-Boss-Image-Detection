# Gunz-Boss-Image-Detection

Installation

git clone
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

For Speech

pip3 install SpeechRecognition
sudo apt install portaudio19-dev python3-pyaudio
pip3 install sounddevice
pip3 install PyAudio

For Image Detection

pip3 install ultralytics
pip3 install torch torchvision torchaudio

For Screenshot

sudo apt-get install wmctrl

Make sure wayland is off for X11:
sudo nano /etc/gdm3/custom.conf
WaylandEnable=false

sudo apt install imagemagick-6.q16

Linux based system:

showkey -a

will display all the codes for findFile.py
