#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 13.8 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 13.8: Markov Analysis: Playing with Text Generation

from os import system
from collections import deque
from bibth3_dicts import add_to_dictlist
from bibth3_strings import make_plain, no_space_nor_punctuation
from random import choice


def make_ngrams(files: list, n: int) -> (dict, list):
    ngrams_dict = dict()
    ngrams_list = list()
    n_gram = deque(maxlen=n)
    for path in files:
        the_file = open(path)
        for line in the_file:
            if line[0] == "#":
                continue
            line = make_plain(line)
            line = line.split()
            line_lenght = len(line)
            i = 0
            while i < line_lenght:
                line[i] = no_space_nor_punctuation(line[i])
                i += 1
            line = deque(line)
            delta_gram = n - len(n_gram)
            if delta_gram > 0:
                for i in range(0, delta_gram):
                    if line:
                        n_gram.append(line.popleft())
            if len(n_gram) == n:
                while line:
                    word = line.popleft()
                    tuple_gram = tuple(n_gram)
                    add_to_dictlist(ngrams_dict,
                                    tuple_gram,
                                    word,
                                    "as_an_element")
                    ngrams_list.append(tuple_gram)
                    n_gram.append(word)
    return (ngrams_dict, ngrams_list)


def print_ngrams(the_dict, n_items):
    n = 1
    for ngram in the_dict:
        words = the_dict[ngram]
        z = min(len(words), n_items)
        print(f"[{n}] ", ngram, " -->> ", words[:z])
        n += 1


def shift_ngram(n_gram: tuple, word: str) -> (str, tuple):
    return (n_gram[0], n_gram[1:] + (word,))


def generate_text(n_grams: dict, propl: list,
                  lenght: int, line_len: int) -> list:
    text = []
    ngram = choice(propl)
    del propl
    words_added = 0
    while words_added < lenght:
        line = []
        while len(line) < line_len:
            word_list = n_grams[ngram]
            word = choice(word_list)
            next_state = shift_ngram(ngram, word)
            line.append(next_state[0])
            words_added += 1
            ngram = next_state[1]
        text.append(line)
    return text


def print_text(text: list):
    for line in text:
        line = " ".join(line)
        print(line)
    print("\n")


if __name__ == "__main__":

    gulliver_path = "files/gulliver_s_travels.txt"
    mobydick_path = "files/moby_dick_or_the_whale.txt"
    huckle_path = "files/huckleberry_finn.txt"
    grimms_path = "files/grimms_tales.txt"
    island_path = "files/secret_island.txt"

    filepaths = [gulliver_path, mobydick_path, huckle_path, grimms_path]
    mashup_combo = make_ngrams(filepaths, 2)
    mashup_ngrams = mashup_combo[0]
    mashup_propl = mashup_combo[1]
    del mashup_combo

    # system('clear')
    # for i in range(1, 13):
    #     mashup_text = generate_text(mashup_ngrams, mashup_propl,
    #                                 650, 13)
    #     print(f"[{i}] Text #{i}:")
    #     print_text(mashup_text)
    # del mashup_propl

    # testfile_path = "book_courses/thinkpython/files/test_file.txt"
    # test_ngrams = make_ngrams(testfile_path, 2)

    ngrams_combo = make_ngrams([gulliver_path], 4)
    gulliver_ngrams = ngrams_combo[0]
    gulliver_propl = ngrams_combo[1]
    del ngrams_combo

    system('clear')
    for i in range(1, 21):
        gulliverick = generate_text(gulliver_ngrams, gulliver_propl,
                                    500, 11)
        print(f"[{i}] Text #{i}:")
        print_text(gulliverick)
    del gulliver_propl

    ngrams_combo = make_ngrams([mobydick_path], 4)
    mobydick_ngrams = ngrams_combo[0]
    mobydick_propl = ngrams_combo[1]
    del ngrams_combo

    # system('clear')
    # for i in range(1, 21):
    #     mobydericks = generate_text(mobydick_ngrams, mobydick_propl,
    #                                 500, 11)
    #     print(f"[{i}] Text #{i}:")
    #     print_text(mobydericks)
    # del mobydick_propl

    # ngrams_combo = make_ngrams([huckle_path], 4)
    # huckle_ngrams = ngrams_combo[0]
    # huckle_propl = ngrams_combo[1]
    # del ngrams_combo

    # system('clear')
    # for i in range(21, 51):
    #     hucklectic = generate_text(huckle_ngrams, huckle_propl,
    #                                300, 11)
    #     print(f"[{i}] Text #{i}:")
    #     print_text(hucklectic)
    # del huckle_propl

    # print_ngrams(test_ngrams, 100)
    # print_ngrams(gulliver_ngrams, 100)
    # print_ngrams(mobydick_ngrams, 100)
    # print(len(gulliver_ngrams))
    # print(len(mobydick_ngrams))
    # print("\n")
