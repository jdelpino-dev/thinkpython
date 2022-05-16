#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Library with Downey's functions / For "Think Python"
# Learning and experimentation with the book "Think Python" by Allen Downey
# Code by Allen Downey

from __future__ import print_function, division


def read_dictionary(filename):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d
