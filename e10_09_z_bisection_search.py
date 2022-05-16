#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 10.9 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 10.9: Bisection Search, final version

from os import system
from time import time
from bibth3_strings import make_words_list
# from bibth3_strings import make_words_dicc


def in_bisect(sorted_list, item):
    '''Does the iterative bisection search of an item on a sorted list
    of strings or integers. If the item is on the list it returns the index.
    If not, it returns None.

    sorted_list: the list must be sorted
    item: str or integer
    '''
    low = 0
    high = len(sorted_list) - 1
    while low < high:
        middle = (high + low) // 2
        middle_item = sorted_list[middle]
        if middle_item == item:
            return middle
        if item > middle_item:
            low = middle + 1
        else:
            high = middle
    if sorted_list[low] == item:
        return low
    else:
        return None


if __name__ == "__main__":
    system('clear')
    file_path = "From the book/master/code/words.txt"
    list_of_words = make_words_list(file_path)
    # words = ["zeugma", "coco", "xylan", "rumblers", "bytalks",
    #         "funest", "allodial", "aa", "aah", "aasvogel",
    #         "zymoses", "zymosis", "zymotic", "zymurgies",
    #         "zymurgy"]
    words = list_of_words
    # dicc_of_words = make_words_dicc(file_path)
    # dicc_of_words = {}
    # for i in range(10000001):
    #    dicc_of_words[i] = i
    # words = dicc_of_words
    times = []
    results = []
    for i in range(10):
        for word in words:
            t0 = time()
            search_result = in_bisect(list_of_words, word)
            # if word in dicc_of_words:
            #    search_result = dicc_of_words[word]
            t = time() - t0
            times.append(t)
            results. append(search_result)
    if len(times) > 0:
        time_mean = sum(times) / len(times)
        print(time_mean)
    print("\n")
    print(results.count(None))
    print(len(results))
    print("\n")
