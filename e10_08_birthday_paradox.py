#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 10.8 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 10.8: Birthday Paradox

from os import system
from random import randint
from e10_01_07_lists import has_duplicates


def random_day(year_type="not_leap"):
    if year_type == "leap":
        return randint(1, 366)
    else:
        return randint(1, 365)


def random_birthdays(n):
    birthdays = []
    for i in range(n):
        a_birthday = random_day()
        birthdays.append(a_birthday)
    return birthdays


def count_cases(n_simulations, group_size):
    cases = 0
    for i in range(n_simulations + 1):
        birthdays = random_birthdays(group_size)
        if has_duplicates(birthdays):
            cases += 1
    return cases


if __name__ == "__main__":
    system('clear')
    n_simulations = 1000
    group_size = 23
    n_cases = count_cases(n_simulations, group_size)
    probability = n_cases * 100 / n_simulations
    print(f"From {n_simulations} simulation(s), {n_cases} had at least one",
          "duplicate.")
    print(f"La probabilidad es del {probability}%.")
    print("\n")
