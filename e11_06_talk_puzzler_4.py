#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 11.6 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 11.6: Car Talk Puzzler IV: Homophones

from os import system
from bibth_downey_code import read_dictionary
from bibth3_dicts import make_lenghts_dict


def seek_homophones():
    global five_letters_words, four_letters_words
    global homophones_dict, pronouncing_dict
    for word in five_letters_words:
        if word == "guses":
            print("Here!")
        dw1 = word[1:]
        dw2 = word[0] + word[2:]
        extended_in = []
        for i in range(1, 10):
            dw1_ext = dw1 + f"({i})"
            dw2_ext = dw2 + f"({i})"
            if dw1_ext in pronouncing_dict and dw2_ext in pronouncing_dict:
                extended_in.append(dw1_ext)
                extended_in.append(dw2_ext)
        if (dw1 in pronouncing_dict and dw2 in pronouncing_dict and
           dw1 in four_letters_words and dw2 in four_letters_words):
            pron_dw1 = pronouncing_dict[dw1]
            pron_dw2 = pronouncing_dict[dw2]
            pair = (dw1, dw2)
            if pron_dw1 == pron_dw2:
                if homophones_dict.setdefault(word, [pair]) != [pair]:
                    homophones_dict[word].append(pair)


def print_homophones():
    global homophones_dict
    if homophones_dict:
        print("There are words that satisfy the conditions!\n")
        for word in homophones_dict:
            homophones = homophones_dict[word]
            print(f'"{word.capitalize()}"\'s homophone pair is:')
            for pair in homophones:
                print(pair)
            print("\n")
    else:
        print("Sorry, there is no-word that satisfy the conditions.")


if __name__ == "__main__":
    system('clear')

    pronouncing_file = "From the book/master/code/c06d"
    pronouncing_dict = read_dictionary(pronouncing_file)

    words_file = "From the book/master/code/words.txt"
    words_by_lenght = make_lenghts_dict(words_file)

    five_letters_words, four_letters_words = {}, {}

    if 5 in words_by_lenght:
        five_letters_words = words_by_lenght[5]
    if 4 in words_by_lenght:
        four_letters_words = words_by_lenght[4]
    if five_letters_words and four_letters_words:
        homophones_dict = {}
        seek_homophones()
        print_homophones()
    else:
        print("Sorry, there is no-word that satisfy the conditions.")
