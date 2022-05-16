#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 13.1-4 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 13.1-4: Book Works I: Book Histograms (Word Frequencies),
#                                and Book Comparison
#                                with Dictionary Subtraction


from os import system
from bibth3_strings import make_plain, no_space_nor_punctuation
from bibth3_dicts import invert_dict, size_dict_list  # , print_dict2
from bibth3_dicts import make_ddicts, add_to_dictlist
from bibth3_lists import print_list


def make_book_hist(filepath):
    the_file = open(filepath)
    hist = {}
    for line in the_file:
        if line[0] == "#":
            continue
        line = make_plain(line)
        line = line.split()
        i = 0
        while i < len(line):
            line[i] = no_space_nor_punctuation(line[i])
            i += 1
        for word in line:
            hist[word] = hist.get(word, 0) + 1
    return hist


def make_words_dict(filepath):
    return make_ddicts(filepath,
                       key_gen=lambda l: len(l),
                       items_gen=lambda k, l: (l, None),
                       value_adder=add_to_dictlist,
                       method="as_the_iterable")


def not_in_target(source: dict, target: dict) -> list:
    not_there = list()
    for word in source:
        lenght = len(word)
        if lenght in target:
            if word not in target[lenght]:
                not_there.append(word)
    not_there.sort()
    return not_there


def calc_total_words(hist: dict) -> int:
    values_list = hist.values()
    return sum(values_list)


def most_common(hist):
    t = list(hist.items())
    t.sort(key=lambda p: p[1], reverse=True)
    return t


if __name__ == "__main__":
    gulliver_path = "files/gulliver_s_travels.txt"
    mobydick_path = "files/moby_dick_or_the_whale.txt"
    english_path = "files/words_new.txt"

    gulliver_hist = make_book_hist(gulliver_path)
    mobydick_hist = make_book_hist(mobydick_path)
    english_dict = make_words_dict(english_path)

    system('clear')
    print(len(gulliver_hist), calc_total_words(gulliver_hist))
    print(len(mobydick_hist), calc_total_words(mobydick_hist))
    print("\n")

    freq_gulliver = invert_dict(gulliver_hist)
    freq_mobydick = invert_dict(mobydick_hist)

    print(size_dict_list(freq_gulliver))
    print(size_dict_list(freq_mobydick))

    # print("\n")
    # print_dict2(freq_gulliver, "frequency")
    # print_dict2(freq_mobydick, "frequency")
    # print("\n\n")

    gulliver_not_there = not_in_target(gulliver_hist, english_dict)
    mobydick_not_there = not_in_target(mobydick_hist, english_dict)

    # rint("\n")
    # print(len(gulliver_not_there))
    # print(len(mobydick_not_there))
    # print("\n\n")

    print_list(most_common(gulliver_hist)[:200], "frequency and word pair")
    print_list(most_common(mobydick_hist)[:200], "frequency and word pair")

    # print(gulliver_not_there)
    # print(mobydick_not_there)

    # print("\n")
    # print_dict2(freq_gulliver, "frecuency",
    #            with_items=True,
    #            sub_label="words")
    # print_dict2(freq_mobydick, "frecuency",
    #            with_items=True,
    #            sub_label="words")
    # print("\n\n")
