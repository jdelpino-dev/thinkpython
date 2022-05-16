#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 11.5 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 11.5: Rotate Pairs

from os import system
from bibth3_dicts import add_dict_of_dicts, make_lenghts_dict, print_dict
from bibth3_strings import en_letters, rot_encoder

"""Downey function finds 1,137 rotate pairs using rotations from 1 to 14, but
they contain 47 repeated pairs. There are actually 1090 reversible pairs,
and my program find them all faster than Downeys.

From my analysis of the results, I concluded that the best ciphers
for English are: (5, 21), (2, 24), and (13, 13). Because they are
the one for which there are less rotate words in the word list.
"""


def find_word_rotations(word, dict_of_lenghts, chr_blocks, dict_of_pairs,
                        ciphers_dict):
    for rotation in range(1, 26):
        rotate_word = rot_encoder(word, rotation, en_letters)
        lenght = len(rotate_word)
        word_group = dict_of_lenghts[lenght]
        rotate_pair = (word, rotate_word)
        inv_pair = (rotate_word, word)
        if rotate_word in word_group:
            if lenght in dict_of_pairs:
                pairs_group = dict_of_pairs[lenght]
            else:
                pairs_group = {}
            if inv_pair not in pairs_group:
                ciphers = (rotation, 26 - rotation)
                add_dict_of_dicts(dict_of_pairs, lenght,
                                  rotate_pair,
                                  element=ciphers)
                add_dict_of_dicts(ciphers_dict, ciphers,
                                  rotate_pair,
                                  element=None)


def make_rotate_dict(dict_of_lenghts, chr_blocks):
    rotate_pairs = {}
    ciphers_dict = {}
    for lenght in dict_of_lenghts:
        for word in dict_of_lenghts[lenght]:
            find_word_rotations(word, dict_of_lenghts, chr_blocks,
                                rotate_pairs, ciphers_dict)
    return rotate_pairs, ciphers_dict


def calculate_size():
    global rotate_pairs
    total_rotate = 0
    lenghts = []
    for lenght in rotate_pairs:
        n_rotate = len(rotate_pairs[lenght])
        lenghts.append((lenght, n_rotate))
        total_rotate += n_rotate
    lenghts.sort()
    print(total_rotate)
    return lenghts


def lenghts_search():
    global lenghts, rotate_pairs
    while True:
        print("Lenghts: ", lenghts)
        lenght = input("Which lenght? ")
        if lenght != "":
            lenght = int(lenght)
            print_dict(rotate_pairs[lenght])
            print("\n")
        else:
            break


def words_search():
    global rotate_pairs
    system('clear')
    while True:
        word = input("Which word? ")
        if word != "":
            lenght = len(word)
            pairs = rotate_pairs[lenght]
            is_pair = False
            the_word_pairs = []
            for pair in pairs:
                if (word == pair[0] or
                   word == pair[1]):
                    is_pair = True
                    triplet = (*pair, pairs[pair])
                    the_word_pairs.append(triplet)
            if is_pair:
                print(f'"{word.upper()}" is in the rotate dictionary.')
                print('The rotate pair(s) is(are):')
                for pair in the_word_pairs:
                    print(pair)
                print("\n")
            else:
                print(f'"Sorry, {word.upper()}" ' +
                      'is not in the interlock dictionary.')
                print("Try with another word...")
                print("\n")
        else:
            break


if __name__ == "__main__":
    system('clear')
    file_path = "From the book/master/code/words.txt"

    words_by_lenght = make_lenghts_dict(file_path)
    rotate_pairs, ciphers_dict = make_rotate_dict(words_by_lenght, en_letters)

    print("Word's Lengts:", len(words_by_lenght))
    print("Rotate's Lengts:", len(rotate_pairs))

    print("\n")
    print("\n")

    lenghts = calculate_size()
    lenghts_search()
    words_search()

    system('clear')
    for cipher in ciphers_dict:
        pairs = ciphers_dict[cipher]
        print(cipher, len(pairs))
    print("\n")
    print("\n\n")
