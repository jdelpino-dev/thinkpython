#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 4.2 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Using exercise 4.2: Flowers Inside Flowers!
# Check https://en.wikipedia.org/wiki/Overlapping_circles_grid

from os import system
from math import radians, degrees, sin
from turtle import Turtle, mainloop, Screen
from e04_02_a_flowers import petal


def multiple_flower(t, radius, n_petals, n_flowers):
    petal_steps = float(360 / n_petals)
    arc_angle = 60 * n_flowers
    arc_angle2 = 60 * n_flowers
    if n_petals > 6:
        arc_angle = float(360 / n_petals)
        arc_angle2 = (180 - arc_angle) / 2
        arc_angle = n_flowers * arc_angle
        arc_angle = radians(arc_angle)
        arc_angle2 = radians(arc_angle2)
        radius = radius * (sin(arc_angle2) / sin(arc_angle))
        arc_angle = degrees(arc_angle)
        arc_angle2 = degrees(arc_angle2)
    initial_angle = 90 - (arc_angle / 2)
    angle_zero = initial_angle
    for i in range(n_petals):
        if i > 0:
            initial_angle = angle_zero + (i * petal_steps)
        petal(t, radius, arc_angle, initial_angle)


if __name__ == "__main__":
    system('clear')
    screen_side = 600
    drawing_area = Screen()
    drawing_area.setup(width=screen_side, height=screen_side)
    t = Turtle()
    t.ht()
    t.speed("fastest")
    multiple_flower(t, 100, 20, 3)
    mainloop()
