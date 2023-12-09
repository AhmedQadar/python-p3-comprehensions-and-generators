#!/usr/bin/env python3

def return_evens(num_list):
    if num_list:
        return [num for num in num_list if num % 2 == 0]
    else:
        return []
    pass

def make_exclamation(sentence_list):
    if sentence_list:
        return [sentence + '!' for sentence in sentence_list]
    else:
        return []
    pass