#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 9.8 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 9.8: Car Talk Puzzler II (improved code)

from os import system
from bibth3_strings import has_palindrome, make_palindrome
from time import time


def find_all_sequences():
    t0 = time()
    sequences = []
    # This loop generates all the 6 digits number palindromes including
    # zeroes to the left, generates a sequence of 4 minor numbers
    # successively substracting one: pal-1, pal-2, pal-3, pal-4. After that,
    # it checks on them a set of pre-stablished properties according
    # to the car puzzler.
    for n in range(1, 1000):
        # Prepares the half of each 6-digit palindrome
        string = str(n)
        string = string.zfill(3)
        # Contruc each 6-digit palindrome
        pal = make_palindrome(string)
        pal_n = int(pal)
        # Generates the sequence of 4 minor numbers from pal.
        # pal_m4 doesn't have to meet any other condition.
        pal_m1 = pal_n - 1
        pal_m2 = pal_n - 2
        pal_m3 = pal_n - 3
        pal_m4 = pal_n - 4
        # Generates their string representations
        pal_m1_s = str(pal_m1).zfill(6)
        pal_m2_s = str(pal_m2).zfill(6)
        pal_m3_s = str(pal_m3).zfill(6)
        pal_m4_s = str(pal_m4).zfill(6)
        # Checks if the sequence we produced from pal have the pre-stablished
        # properties. It is not necesarry to check pal, because we created it
        # as a 6 digit palindrome, nor pal_m4 –see above–.
        # Prop #1: 4-digit-middle-palindrome
        cond_n_minus1 = has_palindrome(pal_m1_s, 1, 4)
        # Prop #2: 5-digit-palindrome
        cond_n_minus2 = has_palindrome(pal_m2_s, 1, 5)
        # Prop #3: 4-digit-palindrome
        cond_n_minus3 = has_palindrome(pal_m3_s, 2, 4)
        # All the properties together
        seq_properties = (cond_n_minus1 and
                          cond_n_minus2 and cond_n_minus3)
        # In case the sequence meets the conditions, it adds
        # it to the list of results:
        if seq_properties:
            # Creates the lists for the string representation of the sequence.
            s_seq = [pal_m4_s, pal_m3_s, pal_m2_s, pal, pal_m1_s, pal]
            # Add the sequence to the results:
            sequences.append(s_seq)
    tf = time()
    print(tf-t0, "\n")
    return sequences


if __name__ == "__main__":
    system('clear')
    for seq in find_all_sequences():
        print(seq)
    print("\n\n")
