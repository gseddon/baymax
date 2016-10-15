# Requires PyAudio and PySpeech.

import speech_recognition as sr
import difflib

class Baymax():
    # Record Audio
    r = sr.Recognizer()
    result = self.getAudio()

    def getAudio(this):
        """

        :return:
        :rtype string
        """
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            recognitionResult = r.recognize_google(audio)
            print("You said: " + recognitionResult)
            return recognitionResult
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ""


if __name__ == '__main__':
    Baymax()

