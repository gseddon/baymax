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
    result_queue = queue.Queue()
    # audioListener = Audio(result_queue)
    Audio(result_queue).start()
    print("Im here")
    while 1:
        result = result_queue.get(True)
        print("main thread got " + result)


if __name__ == '__main__':
    # Baymax()
    main()

