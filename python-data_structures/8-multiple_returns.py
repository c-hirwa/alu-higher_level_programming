#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    leng = len(sentence)
    firs = sentence[0]
    return (leng, firs)
