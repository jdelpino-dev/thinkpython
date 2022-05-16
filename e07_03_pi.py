#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 7.3 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 7.3: Pi and the Srinivasa Ramanujan's series

from os import system
from math import sqrt, factorial, pi


def pi_ramanujan(epsilon):
    factor = 2*sqrt(2)/9801
    sumtn = 0.0
    k = 0
    while True:
        sumtn_term = (factorial(4*k) * (1103 + 26390*k)) / ((factorial(k)**4) *
                                                            (396**(4*k)))
        sumtn += sumtn_term
        if sumtn_term < epsilon:
            break
        else:
            k += 1
    anti_pi = factor * sumtn
    pi_aprox = anti_pi**-1
    return pi_aprox


if __name__ == "__main__":
    system('clear')
    epsilon = 1e-15
    pi_aprox = pi_ramanujan(epsilon)
    print("According to python built in function π =", pi)
    print("Using Srinivasa Ramanujan's aproximation π =", pi_aprox)
    print("the dπ for this two values is", abs(pi_aprox - pi), "\n\n")
