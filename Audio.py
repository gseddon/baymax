
import speech_recognition as sr
import difflib
import time
import queue
import threading

class Audio(threading.Thread):

    def __init__(self, result_queue, queries):
        super(Audio, self).__init__()
        self.result_queue = result_queue #type queue.Queue
        self.queries = queries
        # variables
        r = sr.Recognizer()
        m = sr.Microphone()
        print('listening...')
        with m as source:
            r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening

        # start listening in the background (note that we don't have to do this inside a `with` statement)
        self.stop_listening = r.listen_in_background(m, self.audio_callback)

        # `stop_listening` is now a function that, when called, stops background listening

        # start some loop.
        # while True:
        #     time.sleep(0.1)
        #
        # stop_listening() # calling this function requests that the background listener stop listening
    def update_queries(self, queries_dictionary):
        self.queries = list(queries_dictionary.keys())

    def assess_probability(self, probs):
        ''' Return list of position(s) of largest probability '''
        max_indices = []
        if probs:
            max_val = probs[0]
            for i,val in ((i,val) for i,val in enumerate(probs) if val >= max_val):
                if val == max_val:
                    max_indices.append(i)
                else:
                    max_val = val
                    max_indices = [i]

        return max_indices


    def test_string(self, spoken):
        confidences = [None] * len(self.queries)
        # print(queries)

        for index, phrase in enumerate(self.queries):
            confidences[index] = difflib.SequenceMatcher(None, spoken, phrase).ratio()

        max_conf = self.assess_probability(confidences)[0]

        # ensure confidences is acceptable
        if confidences[max_conf] >= 0.25:
            # return best result
            print('\nRESULT')
            print('I have matched your query to:')
            print('option ' + str(max_conf + 1) + ":")
            print(self.queries[max_conf])
            print("with " + str(confidences[max_conf]) + " confidence.")
            # return max_conf + 1
            return self.queries[max_conf]
        else:
            return False


    # this is called from the background thread
    def audio_callback(self, recognizer, audio):
        # # received audio data, now we'll recognize it using Google Speech Recognition
        spoken = None
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`

            spoken = recognizer.recognize_google(audio)
            print("Google Speech Recognition thinks you said: " + spoken)
            if spoken is not None:
                parsed_result = self.test_string(spoken)
                if parsed_result is not False:
                    self.result_queue.put(parsed_result)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


            # if self.test_string(spoken) is not False:
            #     self.result_queue.put(spoken)
            #     print("spoken was " + self.test_string(spoken))

