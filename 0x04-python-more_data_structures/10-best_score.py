#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new_dictionary = sorted(a_dictionary.items(),
                                key=lambda x: x[1],
                                reverse=True)
        score = next(iter(new_dictionary))
        return (score[0])
    else:
        return None
