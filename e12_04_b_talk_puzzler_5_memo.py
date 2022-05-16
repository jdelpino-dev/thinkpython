#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 12.4 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 12.4: Car Talk Puzzler V: Reducible Words!

"""My undertake with problem is to create a recursive memoized function
as Allen Downey recommends. However, I add the idea that the recursion
must be performed a first time over the whole set in an ordered manner,
first with the shorter words. Memoizing everithing. In case you want to
add words to the database/file, the memo database must be updated at
the same time. A new word is going to affect the memos of bigger words
not of the smaller.

If you add a new one or two letter word,
that is going to produce a huge change on the memos database.

The memoized version finds the reducible words and delivers its dictionary
in 0.16706013679504395 seconds, while the non-memoized version finish
the same task in almost the same amount of time: 0.1425168514251709
seconds. This is because of the shallow nature of the reduction graphs
that natural language produces.
"""

from os import system
from bibth3_strings import make_plain
from bibth3_dicts import make_ddicts, add_to_ddicts, add_to_dictlist
from bibth3_dicts import search_by_key, search_by_sub_key
from bibth3_dicts import filter_ddicts, size_ddicts, find_the_n_longest
from time import time


def make_words_dict(filepath):
    return make_ddicts(filepath,
                       key_gen=lambda l: len(l),
                       items_gen=lambda k, l: [l, None],
                       value_adder=add_to_dictlist,
                       method="as_the_iterable")


def add_children(ddict: dict):
    for lenght in ddict:
        for word in ddict[lenght]:
            children = []
            for i in range(lenght):
                child = word[:i] + word[i+1:]
                if lenght-1 in ddict:
                    if child in ddict[lenght-1]:
                        children.append(child)
            add_to_ddicts(ddict, lenght, word, children,
                          value_adder=add_to_dictlist,
                          method="as_the_iterable")


def is_reducible(word: str, children: list, ddict: dict) -> bool:
    if len(word) == 1:
        return True
    if not children:
        return False
    for child in children:
        lenght = len(child)
        if is_reducible(child, ddict[lenght][child], ddict):
            return True
    return False


def find_reducible_words(words_and_children: dict) -> dict:
    return filter_ddicts(ddicts=words_and_children,
                         the_filter=lambda k, sd: True,
                         sub_filter=is_reducible,
                         value_adder=add_to_dictlist,
                         method="as_the_iterable")


def is_reducible_memo(word: str, children: list,
                      ddict: dict, reducible: dict) -> bool:
    word_lenght = len(word)
    if word_lenght in reducible:
        if word in reducible[word_lenght]:
            return True
    if word_lenght == 1:
        return True
    if not children:
        return False
    for child in children:
        lenght = len(child)
        if is_reducible_memo(child, ddict[lenght][child], ddict, reducible):
            return True
    return False


def find_reducible_words_memo(words: dict) -> dict:
    reducible = dict()
    lenghts_list = sorted(words.keys())
    for lenght in lenghts_list:
        word_group = words[lenght]
        for word in word_group:
            children = word_group[word]
            if is_reducible_memo(word, children, words, reducible):
                add_to_ddicts(reducible, lenght, word, children,
                              value_adder=add_to_dictlist,
                              method="as_the_iterable")
    return reducible


def print_word_list(words: list, word_label: str,
                    with_reductions=False,
                    reducible=[]):
    print("\n")
    n_words = len(words)
    if n_words == 1:
        prompt = (f"The {word_label} word is "
                  f"{words[0].upper()}\n")
        more_than_one = False
    else:
        prompt = (f"The {n_words} {word_label}(s) are:\n")
        more_than_one = True
    print(prompt)
    if more_than_one:
        n = 1
        for word in words:
            print(f"[{n}] ", word)
            n += 1
            if with_reductions:
                reductions = find_all_reductions(word, reducible)
                print_reductions(reductions)
    else:
        word = words[0]
        if with_reductions:
            reductions = find_all_reductions(word, reducible)
            print_reductions(reductions)
    print("\n")


def find_all_reductions(word: str, reducibles: dict) -> list:
    reductions = []
    word = make_plain(word)
    lenght = len(word)
    if lenght in reducibles:
        reducible_group = reducibles[lenght]
        if word in reducible_group:
            if len(word) == 1:
                reductions.append(word)
            children = reducible_group[word]
            n_children = len(children)
            for i in range(n_children):
                child = children[i]
                child_reductions = find_all_reductions(child, reducibles)
                n_child_reduc = len(child_reductions)
                for j in range(n_child_reduc):
                    reduction = [word]
                    reduc_items = child_reductions[j]
                    n_reduc_items = len(reduc_items)
                    for k in range(n_reduc_items):
                        reduction.append(reduc_items[k])
                    reductions.append(reduction)
    return reductions


def print_reductions(reductions: list):
    word = reductions[0][0].upper()
    n_reductions = len(reductions)
    if n_reductions == 0:
        have_reductions = False
        prompt = f"{word} doesn't have any reductions."
    else:
        have_reductions = True
    if n_reductions == 1:
        prompt = f"{word} doesn't have any reductions."
    else:
        prompt = f"The redutions of {word} are:"
    print(prompt, "\n")
    if have_reductions:
        n = 1
        for reduction in reductions:
            secuencia = ""
            index = 0
            for item in reduction:
                if index == 0:
                    secuencia += "| "
                secuencia += item
                if index < len(reduction)-1:
                    secuencia += " -> "
                else:
                    secuencia += " |"
                index += 1
            print(f"[{n}] ", secuencia)
            n += 1
    print("\n")


if __name__ == "__main__":
    system('clear')
    filepath = "files/words_new.txt"

    words_and_children = make_words_dict(filepath)
    add_children(words_and_children)

    t0 = time()
    reducible_words = find_reducible_words_memo(words_and_children)
    t = time()-t0

    n_keys, n_sub_keys, n_items = size_ddicts(reducible_words)
    print(n_keys, n_sub_keys, n_items, "\n")

    search_by_key(reducible_words, "lenghts", int)
    search_by_sub_key(reducible_words, "word", str, "children")

    print_word_list(find_the_n_longest(reducible_words, 10),
                    "longest reducible word",
                    with_reductions=True,
                    reducible=reducible_words)

    # print_word_list(find_the_n_longest(reducible_words, 1000),
    #                "longest reducible word")

    print(t)
