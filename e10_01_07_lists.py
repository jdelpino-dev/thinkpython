#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 10.1 - 10.7 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 10.1 - 10.7: List Exercices

from os import system
from random import randint
from bibth3_strings import make_plain, no_whitespace
from time import time
# from bibth3_strings import make_plain_with_accents


def nested_sum(main_list):
    '''Takes a list of lists of integers and adds up
    the elements from all of the nested lists.
    '''
    summation = 0
    for num_list in main_list:
        summation += sum(num_list)
    return summation


def cum_sum(the_list):
    '''Takes a list of numbers and returns the cumulative sum; that is, a new
    list where the ith element is the sum of the first i + 1 elements from
    the original list.
    '''
    cum_list = []
    for i in range(len(the_list)):
        elements = i + 1
        summation = sum(the_list[:elements])
        cum_list.append(summation)
    return cum_list


def middle(the_list):
    '''Takes a list and returns a new list that contains all but the first and
    last elements.
    '''
    return the_list[1:-1]


def chop(the_list):
    '''Takes a list, modifies it by removing the first and
    last elements, and returns None.
    '''
    del the_list[0]
    del the_list[-1]


def is_sorted(the_list):
    '''Takes a list as a parameter and returns True if
    the list is sorted in ascending order and False otherwise.
    '''
    return True if the_list == sorted(the_list) else False


def is_reverse(str1, str2):
    return True if str1 == str2[::] else False


def is_anagram(str1, str2):
    str1, str2 = make_plain(str1), make_plain(str2)
    str1, str2 = no_whitespace(str1), no_whitespace(str2)
    if str1 == str2 or len(str1) != len(str2):
        return False
    if is_reverse(str1, str2):
        return True
    for letter in str1:
        if letter not in str2:
            return False
    return True


def has_duplicate_old(the_list):
    lenght = len(the_list)
    i = 0
    j = 1
    while j < lenght:
        if the_list[i] == the_list[j]:
            return True
        i += 1
        j += 1
    return False


def has_duplicates_old2(the_list):
    t0 = time()
    list_copy = the_list[:]
    list_copy.sort()
    lenght = len(list_copy)
    i = 0
    while i + 1 < lenght:
        item, next_item = list_copy[i], list_copy[i + 1]
        if item == next_item:
            print(time() - t0)
            return True
        i += 1
    print(time() - t0)
    return False


def has_duplicates(the_list):
    t0 = time()
    d = {}
    for item in the_list:
        d[item] = d.get(item, 0) + 1
        if d[item] >= 2:
            print(time() - t0)
            return True
    print(time() - t0)
    return False


def chop_secuence(the_list):
    print(the_list)
    suc_mid = the_list[:]
    lenght = len(the_list)
    if lenght % 2 == 0:
        loops = int(lenght / 2)
    else:
        loops = int((lenght + 1) / 2)
    for i in range(loops):
        suc_mid = middle(suc_mid)
        print(suc_mid)


def count_duplicates(the_list):
    duplicated = []
    lenght = len(the_list)
    for i in range(lenght):
        j = i + 1
        while j < lenght:
            item, next_item = the_list[i], the_list[j]
            if item == next_item and item not in duplicated:
                duplicated.append(item)
            j += 1
    return len(duplicated)


def half_cut_point(lenght):
    '''Return the index of the last element of the first half of the list.
    If the list has an odd lenght, then the first half is smaller than the
    seconf by 1 item.

    When the list is a singleton or the empty list, the function returns -1.
    '''
    cut_point = int((lenght // 2) - 1)
    return cut_point


def random_elements(the_list, n):
    random_list = []
    lenght = len(the_list)
    if n > lenght:
        return []
    while len(random_list) < n:
        random_index = randint(0, lenght - 1)
        random_item = the_list[random_index]
        if random_item not in random_list:
            random_list.append(random_item)
    return random_list


if __name__ == "__main__":
    system('clear')
    # the_list = list(range(6)) + [0, 1, 3, 11, 11]
    # print(the_list, count_duplicates(the_list))
    # print("\n")
    # the_list = list(range(0, 20))
    # chop(the_list)
    # print(the_list, is_sorted(the_list))
    # the_list.sort(reverse=True)
    # print(the_list, is_sorted(the_list))
    # main_list = [[0], [1], [1, 2], [1, 2, 3]]
    # print(nested_sum(main_list))
    # the_list = list(range(0, 11))
    # print(the_list, cum_sum(the_list))
    # print(the_list, middle(the_list))
    # the_list = list(range(0, 21))
    # chop_secuence(the_list)
    # anagrams = [("listen", "silent"), ("debit card", "bad credit"),
    #            ("Coronavirus", "carnivorous"),
    #            ("New York Times", "monkeys write"),
    #            ("placebo", "obecalp"), ("funeral", "real fun"),
    #            ("restful", "fluster"), ("roma", "amor"),
    #            ("adultery", "true lady")]
    # not_anagrams = [("corina", "corina"), ("anilina", "Anilina"),
    #                ("cocinar", "racionar")]
    # for pair in anagrams:
    #    print(pair, is_anagram(*pair))
    # print("\n")
    # for pair in not_anagrams:
    #    print(pair, is_anagram(*pair))
    # the_list = ["Casa", "casa", "árbol", "arboleda"]
    # print(the_list, has_duplicates(the_list))
    # print("\n")
    # temp_list = list(map(make_plain_with_accents, the_list))
    # print(temp_list, has_duplicates(temp_list))
    # print("\n")
