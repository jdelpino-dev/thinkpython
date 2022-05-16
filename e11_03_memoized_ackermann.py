#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 11.2 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 11.3: Memoized Ackermann

from os import system
from bibth_general import integer_range_input, yes_or_no_input
# from time import time

known = {
             (1, 0): 2, (1, 1): 3, (1, 2): 4, (1, 3): 5,
             (1, 4): 6, (1, 5): 7, (3, 4): 125, (2, 4): 11,
             (1, 4): 6, (4, 0): 13, (4, 1): 65533,
             (5, 0): 65533, (3, 3): 61, (3, 2): 29,
             (3, 1): 13
}


def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))


def ackermann_memo(m, n):
    global known
    if (m, n) in known:
        return known[(m, n)]
    elif m == 0:
        result = n + 1
    elif m == 1:
        result = n + 2
    elif m == 2:
        result = 2*n + 3
    elif m == 3:
        result = 8*(2**n) - 3
    elif m > 3 and n == 0:
        result = ackermann_memo(m - 1, 1)
    elif m > 3 and n > 0:
        new_n = ackermann_memo(m, n - 1)
        result = ackermann_memo(m - 1, new_n)
    known[(m, n)] = result
    return result


if __name__ == "__main__":
    system('clear')
    while True:
        print("The Ackermann Function", "\n")
        m = integer_range_input("Insert m", 0, None)
        n = integer_range_input("Insert n", 0, None)
        result = ackermann_memo(m, n)
        print(f"The value for Ackermann({m},{n}) is {result}.")
        print("\n")
        answer = yes_or_no_input("Do you want to calculate another" +
                                 "values? y/n: ")
        if answer == "n":
            break
        print("\n")
    print("\n\n")
