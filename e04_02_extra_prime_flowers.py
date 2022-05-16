#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 4.2 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Using exercise 4.2: Prime Flowers!
# Check https://en.wikipedia.org/wiki/Overlapping_circles_grid

from os import system
from turtle import Turtle, mainloop, Screen
from e04_02_a_flowers import flower

if __name__ == "__main__":
    system('clear')
    screen_side = 600
    drawing_area = Screen()
    drawing_area.setup(width=screen_side, height=screen_side)
    t = Turtle()
    t.ht()
    t.speed("fastest")
    n = 45
    flower(t, 30 + n, 3)
    flower(t, 50 + n, 5)
    flower(t, 70 + n, 7)
    flower(t, 110 + n, 11)
    flower(t, 130 + n, 13)
    flower(t, 170 + n, 17)
    flower(t, 190 + n, 19)
    flower(t, 230 + n, 23)
    mainloop()
