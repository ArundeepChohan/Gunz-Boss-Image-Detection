import speech_recognition as sr
import sounddevice
import re
from word2number import w2n
# print(sr.__version__)
# print( sr.Microphone.list_microphone_names())
class SpeechDetection:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source,duration=1)
    def recognize_speech_from_mic(self):
        """Transcribe speech from recorded from `microphone`.

        Returns a dictionary with three keys:
        "success": a boolean indicating whether or not the API request was
                successful
        "error":   `None` if no error occured, otherwise a string containing
                an error message if the API could not be reached or
                speech was unrecognizable
        "transcription": `None` if speech could not be transcribed,
                otherwise a string containing the transcribed text
        """
        if not isinstance(self.recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(self.microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")
        
        with self.microphone as source:
            audio = self.recognizer.listen(source,phrase_time_limit=3)
            
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        try:
            response["transcription"] = self.recognizer.recognize_google(audio, language= 'en-US').upper()
            parts = re.findall(r'\D+|\d+', response["transcription"])
            print("Parts",parts)
            words = ' '.join(parts)
            print('Words: ',words)
            o = []
            for word in words.split(' '):
                try:
                    o += [str(w2n.word_to_num(word))]
                except ValueError:
                    o += [word]
            print('Before join',o)
            response["transcription"] = ' '.join(o)

        except sr.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            response["error"] = "Unable to recognize speech"

        return response

# speech_detection=SpeechDetection()
# while True:
#     guess = speech_detection.recognize_speech_from_mic()
#     print(guess)
