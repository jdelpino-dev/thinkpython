#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Library to plot polygons and other geometrical shapes
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino and Allen Downey

from math import tan, pi


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


def polyline(t, n, side_size, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(side_size)
        t.lt(angle)


def polygon(t, n, side_size):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    center_polygon(t, n, side_size)
    t.pendown()
    polyline(t, n, side_size, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


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
