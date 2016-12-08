import difflib
queries = [
    "start", 
"deflate",
"can you scan me"]

def assessProbability( probs):
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

def test_string(string):
    spoken = string
    confidences = [None] * len(queries)
    # print(queries)

    for index, phrase in enumerate(queries):
        confidences[index] = difflib.SequenceMatcher(None, spoken, phrase).ratio()

    max_conf = assessProbability(confidences)[0]

    # print(confidences)
    # print(max_conf)
    # ensure confidences is acceptable
    if confidences[max_conf] >= 0.25:
        # return best result
        print('\nRESULT')
        print('I have matched your query to:')
        print('option ' + str(max_conf + 1) + ":")
        print(queries[max_conf])
        print("with " + str(confidences[max_conf]) + " confidence.")
        # return max_conf + 1
        return queries[max_conf]
    else:
        return False

test_string("scan me")