#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 4.2 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 4.2: Flowers
# Check https://en.wikipedia.org/wiki/Overlapping_circles_grid

from os import system
from math import sin, radians, degrees
from bibth_general import integer_range_input
from turtle import Turtle, mainloop, Screen
from bibth2_polygons_etc import arc


def radius_input(message, square_screen_side):
    # Validates the side_size of an aproximative circle-polygon acording to the
    # screen size.
    max_radius_lenght = int((square_screen_side / 2) * 85/100)
    cond = True
    while cond:
        radius = float(input(message + f" (max {max_radius_lenght}): "))
        if radius <= max_radius_lenght:
            cond = False
        else:
            print(f"Tamaño inválido. Ingrese un número menor que "
                  f"{max_radius_lenght}")
    return radius


def petal(t, radius, arc_angle, initial_angle):
    t.seth(initial_angle)
    for i in range(2):
        arc(t, radius, arc_angle)
        t.lt(180 - arc_angle)


def flower(t, radius, n_petals):
    petal_steps = float(360 / n_petals)
    arc_angle = 60
    arc_angle2 = 60
    if n_petals > 6:
        arc_angle = float(360 / n_petals)
        arc_angle2 = (180 - arc_angle) / 2
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
    radius = radius_input(f"Introduce the radius of the flower", 600)
    n_petals = integer_range_input("How many petals for the flower? (min 3): ",
                                   3, None)
    t = Turtle()
    t.ht()
    t.speed("fastest")
    # t.lt(90)
    # t.fd(radius)
    # t.penup()
    # t.lt(180)
    # t.fd(radius)
    # t.seth(0)
    t.pendown()
    flower(t, radius, n_petals)
    # t.seth(0)
    # t.penup()
    # t.seth(270)
    # t.fd(radius)
    # t.seth(0)
    # t.pendown()
    # t.circle(radius)
    # t.penup()
    # t.seth(90)
    # arc_angle = 360/n_petals
    # arc_angle2 = (180 - arc_angle) / 2
    # arc_angle = radians(arc_angle)
    # arc_angle2 = radians(arc_angle2)
    # smaller_radius = radius * (sin(arc_angle) / sin(arc_angle2))
    # t.fd(radius - smaller_radius)
    # t.seth(0)
    # t.pendown()
    # t.circle(smaller_radius)
    # t.ht()
    mainloop()
