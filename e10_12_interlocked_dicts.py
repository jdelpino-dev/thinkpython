#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 10.12 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 10.2: Interlock Words

"""
My code is way faster than  Downey's, and, of course, is way more complex.
Of course it's more complex because it actually finds all the words in
words.txt that are interlock with two components and/or three components
Moreover, it finds all those components! However, it uses a broader
definition of interlock words that encompases Downeys definition.

In total, it finds 6,474 words and it does it in  4.925 seconds!!!!
I also implemented a restricted version of the code that finds
all the restricted interlocks very faster: 0.4433 seconds.

Because the more restricted definition. Downey's only find
less than 35% of the interloks that mine does –that is, only 2,245–...
However, besides that it's important to consider that his code is
also highly time inefficient. That's not only because it uses his inefficient
bisection search algorithm, but also because, for each word, it finds first
all components that it considers and then, after that, it verifies
if they are included in words.txt. Even if I would've implemented my solution
with list instead of diccionaries, my code will be way more faster,
efficient and complete.
"""


from os import system
from time import time
from bibth3_strings import make_plain


def add_dict_of_dicts(the_dict, the_key, sub_key, element=None):
    if the_key in the_dict:
        sub_dict = the_dict[the_key]
        if sub_key in sub_dict:
            pass
        else:
            sub_dict[sub_key] = element
    else:
        the_dict[the_key] = {sub_key: element}


def make_lenghts_dict(file_name):
    words = open(file_name)
    lenghts_dict = {}
    for word in words:
        word = make_plain(word)
        lenght = len(word)
        add_dict_of_dicts(lenghts_dict, lenght, word)
    return lenghts_dict


def n_comps_interlock(string, n):
    comps = []
    for i in range(n):
        inter = string[i::n]
        comps.append(inter)
    return tuple(comps)


def de_interlock_restricted(string, lenght, lenghts_dict,
                            interlock_dicc):
    '''Using the restricted definition of interlock words,
    finds any interlocked string that is in the lenghts_dict, and
    it also find all its possible trios and pairs of words included
    in lenghts_dict.
    '''
    if string == "schooled":
        print("schooled!")
    comps_list = []
    temp = []
    temp.append(n_comps_interlock(string, 2))
    temp.append(n_comps_interlock(string, 3))
    for comps in temp:
        count = 0
        for comp in comps:
            comp_lenght = len(comp)
            if comp_lenght in lenghts_dict:
                words = lenghts_dict[comp_lenght]
                if comp in words:
                    count += 1
        if count == len(comps):
            comps_list.append(comps)
    if comps_list:
        add_dict_of_dicts(interlock_dicc, lenght, string, element=comps_list)


def make_interlock_dict_restricted(lenghts_dict):
    interlock_dicc = {}
    for lenght in lenghts_dict:
        words = lenghts_dict[lenght]
        for word in words:
            if word == "schooled":
                print("schooled!")
            de_interlock_restricted(word, lenght, lenghts_dict,
                                    interlock_dicc)
    return interlock_dicc


def make_comp_two_interloks(string, lenght1, lenght2, comp_n):
    string_lenght = len(string)
    comp = ""
    shared_lenght = min(lenght1, lenght2)
    if comp_n == 1:
        lenght = lenght1
        start = 0
        first_end = (2 * shared_lenght) - 1
    else:
        lenght = lenght2
        start = 1
        first_end = 2 * shared_lenght
    for k in range(start, first_end, 2):
        comp += string[k]
    current_lenght = len(comp)
    if current_lenght < lenght:
        second_start = 2 * shared_lenght
        end = string_lenght
        for m in range(second_start, end):
            comp += string[m]
    return comp


def make_first_piece(string, start, first_end, steps):
    comp = ""
    for k in range(start, first_end, steps):
        comp += string[k]
    return comp


