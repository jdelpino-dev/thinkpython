#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 9.9 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 9.9: Car Talk Puzzler III

# My code mark is 0.00036597251892089844 seconds
# Allen Downey's mark is 0.01728510856628418
# That is... my code is 97.88 % faster!!!

from os import system


def reverse_ages_generator():
    """Checks each possible age difference between son and mother
    to find how many palindromes each delta can generates during
    their lifes.
    """
    ages_by_delta = {}
    # This loop creates the data structure that the other lopp will use
    # to store each delta with its list of age palindromes.
    for delta in range(10, 72):
        ages_by_delta[str(delta)] = []
    # This loop do the main search for age palindromes:
    for son_age in range(1, 99):
        son_age_st = str(son_age).zfill(2)
        mother_age_st = son_age_st[::-1]
        mother_age = int(mother_age_st)
        age_delta = abs(mother_age - son_age)
        conditions = ((son_age < mother_age < 121) and
                      (9 < age_delta < 71))
        if conditions:
            # Assuming that mother and daughter don't have the same birthday,
            # they have two chances per year to have palindromic ages.
            # On my first version I did't consider this detail... I learned
            # from the book's author.
            ages_by_delta[str(age_delta - 1)].append((son_age_st,
                                                      mother_age_st))
            ages_by_delta[str(age_delta)].append((son_age_st,
                                                  mother_age_st))
    return ages_by_delta


if __name__ == "__main__":
    system('clear')
    ages = reverse_ages_generator()
    for delta in ages:
        delta_list = ages[delta]
        if len(delta_list) >= 8:
            print(delta, delta_list)
