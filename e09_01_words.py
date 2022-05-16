#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 9.1 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 9.1: Words.txt

from os import system


def words(file_name):
    words = open(file_name)
    for word in words:
        word = word.strip()
        yield word


def w_bigger_than(words, lenght):
    for word in words:
        if len(word) > lenght:
            print(word)


if __name__ == "__main__":
    file_name = "From the book/master/code/words.txt"
    system('clear')
    the_words = words(file_name)
    w_bigger_than(the_words, 20)
    print("\n")
    the_words = words(file_name)
    w_bigger_than(the_words, 19)
    print("\n\n")
