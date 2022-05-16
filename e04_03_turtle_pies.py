#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 4.3 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 4.3: Turtle Pies!
# Check https://en.wikipedia.org/wiki/Overlapping_circles_grid

from os import system
from math import sqrt
from turtle import Turtle, mainloop, Screen
from bibth2_polygons_etc import polygon, apothem


def angle_side(t, lenght, angle, direction):
    if direction == 'right':
        t.rt(180 - angle)
    else:
        t.lt(angle)
    t.fd(lenght)


def isoceles_triangle(t, base, equal_sides, base_angle, opposite_angle):
    angle_side(t, base, 0)
    angle_side(t, equal_sides, base_angle)
    angle_side(t, equal_sides, opposite_angle)


def angle_calculator_poly(t, n_sides):
    # Caculates the angles for the isoceles triangle
    # incribed on a n-polygon. It returns a tuple,
    # where the first element is the base angle
    # and the second one is the opposite one.
    base_angle = ((n_sides * 180) - 360) / (2 * n_sides)
    opposite_angle = 180 - (base_angle * 2)
    return (base_angle, opposite_angle)


def polygon_pie(t, n, side_size):
    polygon(t, n, side_size)
    angles = angle_calculator_poly(t, n)
    base_angle = angles[0]
    opposite_angle = angles[1]
    poly_angle = 360 / n
    longsides_len = sqrt((apothem(n, side_size) ** 2) + ((side_size / 2) ** 2))
    if n % 2 == 0:
        n_iter = n
    else:
        n_iter = n + 1
    n_iter = int(n_iter / 2)
    for i in range(n_iter):
        t.penup()
        t.fd(side_size)
        t.lt(poly_angle)
        t.pendown()
        angle_side(t, longsides_len, base_angle, 'left')
        angle_side(t, longsides_len, opposite_angle, 'right')
        t.lt(base_angle + poly_angle)


if __name__ == "__main__":
    system('clear')
    screen_side = 600
    drawing_area = Screen()
    drawing_area.setup(width=screen_side, height=screen_side)
    t = Turtle()
    t.ht()
    t.speed("fastest")
    polygon_pie(t, 9, 200)
    mainloop()
