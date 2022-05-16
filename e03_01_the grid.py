#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 3.3 / "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 4.1-5: The Grid

from os import system

from bibth_general import integer_range_input, print_grid


system('clear')
print()
height = integer_range_input('Height?', 3, None)
print()
wide = integer_range_input('Wide?', 3, None)
print('\n'*2)
print_grid(height, wide)
print('\n'*3)
