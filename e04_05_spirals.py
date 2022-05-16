#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 4.5 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 4.5: Spirals!

from os import system
from math import pi, sin, cos
from turtle import Turtle, mainloop, Screen


def draw_coord_system(t, size):
    t.penup()
    t.goto(0, size)
    t.pendown()
    t.goto(0, -size)
    t.penup()
    t.goto(size, 0)
    t.pendown()
    t.goto(-size, 0)
    t.penup()
    t.goto(0, 0)


def draw_archimedean_spiral(t, final_theta, n, a, b, screen_side):
    """Draws an Archimedian spiral starting at the origin.

    Args:
      t: turtle
      final_theta: the final angle in radians
      n: how many line segments to draw
    """
    theta = 0.0
    increment = final_theta / n
    t.seth(0)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.penup()
    t.fd(a)
    t.pendown()
    i = 1
    while i <= n + 1:
        x = float((a + (b * theta)) * cos(theta))
        y = float((a + (b * theta)) * sin(theta))
        if abs(x) > screen_side or abs(y) > screen_side:
            i = n + 2
        else:
            t.goto(x, y)
            theta += increment
            i += 1


def draw_hyperbolic_spiral(t, initial_theta, final_theta, n, b, screen_side):
    """Draws an Hyperbolic spiral starting at the origin.

    Args:
      t: turtle
      final_theta: the final angle in radians
      n: how many line segments to draw
    """
    theta = initial_theta
    increment = final_theta / n
    t.seth(0)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    i = 1
    while i <= n + 1:
        x = float(b * cos(theta)/theta)
        y = float(b * sin(theta)/theta)
        if abs(x) > screen_side or abs(y) > screen_side:
            i = n + 2
        elif i == 1:
            t.penup()
            t.goto(x, y)
            t.pendown()
            theta += increment
            i += 1
        else:
            t.goto(x, y)
            theta += increment
            i += 1


if __name__ == "__main__":
    system('clear')
    screen_side = 700
    drawing_area = Screen()
    drawing_area.setup(width=screen_side, height=screen_side)
    t = Turtle()
    t.ht()
    t.speed("fastest")
    draw_coord_system(t, screen_side/2)
    draw_archimedean_spiral(t, final_theta=16*pi, n=5000, a=12, b=10,
                            screen_side=screen_side/2)
    # draw_hyperbolic_spiral(t, 1, final_theta=10*pi, n=5000, b=-400,
    #                       screen_side=screen_side/2)
    mainloop()
