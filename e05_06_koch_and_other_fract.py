#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 5.6 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 5.6: Koch Curve and Other Fractals

from os import system
from turtle import Turtle, mainloop, Screen
from math import sqrt


def koch_curve(t, lenght):
    '''Máx lenght 95% of screen-side.
    '''
    t.pendown()
    if lenght < 3:
        t.fd(lenght)
    else:
        koch_curve(t, lenght/3)
        t.lt(60)
        koch_curve(t, lenght/3)
        t.rt(120)
        koch_curve(t, lenght/3)
        t.lt(60)
        koch_curve(t, lenght/3)


def center_koch(t, lenght):
    moving_a = ((lenght/3)*2 + (lenght/6)) + 5
    t.seth(180)
    t.penup()
    t.fd(moving_a)


def snow_flake(t, lenght):
    '''Máx lenght 82% of screen-side.
    '''
    for i in range(3):
        koch_curve(t, lenght)
        t.rt(120)


def center_snow_flake(t, lenght):
    center_koch(t, lenght)
    s_height = sqrt(((lenght/3)**2) - ((lenght/6)**2))
    moving_a = (s_height/2) + lenght*14.9/100
    t.penup()
    t.seth(90)
    t.fd(moving_a)


def quadratic_curve_type1(t, lenght):
    '''Máx lenght ¿?% of screen-side.
    '''
    t.pendown()
    if lenght < 3:
        t.fd(lenght)
    else:
        quadratic_curve_type1(t, lenght/3)
        t.lt(90)
        quadratic_curve_type1(t, lenght/3)
        t.rt(90)
        quadratic_curve_type1(t, lenght/3)
        t.rt(90)
        quadratic_curve_type1(t, lenght/3)
        t.lt(90)
        quadratic_curve_type1(t, lenght/3)


def quadratic_curve_type2(t, lenght):
    '''Máx lenght ¿?% of screen-side.
    '''
    t.pendown()
    if lenght < 4:
        t.fd(lenght)
    else:
        quadratic_curve_type2(t, lenght/4)
        t.lt(90)
        quadratic_curve_type2(t, lenght/4)
        t.rt(90)
        quadratic_curve_type2(t, lenght/4)
        t.rt(90)
        quadratic_curve_type2(t, lenght/4)
        quadratic_curve_type2(t, lenght/4)
        t.lt(90)
        quadratic_curve_type2(t, lenght/4)
        t.lt(90)
        quadratic_curve_type2(t, lenght/4)
        t.rt(90)
        quadratic_curve_type2(t, lenght/4)


def center_quadratic(t, lenght):
    moving_a = lenght/2
    t.seth(180)
    t.penup()
    t.fd(moving_a)


if __name__ == "__main__":
    system('clear')
    screen_side = 700
    drawing_area = Screen()
    drawing_area.setup(width=screen_side, height=screen_side)
    t = Turtle()
    t.ht()
    t.speed("fastest")
    lenght = 670
    t.penup()
    t.goto(0, 0)
    # center_koch(t, lenght)
    center_quadratic(t, lenght)
    t.seth(0)
    quadratic_curve_type2(t, 600)
    # koch_curve(t, lenght)
    # center_snow_flake(t, lenght)
    # snow_flake(t, lenght)
    # cesaro_curve_80(t, lenght)
    mainloop()
    system("clear")
