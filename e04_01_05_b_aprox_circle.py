#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 4.1 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 4.1: Aproximate a circle

from os import system
from math import tan, pi
from turtle import Turtle, mainloop, Screen


def apothem(n, side_size):
    return side_size / (2*tan(pi/n))


def max_side(n):
    return int(((85*600)/100) * tan(pi/n))


def circunference(radius):
    return 2 * pi * radius


def square(t, size):
    # Uses the turtle (t) to draw a square.
    center_polygon(t, size)
    t.pendown()
    for i in range(4):
        t.fd(size)
        t.lt(90)


def center_square(t, side_size):
    # Move the Turtle to a position so it could draw
    # a centered polygon.
    reloc_d = side_size / 2
    t.penup()
    t.lt(180)
    t.fd(reloc_d)
    t.lt(90)
    t.fd(reloc_d)
    t.lt(90)
    t.pendown()


def center_polygon(t, n, side_size):
    # Move the Turtle to a position so it could draw
    # a centered polygon.
    reloc_v = apothem(n, side_size)
    reloc_h = side_size / 2
    t.penup()
    t.lt(180)
    t.fd(reloc_h)
    t.lt(90)
    t.fd(reloc_v)
    t.lt(90)
    t.pendown()


def polygon(t, n, side_size):
    # Uses the turtle (t) to draw a polygon.
    angle = 360 / n
    center_polygon(t, n, side_size)
    t.pendown()
    for i in range(n):
        t.fd(side_size)
        t.lt(angle)


def polygon_input():
    # Validates the side_size of an n-polygon acording to the
    # screen size.
    n = int(input("How many polygon sides?: "))
    max_side_lenght = max_side(n)
    cond = True
    while cond:
        side_size = int(input(f"How big will the sides be (max "
                              f"{max_side_lenght})?:"))
        if side_size <= max_side_lenght:
            cond = False
        else:
            print(f"Tamaño inválido. Ingrese un número menor que "
                  f"{max_side_lenght}")
    return (n, side_size)


def aprox_circle_input():
    # Validates the side_size of an aproximative circle-polygon acording to the
    # screen size.
    max_radius_lenght = int(300 * 85/100)
    cond = True
    while cond:
        radius = int(input(f"Introduce the radius of the circle you want "
                           f"to aproximate (max {max_radius_lenght}): "))
        if radius <= max_radius_lenght:
            cond = False
        else:
            print(f"Tamaño inválido. Ingrese un número menor que "
                  f"{max_radius_lenght}")
    return radius


def aprox_circle(t, radius, n):
    # Aprox de circle with a polygon of 100 sides:
    side_size = 2 * radius * tan(pi/n)
    polygon(t, n, side_size)


if __name__ == "__main__":
    system('clear')
    screen_side = 600
    drawing_area = Screen()
    drawing_area.setup(width=screen_side, height=screen_side)
    radius = aprox_circle_input()
    n = int((circunference(radius)/4)+7)
    if n < 70:
        n = 70
    t = Turtle()
    aprox_circle(t, radius, n)
    mainloop()
