#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 12.1 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 12.1: Most Frequent

from os import system
from bibth3_strings import make_plain_with_accents as plain_string
from bibth3_strings import no_whitespace
from bibth3_dicts import print_dict, invert_dict


def make_texts_dict(filepath: str) -> dict:
    """Reads from a file and builds a dictionary of language tags that maps
    each language label to a list of strings/texts, written in that language.

    filename: string
    returns: map from language to texts
    """
    texts_by_language = dict()
    texts_file = open(filepath)
    for line in texts_file:
        bare_line = line.strip()
        if line[0:6] == "#LANG#":
            key = plain_string(line[6:-2])
            text_list = []
            texts_by_language[key] = text_list
        elif line[0:2] == "#[":
            pass
        elif bare_line:
            text_list.append(bare_line)
    return texts_by_language


def make_letters_histogram(filepath: str) -> dict:
    """Reads from a file and builds a dictionary of language tags that maps
    to a histogram of letters based on the strings/texts, written in that
    language, and inlcuded on the file.

    filename: string
    returns: map from language to texts
    """
    letters_by_language = dict()
    texts_file = open(filepath)
    for line in texts_file:
        bare_line = line.strip()
        if line[0:6] == "#LANG#":
            key = plain_string(line[6:-2])
            dicc_of_letters = {}
            letters_by_language[key] = dicc_of_letters
        elif line[0:2] == "#[":
            pass
        elif bare_line:
            bare_line = no_whitespace(bare_line.lower())
            for letter in bare_line:
                count = letters_by_language[key].get(letter, 0) + 1
                letters_by_language[key][letter] = count
    return letters_by_language


def calculate_frequencies(letters_by_language):
    dict_results = {}
    for language in letters_by_language:
        results = []
        dict_results[language] = results
        freq_dict = invert_dict(letters_by_language[language])
        frequencies = sorted(freq_dict, reverse=True)
        corpus_size = sum(frequencies)
        for freq in frequencies:
            percentage = str(round((freq*100/corpus_size), 2)) + "%"
            letters = freq_dict[freq]
            letters. sort()
            for letter in letters:
                results.append((letter, percentage))
    return dict_results


if __name__ == "__main__":
    system('clear')
    filepath = "files/freq_samples.txt"
    letters_by_language = make_letters_histogram(filepath)
    dict_results = calculate_frequencies(letters_by_language)
    print_dict(dict_results)
    print("\n\n")
