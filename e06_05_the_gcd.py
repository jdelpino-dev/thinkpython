#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 6.5 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 6.5: The Greatest Common Divisor

from os import system


def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)


if __name__ == "__main__":
    system('clear')
    a, b = 9000, 240
    print(f"The greatest common divisor of {a} and {b} is",
          str(gcd(a, b)) + ".\n\n")
