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
                   "ouch": self.inflate,
                   "how are you": self.how_are_you}
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
        result_queue = queue.Queue()
        self.recogniser = Audio(result_queue, list(self.queries.keys()))
        self.recogniser.start()
        pygame.init()
        self.play_sound_duration('care.mp3',2)
        sleep(1)
        self.play_sound_duration('hello_baymax.mp3',2)
        sleep(1)
        while 1:
            result = result_queue.get(True)
            self.queries[result]()

    def hello(self):
        print("hello")
        self.toggle_pin_play_sound_duration(pin = 11, sound = "hello_baymax.mp3", duration=5)
        self.rate_pain()


    def start(self):
        pass


    def stop(self):
        pass

    def inflate(self):
        print("inflate")
        self.toggle_pin_play_sound_duration(pin= 11, sound = "openingSound.mp3", duration=5)
        self.play_sound_duration(sound = "hello_baymax.mp3", duration=5)
        # self.queries = {"start": self.start,
        #            "deflate": self.deflate,
        #            "can you scan me" : self.scan}
        # self.recogniser.update_queries(self.queries)
        self.rate_pain()

    def deflate(self):
        print("deflating...")
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
        sleep(180)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
        # sleep(180)
        print("G00d by3 :)")
        quit()

    def rate_pain(self):
        print("rate pain")
        self.toggle_pin_play_sound_duration(11, "ratePain.mp3", duration=4)
        self.queries = {"1": lambda: self.respond_to_rating(1),
                   "2": lambda: self.respond_to_rating(2),
                   "3": lambda: self.respond_to_rating(3),
                   "4": lambda: self.respond_to_rating(4),
                   "5": lambda: self.respond_to_rating(5),
                   "6": lambda: self.respond_to_rating(6),
                   "7": lambda: self.respond_to_rating(7),
                   "8": lambda: self.respond_to_rating(8),
                   "9": lambda: self.respond_to_rating(9)}
        self.recogniser.update_queries(self.queries)

    def respond_to_rating(self, rating):
        print("rating pain")
        if (rating <= 5):
            pass
        else:
            self.scan()
        print(rating)

    def scan(self):
        print("scanning...")
        self.play_sound_duration("scanning.mp3", 2)
        sleep(2)
        self.play_sound_duration("scanComplete.mp3", 1)
        sleep(1)
        self.play_sound_duration('Puberty.mp3', 4)
        sleep(1)
        self.play_sound_duration('care.mp3',3)
        sleep(4)
        self.queries = {
            "yes": self.deflate,
            "no": self.rate_pain
        }
        self.recogniser.update_queries(self.queries)

    def how_are_you(self):
        print("How are you?")

    def play_sound_duration(self, sound, duration):
        mixer.music.load("assets/"+sound)
        mixer.music.play()
        sleep(duration)
        mixer.music.stop()

    def toggle_pin_play_sound_duration(self, pin, sound, duration):
        mixer.music.load("assets/"+sound)
        mixer.music.play()
        GPIO.output(pin, GPIO.HIGH)
        sleep(duration)
        mixer.music.stop()


if __name__ == '__main__':
    Baymax()


