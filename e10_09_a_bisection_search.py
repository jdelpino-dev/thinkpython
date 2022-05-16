#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 10.9 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 10.9: Bisection Search

''' Mine in_bisect function is very complex but is way more efficient
than Downey's. On average mine takes 0.000038 seconds to find a word, while
Downey's take 0.0032 seconds. Than is, my function is 99 % faster.

One diference is that I don't use recursion nor list_copies. Thise means
that my code is more ram efficient. Other difference, although,
I think it don't increase to much the performance, is that my funciton
does extra checks between the item and the other items that it has
at hand during every loop.

What I need to do is to make it more readable and innecessarily complex.
Maybe I can do it making it recursive... I guess that the key is avoid
making list copies. Other thing I can do is to manage some of the
many variables using a small data_structure and a function that
updates their values inside that structure. ¡It could be a diccionary!
'''

from os import system
from time import time
from bibth3_strings import make_words_list
from e10_01_07_lists import half_cut_point
# from e10_1_7_lists import random_elements


def in_bisect_it(sorted_list, item):
    '''Does a bisection search of an item on a sorted list.
    If the item is on the list it returns the index.
    If not, it returns None
    '''
    lenght = len(sorted_list)
    cut_point = lenght
    if lenght == 0:
        return None
    elif lenght >= 1:
        if item == sorted_list[0]:
            return 0
        elif item == sorted_list[lenght - 1]:
            return lenght - 1
        elif item > sorted_list[lenght - 1]:
            return None
    cut_point = half_cut_point(lenght)
    relative_index = 0
    while lenght >= 0:
        cut_item = sorted_list[cut_point]
        cut_item2 = sorted_list[cut_point + 1]
        if item == cut_item:
            return cut_point
        elif item == cut_item2:
            return cut_point + 1
        last_item = sorted_list[(lenght - 1) + relative_index]
        if cut_item < item < cut_item2 or item > last_item:
            return None
        if lenght % 2 == 0:
            sub_lenght1 = cut_point + 1 - relative_index
            sub_lenght2 = sub_lenght1
        else:
            sub_lenght1 = cut_point + 1 - relative_index
            sub_lenght2 = sub_lenght1 + 1
        if item > cut_item:
            relative_index = relative_index + sub_lenght1
            cut_point = half_cut_point(sub_lenght2) + relative_index
            lenght = sub_lenght2
        else:
            cut_point = half_cut_point(sub_lenght1) + relative_index
            lenght = sub_lenght1
    return None


if __name__ == "__main__":
    system('clear')
    file_path = "/From the book/master/code/words.txt"
    list_of_words = make_words_list(file_path)
    # word = "aa"
    # word = 17
    # list_of_words = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    # print(list_of_words)
    # search_result = in_bisect(list_of_words, word)
    # print(search_result)
    # if search_result != None:
    # print(list_of_words[search_result])
    # else:
    # print(f"{word} is not in the list")
    # words = ['aa', 'alien', 'allen', 'zymurgy']
    # words = ['alien']
    # words = random_elements(list_of_words, 10000)
    # list_of_words = list(range(1, 28450))
    words = list_of_words
    times = []
    for word in words:
        t0 = time()
        search_result = in_bisect_it(list_of_words, word)
        t = time() - t0
        times.append(t)
        print(t)
        if search_result is not None:
            print(word, 'is in list and its index is', search_result)
            print(list_of_words[search_result])
        else:
            print(f"{word} is not in the list")
        print("\n")
    print("\n")
    time_mean = sum(times) / len(times)
    print(time_mean)
    print("\n")
