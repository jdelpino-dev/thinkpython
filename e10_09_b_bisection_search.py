#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 10.9 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 10.9: Bisection Search #2 (both recursive & iterative)

''' Mine in_bisect recursive function is way more efficient
than Downey's. On average mine takes 0.0000151045 seconds to find
a word on the given list –that has 113,808 items–, while Downey's
take 0.0032 seconds. Than is, my function is 99.6% faster. My recursive
function performance is even a little better with integers as items
instead of string, with a average of 0.0000146961.

My iterative version is even faster. It takes 0.000011489 seconds
with strings and 0.000011067 with integers.

Because of the sliced list copies, Downey's time complexity is
O(n/k) being k a real number 2 < k < n, while my two functions are
O(Log n)- The recursive function is especifically log(n)/2**-p,
being a number 19 < p < 21

    5000K numbrs, 0.000020418, p = 1089896.01
    p = 2**-20.055759054952761

    2000K numbrs, 0.000017234 , p = 1,214,550.81
    p = 2**-20.211991414836615

    1500K numbrs, 0.000017985, p =  1,140,757.91
    p = 2**-20.121561226770426

    500K numbers, 0.000015521, p = 1,219,738.97 (delta 500K-113,809 = 107,736)
    p = 2**-20.084729749036027

    100 numbers,  0.000006894, p =   963,715.72
    p = 2**-19.878248112768686

    10 numbers,   0.000005857, p =   567,172.29
    p = 2**-19.113427523840518

This is an interesting case of how you can ruin an algorithm's
time complexity with a wrong implementation.
'''

from os import system
from time import time
from bibth3_strings import make_words_list
from e10_01_07_lists import half_cut_point


def in_bisect_it(sorted_list, item):
    '''Does the iterative bisection search of an item on a sorted list
    of strings or integers. If the item is on the list it returns the index.
    If not, it returns None.

    item: str or integer
    '''
    # Initiates de loop after initializing the variables:
    lenght = len(sorted_list)
    pos0 = 0
    posf = lenght - 1
    while True:
        # Check all the bace cases:
        sub_lenght = posf - pos0 + 1
        if sub_lenght == 0:
            return None
        if (item > sorted_list[posf]) or (item < sorted_list[pos0]):
            return None
        if item == sorted_list[pos0]:
            return pos0
        if item == sorted_list[posf]:
            return posf
        if sub_lenght == 1 or sub_lenght == 2:
            return None
        # Calculates the new values and continues the bisection search:
        cut_point = half_cut_point(sub_lenght) + pos0
        cut_point2 = cut_point + 1
        cut_item = sorted_list[cut_point]
        # Decides in which sub-list it will continue the search:
        if item > cut_item:
            pos0 = cut_point2
        else:
            posf = cut_point


def bisect_recur(sorted_list, lenght, item, pos0, posf):
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
    if sub_lenght == 1 or sub_lenght == 2:
        return None
    # Calculates the new values and continues the recursive bisection search:
    cut_point = half_cut_point(sub_lenght) + pos0
    cut_point2 = cut_point + 1
    cut_item = sorted_list[cut_point]
    # Decides which brach of the bisection search to follow:
    if item > cut_item:
        return bisect_recur(sorted_list, lenght, item,
                            pos0=cut_point2, posf=posf)
    else:
        return bisect_recur(sorted_list, lenght, item,
                            pos0=pos0, posf=cut_point)


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
    return bisect_recur(sorted_list, lenght, item, pos0=0, posf=lenght-1)


if __name__ == "__main__":
    system('clear')
    file_path = "From the book/master/code/words.txt"
    list_of_words = make_words_list(file_path)
    # list_of_words = list(range(113810))
    words = list_of_words
    times = []
    results = []
    for i in range(10):
        for word in words:
            t0 = time()
            search_result = in_bisect_it(list_of_words, word)
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
