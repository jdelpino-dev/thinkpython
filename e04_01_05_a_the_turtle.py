#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 4.1 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 4.1: Using TurtleWorld

from os import system
from math import tan, pi
from turtle import Turtle, mainloop, screensize


def apothem(n, side_size):
    return side_size / (2*tan(pi/n))


def max_side(n):
    return int(((85*600)/100) * tan(pi/n))


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


def aprox_circle(t, radius):
    # Aprox de circle with a polygon of 100 sides:
    side_size = 2 * radius * tan(pi/100)
    polygon(t, n, side_size)


if __name__ == "__main__":
    system('clear')
    poly_mesures = polygon_input()
    n = poly_mesures[0]
    side_size = poly_mesures[1]
    screensize(600, 600)
    t = Turtle()
    polygon(t, n, side_size)
    mainloop()
