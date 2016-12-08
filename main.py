# Requires PyAudio and PySpeech.

import speech_recognition as sr
import difflib
from Audio import Audio
import queue
from pygame import mixer
import pygame
from RPi import GPIO
from time import sleep

recogniser = None
queries = None

def main():
    queries = {"start": start,
               "stop": stop,
               "hello": hello,
               "inflate": inflate,
               "how are you": how_are_you}
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    result_queue = queue.Queue()
    recogniser = Audio(result_queue, list(queries.keys())).start()
    pygame.init()
    hello()
    while 1:
        result = result_queue.get(True)
        print("main thread got " + result)
        queries[result]()

def hello():
    toggle_pin_play_sound_duration(pin = 11, sound = "hello_baymax.mp3", duration=5)

def start():

    pass

def stop():
    pass

def inflate():
    print("inflate")
    toggle_pin_play_sound_duration(pin= 11, sound = "openingSound.mp3", duration=5)
    queries = {"start": start,
               "deflate": deflate,
               "can you scan me" : scan}
    recogniser.queries = queries.keys()

def deflate():
    print("deflate")

def scan():
    toggle_pin_play_sound_duration(11, "ratePain.mp3", duration=4)
    queries = {"1", 1}


def how_are_you():
    pass

def toggle_pin_play_sound_duration(pin, sound, duration):
    mixer.music.load("assets/"+sound)
    mixer.music.play()
    GPIO.output(pin, GPIO.HIGH)
    sleep(duration)
    mixer.music.stop()
    GPIO.output(pin, GPIO.LOW)

if __name__ == '__main__':
    # Baymax()
    main()

