#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 13.5 and 13.7 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 13.5 and 13.7: Book Works II and IV: Frequency Proportional Random
#                         Choose from a Book's Histogram

from os import system
from random import randint, choice
from bibth3_dicts import make_simple_dict
from e13_01_04_book_works1 import make_book_hist


def make_proplist(hist: dict) -> list:
    prop_list = []
    for key in hist:
        to_add = [key] * hist[key]
        prop_list.extend(to_add)
    return prop_list


def make_proplist2(hist: dict) -> list:
    prop_list = []
    for key in hist:
        to_add = [key] * hist[key]
        lenght = len(prop_list)
        if lenght == 0:
            prop_list.extend(to_add)
        else:
            for item in to_add:
                prop_list.insert(randint(0, lenght-1), item)
    return prop_list


def choose_from_hist(hist: dict, keys_list: list):
    """Takes a histogram dict and a list of its keys that include them
    as many times as their frequencies in the dictionary. The function
    returns a random value from the histogram, chosen frmo the list with
    probability in proportion to frequency. The type of value returned
    depends of the kinds of values stored on the dict.
    """
    lenght = len(keys_list)
    picked_key = keys_list[randint(0, lenght-1)]
    return picked_key


def print_randomprop_keys(the_dict: dict, n: int,
                          prop_list: list, message: str):
    print(f"The {n} random word(s) from {message} are:\n")
    for i in range(1, n+1):
        random_key = choose_from_hist(the_dict, prop_list)
        freq = the_dict[random_key]
        tab = " " * (25-len(random_key))
        print(f"[{i}] {random_key} –>{tab}-> "
              f"FREQ = {freq}")
    print("\n")


def print_randomprop_keys2(the_dict: dict, n: int, message: str):
    prop_list = make_proplist(the_dict)
    print(f"The {n} random word(s) from {message} are:\n")
    for i in range(1, n+1):
        random_key = choose_from_hist(the_dict, prop_list)
        freq = the_dict[random_key]
        tab = " " * (25-len(random_key))
        print(f"[{i}] {random_key} –>{tab}-> "
              f"FREQ = {freq}")
    print("\n")


def print_random_keys(the_dict: dict, n: int, message: str):
    print(f"The {n} random word(s) from {message} are:\n")
    for i in range(1, n+1):
        random_key = choice(the_dict)
        print(f"[{i}] {random_key}")
    print("\n")


if __name__ == "__main__":

    gulliver_path = "files/gulliver_s_travels.txt"
    mobydick_path = "files/moby_dick_or_the_whale.txt"
    english_path = "files/words_new.txt"

    gulliver_hist = make_book_hist(gulliver_path)
    mobydick_hist = make_book_hist(mobydick_path)
    english_dict = make_simple_dict(english_path)

    prop_gulli = make_proplist(gulliver_hist)
    prop_moby = make_proplist(mobydick_hist)
    keys_english = list(english_dict.keys())

    system('clear')
    print_randomprop_keys(gulliver_hist, 100,
                          prop_gulli, "the Gulliver's histogram")
    print_randomprop_keys(mobydick_hist, 100,
                          prop_moby, "the Mobidick's histogram")
    print_random_keys(keys_english, 100, "the English dict")
    print("\n")
