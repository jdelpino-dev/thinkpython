#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 9.9 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 9.9: Car Talk Puzzler III

# My code mark is 0.0003337860107421875 seconds
# Allen Downey's mark is 0.01728510856628418
# That is... my code is 98 % faster, or 52 times faster!!!

from os import system
from time import time


def add_to_dict(dict_of_list, key_d, element):
    if key_d in dict_of_list:
        dict_of_list[key_d].append(element)
    else:
        dict_of_list[key_d] = [element]


def setify(dict_of_list):
    for key in dict_of_list:
        the_list = dict_of_list[key]
        the_set = set(the_list)
        dict_of_list[key] = the_set


def reverse_ages_generator():
    """Checks each possible age difference between son and mother
    to find how many palindromes each delta can generates during
    their lifes.
    """
    t0 = time()
    ages = {}
    # This loop do the main search for age palindromes:
    for son_age in range(1, 99):
        son_age_st = str(son_age).zfill(2)
        mother_age_st = son_age_st[::-1]  # Creates the age palindrome
        mother_age = int(mother_age_st)
        delta = abs(mother_age - son_age)  # Calculates the age difference
        conditions = ((son_age < mother_age < 121) and
                      (9 < delta < 71))
        if conditions:
            # Assuming that mother and daughter don't have the same birthday,
            # they have two chances per year to have palindromic ages.
            # On my first version I did't consider this detail... I learned
            # from the book's author.
            age_tuple = (son_age_st, mother_age_st)
            add_to_dict(ages, str(delta), age_tuple)
            add_to_dict(ages, str(delta - 1), age_tuple)
    # Make sure that are not repeated ages tuples associated with each delta:
    setify(ages)
    tf = time()
    print(tf-t0)
    return ages


if __name__ == "__main__":
    system('clear')
    ages = reverse_ages_generator()
    for key in ages:
        print(key, ages[key])
    print("\n")
    for delta in ages:
        delta_list = ages[delta]
        if len(delta_list) >= 8:
            print(delta, delta_list)
    print("\n\n")
