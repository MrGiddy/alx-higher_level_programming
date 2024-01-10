#!/usr/bin/python3

def best_score(a_dictionary: dict) -> str:
    if (a_dictionary is None):
        return None

    best_score_key = max(a_dictionary, key=a_dictionary.get)
    return best_score_key
