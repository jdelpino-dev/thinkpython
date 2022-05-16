#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercises 8.0 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 8.0: Miscelanea

from os import system


def backward_printing(string):
    i = len(string) - 1
    while i >= 0:
        letter = string[i]
        print(letter)
        i = i - 1


def ducklings(prefixes, suffix):
    for prefix in prefixes:
        print(prefix + suffix)


def is_reverse(word1, word2):
    # Guardian 1
    if len(word1) != len(word2):
        return False
    # Loop
    i = 0
    j = len(word2) - 1
    while j >= 0:
        # Iterative comprobation
        if word1[i] != word2[j]:
            return False
        i += 1
        j = j - 1
    return True


def calc_ocurr(words, letters):
    '''
    Parameters:

    "words" must be a set or list of words. If there is
    words that are included, thei multiple ocurrences
    are considerred only if there ar case differences.

    "letters" must be a string, set or list of letters or
    characters.
    '''
    o_dicc = {}
    words = set(words)
    for word in words:
        w_list = []
        end = len(word)
        for letter in letters:
            letter_dic = {}
            i = word.count(letter)
            index = 0
            index_list = []
            while i > 0:
                index = word.index(letter, index, end)
                index_list.append(index)
                index += 1
                i = i - 1
            if index_list:
                letter_dic = {"letter": letter, "index_list": index_list}
                w_list.append(letter_dic)
        o_dicc[word] = w_list
    return o_dicc


if __name__ == "__main__":
    system('clear')
    # backward_printing("paralelepípedo")
    # print("\n")
    # ducklings("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ", "ack")
    # print("\n\n")
    # ocurrences = calc_ocurr(["Anagrama", "Mamograma",
    #                         "mamograma", "Mamograma", "grafema"],
    #                        ["A", "a", "g", "m"])
    # abecedario = "AaBbCcDdEeFfGgHhIiJjKlLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz"
    # ocurrences = calc_ocurr(["Paralelepípedo"], abecedario)
    # print(ocurrences, "\n\n")
    print(is_reverse("pots", "stop"))
    print("\n\n")
