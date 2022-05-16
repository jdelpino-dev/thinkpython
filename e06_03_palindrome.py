#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 6.3 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 6.3: Palindrome

from os import system
from bibth3_strings import make_plain


def first_letter(st):
    '''Doesn't work with the empty string.
    '''
    return st[0]


def middle_str(st):
    return st[1:-1]


def last_letter(st):
    '''Doesn't work with the empty string.
    '''
    return st[-1]


def is_palindrome(st):
    '''Recursively identifies palindrome strings words.
    The empty string '' is considered a palindrome, as well as any string
    with one character. This function doesn't work yet with every sentence that
    inlcudes punctuation marks'''
    len_st = len(st)
    # The first "if" –including its branches– is a guardian for
    # the special case of empty strings, which doesn't need any recursion,
    # and the base case of one-character strings, which ends the recursion.
    if len_st == 1:
        return True
    elif len_st == 0:
        return True
    # This second "if" make central logic of the function. It either stops
    # the recursion when it found that the word is not a palindrome or
    # keep going with the recursion if there is still a chance.
    if first_letter(st) != last_letter(st):
        return False
    return is_palindrome(middle_str(st))


if __name__ == "__main__":
    system('clear')
    t_words = []
    words = ["casa", "noon", "anagrama", "coon", "Anna", "Civic", "madam",
             "refer", "Stats", "radar", "rotor", "solos", "moco", "coco",
             "", '', "S", "e", "Go hang a salami, I'm a lasagna hog"]
    for word in words:
        t_word = make_plain(word)
        t_words.append(t_word)
    answers = map(is_palindrome, t_words)
    labeled_answers = list(zip(words, answers))
    print(labeled_answers, "\n\n")
