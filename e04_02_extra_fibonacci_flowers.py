#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 4.2 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Using exercise 4.2: Fibonacci Flowers!
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
    # t.lt(90)
    # t.fd(130)
    # t.penup()
    # t.lt(180)
    # t.fd(130)
    # t.seth(0)
    # t.pendown()
    n = 45
    flower(t, 30 + n, 3)
    flower(t, 50 + n, 5)
    flower(t, 80 + n, 8)
    flower(t, 130 + n, 13)
    flower(t, 210 + n, 21)
    flower(t, 30 + n, 21)
    flower(t, 50 + n, 13)
    flower(t, 80 + n, 8)
    flower(t, 130 + n, 5)
    flower(t, 210 + n, 3)
    mainloop()
