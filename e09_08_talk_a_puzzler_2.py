#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 9.8 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 9.8: Car Talk Puzzler II

from os import system
from bibth3_strings import is_palindrome


def make_palindrome(string, middle_st=""):
    return string[::-1] + middle_st + string


def find_sequences():
    sequences = []
    for n in range(1, 1000):
        count = 0
        string = str(n)
        if n < 99:
            string = string.zfill(3)
        pal = make_palindrome(string)
        pal_n = int(pal)
        pal_4 = pal_n - 4
        pal_3 = pal_n - 3
        pal_2 = pal_n - 2
        pal_1 = pal_n - 1
        n_seq = [pal_4, pal_3, pal_2, pal_1, pal_n]
        s_seq = list(map(str, n_seq))
        pal_3_ext = s_seq[1][-4:]
        pal_2_ext = s_seq[2][-5:]
        pal_1_ext = s_seq[3][-5:-1]
        if is_palindrome(pal_3_ext):
            count += 1
        if is_palindrome(pal_2_ext):
            count += 1
        if is_palindrome(pal_1_ext):
            count += 1
        if count == 3:
            sequences.append(s_seq)
    print("\n")
    return sequences


if __name__ == "__main__":
    system('clear')
    for seq in find_sequences():
        print(seq)
    print("\n\n")
