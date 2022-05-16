#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 10.11 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 10.11: Find all the reverse pairs

from os import system
from time import time
from bibth3_strings import make_words_list
from e10_09_z_bisection_search import in_bisect


def find_all_reverse_pairs(sorted_list):
    times = []
    reversed_pairs = {}
    t0 = time()
    for word in sorted_list:
        tt0 = time()
        rev_word = word[::-1]
        rev_index = in_bisect(sorted_list, rev_word)
        if rev_index is not None:
            reversed_pairs[word] = sorted_list[rev_index]
        times.append(time() - tt0)
    t = time() - t0
    for word in reversed_pairs:
        reverse = reversed_pairs[word]
        print(word, reverse)
    print("\n")
    print(t)
    print(len(reversed_pairs))
    print("\n")
    if len(times) > 0:
        time_mean = sum(times) / len(times)
        print(time_mean)
    print("\n\n")


if __name__ == "__main__":
    system('clear')
    t0 = time()
    file_path = "From the book/master/code/words.txt"
    list_of_words = make_words_list(file_path)
    print(time() - t0)
    find_all_reverse_pairs(list_of_words)
