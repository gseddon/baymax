# Requires PyAudio and PySpeech.

import speech_recognition as sr
import difflib
from Audio import Audio
import queue


# class Baymax():
#
#     def __init__(self):
#         pass
#
#     audioListener = Audio()
def main():
    queries = [
        "start",
        "stop",
        "inflate",
        "how are you"
    ] # these are the strings that we want the voice recognition to match against
    queries = {"start": start,
               "stop": stop,
               "inflate": inflate,
               "how are you": how_are_you}
    print(queries)
    result_queue = queue.Queue()
    # audioListener = Audio(result_queue)
    Audio(result_queue, list(queries.keys())).start()
    while 1:
        result = result_queue.get(True)
        print("main thread got " + result)
        queries[result]()

def start():
    print("I'm going to start inflating")
    pass

def stop():
    pass

def inflate():
    pass

def how_are_you():
    pass


if __name__ == '__main__':
    # Baymax()
    main()

