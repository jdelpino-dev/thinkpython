#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 5.3 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 5.3: Is Triangle?

from os import system
from bibth_general import integer_input, yes_or_no_input


def is_triangle(n1, n2, n3):
    if n1 > n2 + n3 or n2 > n1 + n3 or n3 > n1 + n2:
        return "No"
    else:
        return "Yes"


def input_is_triangle():
    cond = True
    while cond:
        system("clear")
        print("Let's see if your three lines could form a triangle!\n")
        n1 = integer_input(f"Introduce the lenght of side #1: ")
        n2 = integer_input(f"Introduce the lenght of side #2: ")
        n3 = integer_input(f"Introduce the lenght of side #3: ")
        answer = is_triangle(n1, n2, n3)
        print()
        if answer == "Yes":
            print(answer + "!, these three sides can form a triangle!\n")
        else:
            print(answer +
                  ". I'm sorry these three sides can't form a triangle...\n")
        stay_or_exit = yes_or_no_input("Do you want to try another " +
                                       "possible triangle? (Y/N)")
        if stay_or_exit == 'n':
            cond = False
    system("clear")


if __name__ == "__main__":
    system('clear')
    input_is_triangle()