def make_second_piece(string, string_lenght, lenght, second_start,
                      shared_lenght, next_comp_n, comp, the_other):
    if next_comp_n == 0:
        end = string_lenght
        for m in range(second_start, end):
            comp += string[m]
    else:
        rest_of_string = string[second_start:]
        rest_of_lenght = lenght - len(comp)
        rest_of_other = the_other - shared_lenght
        rest_comp = ""
        if next_comp_n == 1:
            rest_comp = make_comp_two_interloks(rest_of_string,
                                                rest_of_lenght,
                                                rest_of_other, 1)
        elif next_comp_n == 2:
            rest_comp = make_comp_two_interloks(rest_of_string,
                                                rest_of_other,
                                                rest_of_lenght, 2)
        comp += rest_comp
    return comp


def make_comp_three_interloks(string, lenght1, lenght2, lenght3, comp_n):
    string_lenght = len(string)
    shared_lenght = min(lenght1, lenght2, lenght3)
    the_other = ""
    if comp_n == 1:
        lenght = lenght1
        start = 0
        first_end = (3 * shared_lenght) - 2
        if lenght2 == lenght3:
            next_comp_n = 0
        else:
            next_comp_n = 1
            the_other = max(lenght2, lenght3)
    elif comp_n == 2:
        lenght = lenght2
        start = 1
        first_end = (3 * shared_lenght) - 1
        if lenght1 == lenght3:
            next_comp_n = 0
        elif lenght1 > lenght3:
            next_comp_n = 2
            the_other = lenght1
        else:
            next_comp_n = 1
            the_other = lenght3
    elif comp_n == 3:
        lenght = lenght3
        start = 2
        first_end = 3 * shared_lenght
        if lenght1 == lenght2:
            next_comp_n = 0
        else:
            next_comp_n = 2
            the_other = max(lenght1, lenght2)
    comp = make_first_piece(string, start, first_end, 3)
    current_lenght = len(comp)
    if current_lenght < lenght:
        second_start = 3 * shared_lenght
        comp = make_second_piece(string, string_lenght, lenght, second_start,
                                 shared_lenght, next_comp_n, comp,
                                 the_other)
    return comp


def de_interlock_all_two_interloks(string):
    '''De-interlocks any string in all its possible
    interlocked pairs.
    '''
    lenght = len(string)
    comps_list = []
    for i in range(1, lenght):
        j = lenght - i
        comp1 = make_comp_two_interloks(string, i, j, 1)
        comp2 = make_comp_two_interloks(string, i, j, 2)
        comps = (comp1, comp2)
        comps_list.append(comps)
    return comps_list


def de_interlock_all_three_interloks(string):
    '''De-interlocks any string in all its possible
    interlocked trios.
    '''
    lenght = len(string)
    comps_list = []
    for i in range(1, lenght):
        jk = lenght - i
        for j in range(1, jk):
            k = jk - j
            comp1 = make_comp_three_interloks(string, i, j, k, 1)
            comp2 = make_comp_three_interloks(string, i, j, k, 2)
            comp3 = make_comp_three_interloks(string, i, j, k, 3)
            comps = (comp1, comp2, comp3)
            comps_list.append(comps)
    return comps_list


def de_interlock_all_2_and_3_interloks(string):
    '''De-interlocks any string in all its possible
    interlocked paits and trios.
    '''
    lenght = len(string)
    comps_list = []
    for i in range(0, lenght):
        jk = lenght - i
        for j in range(1, jk):
            k = jk - j
            comp1 = make_comp_three_interloks(string, i, j, k, 1)
            comp2 = make_comp_three_interloks(string, i, j, k, 2)
            comp3 = make_comp_three_interloks(string, i, j, k, 3)
            if comp1 == "":
                comps = (comp2, comp3)
            else:
                comps = (comp1, comp2, comp3)
            comps_list.append(comps)
    return comps_list


def de_interlock_two_interlocks(string, lenght, lenghts_dict, interlock_dicc):
    '''De-interlocks any string in all its possible pairs
    of interlocked words included in lenghts_dict.
    '''
    comps_list = []
    for i in range(1, lenght):
        j = lenght - i
        if (i in lenghts_dict) and (j in lenghts_dict):
            comp1 = make_comp_two_interloks(string, i, j, 1)
            strings1 = lenghts_dict[i]
            if comp1 in strings1:
                comp2 = make_comp_two_interloks(string, i, j, 2)
                strings2 = lenghts_dict[j]
                if comp2 in strings2:
                    comps = (comp1, comp2)
                    comps_list.append(comps)
                    add_dict_of_dicts(interlock_dicc, lenght, string,
                                      element=comps_list)


