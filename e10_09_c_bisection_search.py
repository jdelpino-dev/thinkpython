#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 10.9 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 10.9: Reduced Bisection Search (recursive, reducing)

''' This is an improved bisection search that reduces the succesive
sub_lists by one element in one of its extremes. It increases considerably
the performance by savind 4 recursions per search.
'''

from os import system
from time import time
from bibth3_strings import make_words_list
from e10_01_07_lists import half_cut_point


def bisect_recursion(sorted_list, lenght, item, pos0, posf):
    '''Does the recursive bisection search for in_bisect of
    an item in a sorted list of strings or integers, and its
    succesive sub-list. This functions doesn't make sliced
    copies of the list, but keep track of the sublist using
    pos0 and posf.

    Arguments:
        item: str or integer
        pos0: index of the first element of the sublist.
    '''
    # This guardian solves all the bases cases of the recursion:
    sub_lenght = posf - pos0 + 1
    if sub_lenght == 0:
        return None
    if (item > sorted_list[posf]) or (item < sorted_list[pos0]):
        return None
    if item == sorted_list[pos0]:
        return pos0
    if item == sorted_list[posf]:
        return posf
    elif sub_lenght == 1 or sub_lenght == 2:
        return None
    # Calculates the new values and continues the recursive bisection search:
    cut_point = half_cut_point(sub_lenght) + pos0
    cut_point2 = cut_point + 1
    cut_item = sorted_list[cut_point]
    # Decides which brach of the bisection search to follow:
    if item > cut_item:
        return bisect_recursion(sorted_list, lenght, item,
                                pos0=cut_point2, posf=posf-1)
    else:
        return bisect_recursion(sorted_list, lenght, item,
                                pos0=pos0+1, posf=cut_point)


def in_bisect(sorted_list, item):
    '''Does a bisection search of an item on a sorted list
    of strings or integers.

    If the item is on the list it returns the index.
    If not, it returns None. It uses a sub-function to do
    the recursive search.

    item: str or integer
    '''
    # Calculates the lenght of the sorted list one time before
    # the recursive search starts, to avoid complexity increases.
    lenght = len(sorted_list)
    # Initiates de recursive bisectional search using a sub-function:
    return bisect_recursion(sorted_list, lenght, item, pos0=0, posf=lenght-1)


if __name__ == "__main__":
    system('clear')
    file_path = "From the book/master/code/words.txt"
    list_of_words = make_words_list(file_path)
    words = list_of_words
    times = []
    results = []
    for word in words:
        t0 = time()
        search_result = in_bisect(list_of_words, word)
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
