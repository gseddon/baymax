# Requires PyAudio and PySpeech.

import speech_recognition as sr
import difflib
from Audio import Audio
import queue
from pygame import mixer
import pygame
from RPi import GPIO
from time import sleep

class Baymax():
    queries = None

    def __init__(self):
        self.queries = {"start": self.start,
                   "stop": self.stop,
                   "hello": self.hello,
                   "inflate": self.inflate,
                   "how are you": self.how_are_you}
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        result_queue = queue.Queue()
        self.recogniser = Audio(result_queue, list(self.queries.keys()))
        self.recogniser.start()
        pygame.init()
        self.hello()
        while 1:
            result = result_queue.get(True)
            self.queries[result]()

    def hello(self):
        self.toggle_pin_play_sound_duration(pin = 11, sound = "hello_baymax.mp3", duration=5)

    def start(self):
        pass

    def stop(self):
        pass

    def inflate(self):
        print("inflate")
        self.toggle_pin_play_sound_duration(pin= 11, sound = "openingSound.mp3", duration=5)
        self.queries = {"start": self.start,
                   "deflate": self.deflate,
                   "can you scan me" : self.scan}
        self.recogniser.update_queries(self.queries)

    def deflate(self):
        print("deflate")

    def scan(self):
        self.toggle_pin_play_sound_duration(11, "ratePain.mp3", duration=4)
        self.queries = {"1": lambda: self.rate_pain(1),
                   "2": lambda: self.rate_pain(2),
                   "3": lambda: self.rate_pain(3),
                   "4": lambda: self.rate_pain(4),
                   "5": lambda: self.rate_pain(5),
                   "6": lambda: self.rate_pain(6),
                   "7": lambda: self.rate_pain(7),
                   "8": lambda: self.rate_pain(8),
                   "9": lambda: self.rate_pain(9)}
        self.recogniser.update_queries(self.queries)

    def rate_pain(self, rating):
        print("rate_pain")
        print(rating)



    def how_are_you(self):
        pass

    def toggle_pin_play_sound_duration(self, pin, sound, duration):
        mixer.music.load("assets/"+sound)
        mixer.music.play()
        GPIO.output(pin, GPIO.HIGH)
        sleep(duration)
        mixer.music.stop()
        GPIO.output(pin, GPIO.LOW)

if __name__ == '__main__':
    Baymax()


