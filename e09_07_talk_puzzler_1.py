#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 9.7 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 9.7: Car Talk Puzzler I

from os import system
from e09_01_words import words


def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.

    word: string

    returns: bool
    """
    lenght = len(word)
    # Guardian 1: for words that contain less than 6 letters.
    if lenght < 6:
        return False
    # Search the triple doubles usind the variable doubles.
    doubles = 0
    i = 0
    while i < lenght:
        if word[i] == word[i+1]:
            # Counts one double letter and jump to the following
            # possible pair to continue the search.
            i += 2
            doubles += 1
            if doubles == 3:
                # Check if there is already three double letter.
                return True
        else:
            i += 1
            doubles = 0
        if (lenght - i) < (6 - 2*doubles):
            # Guardian 2: to stop the search when the rest of the
            # word is shorter than 6 letters.
            return False
    # After consuming all possibilities without finding the triple
    # double returns false.
    return False


if __name__ == "__main__":
    system('clear')
    file_name = "From the book/master/code/words.txt"
    the_words = words(file_name)
    for word in the_words:
        if is_triple_double(word):
            print(word)
    print("\n")