def de_interlock_2_and_3_interlocks(string, lenght, lenghts_dict,
                                    interlock_dicc):
    '''De-interlocks any string in all its possible trios
    and pairs of interlocked words included in lenghts_dict.
    '''
    comps_list = []
    for i in range(0, lenght):
        jk = lenght - i
        for j in range(1, jk):
            k = jk - j
            if ((j in lenghts_dict) and (k in lenghts_dict) and
               (i in lenghts_dict or i == 0)):
                comp2 = make_comp_three_interloks(string, i, j, k, 2)
                strings2 = lenghts_dict[j]
                if comp2 in strings2:
                    comp3 = make_comp_three_interloks(string, i, j, k, 3)
                    strings3 = lenghts_dict[k]
                    if comp3 in strings3:
                        if i == 0:
                            comps = (comp2, comp3)
                            comps_list.append(comps)
                        else:
                            comp1 = make_comp_three_interloks(string, i, j,
                                                              k, 1)
                            strings1 = lenghts_dict[i]
                            if comp1 in strings1:
                                comps = (comp1, comp2, comp3)
                                comps_list.append(comps)
    if comps_list:
        add_dict_of_dicts(interlock_dicc, lenght, string, element=comps_list)


def make_interlock_dict(lenghts_dict):
    interlock_dicc = {}
    for lenght in lenghts_dict:
        words = lenghts_dict[lenght]
        for word in words:
            de_interlock_2_and_3_interlocks(word, lenght, lenghts_dict,
                                            interlock_dicc)
    return interlock_dicc


def print_dict_of_dicts(dict_of_dicts):
    for key in dict_of_dicts:
        print(key, ":")
        sub_dict = dict_of_dicts[key]
        for sub_key in sub_dict:
            element = sub_dict[sub_key]
            if element is None:
                print_element = ""
            else:
                print_element = ":" + str(element)
            print(sub_key, print_element)
        print("\n")


def print_dict(dict_of_dicts):
    for key in dict_of_dicts:
        element = dict_of_dicts[key]
        print(key, ":", element)


if __name__ == "__main__":
    system('clear')
    t0_1 = time()
    file_path = "From the book/master/code/words.txt"
    t1 = time() - t0_1
    main_dictionary = make_lenghts_dict(file_path)
    t0_2 = time()
    interlock_dict = make_interlock_dict(main_dictionary)
    # interlock_dict = make_interlock_dict_restricted(main_dictionary)
    t2 = time() - t0_2
    print("\n")
    print(len(main_dictionary))
    print(len(interlock_dict))
    print("\n")
    total_interloks = 0
    lenghts = []
    for lenght in interlock_dict:
        n_interlocks = len(interlock_dict[lenght])
        lenghts.append((lenght, n_interlocks))
        total_interloks += n_interlocks
    lenghts.sort()
    print(total_interloks)
    print("\n")
    print(t1)
    print(t2)
    print(t1 + t2)
    print("\n")
    while True:
        print("Lenghts: ", lenghts)
        lenght = input("Which lenght? ")
        if lenght != "":
            lenght = int(lenght)
            print_dict(interlock_dict[lenght])
            print("\n")
        else:
            break
    system('clear')
    while True:
        word = input("Which word? ")
        if word != "":
            lenght = len(word)
            words = interlock_dict[lenght]
            if word in words:
                comps_list = words[word]
                print(f'"{word.upper()}" is in the interlock dictionary.')
                print('Its componets are:')
                print(comps_list)
                print("\n")
            else:
                print(f'"Sorry, {word.upper()}" ' +
                      'is not in the interlock dictionary.')
                print("Try with another word...")
                print("\n")
        else:
            break
    print("\n")
