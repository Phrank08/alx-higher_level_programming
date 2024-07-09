#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary  == {}:
        return None
    elif a_dictionary is not None:
        sortScore = sorted(a_dictionary.value())
        i = sortScore[len(sortScore) - 1]

        for key, digit in a_dictionary.items():
            if digit == i:
                return key
            else:
                return None
