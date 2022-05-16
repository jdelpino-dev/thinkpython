#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Library with JMD functions / For "Think Python"
# Learning and experimentation with the book "Think Python" by Allen Downey
# Code by José Delpino

# General Library (by José Delpino)

from os import system


def print_grid(height, wide):
    """Print cuadruple grids with the form:
    + - - - - + - - - - +
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    + - - - - + - - - - +
    Each grid-area must be min 3X3, although.
    heigh and wide must be >=3."""
    if (height >= 3) and (wide >= 3):
        plus_sign = '+'
        minus_sign = '- '
        bar_sign = '|'
        space = ' '
        n_lines = height * 2
        h_pos = 1
        n_minus = wide - 2
        n_spaces_bar = (wide*2)-3
        while (h_pos < n_lines):
            if h_pos in (1, height, n_lines-1):
                line = plus_sign + ' ' + (minus_sign * n_minus)
                line = (line * 2) + plus_sign
                print(line)
            else:
                line = bar_sign + (space * n_spaces_bar)
                line = (line * 2) + bar_sign
                print(line)
            h_pos += 1


def integer_input(message):
    """Valida la entrada de un número entero y lo entrega."""
    while True:
        try:
            print(message)
            n_integer = int(input())
            return n_integer
        except ValueError:
            print('Error. Invalid value. Try again..')


def integer_range_input(message, ra_min, ra_max):
    """Valida la entrada de un número entero y lo entrega.
    Ofrece la opción de válida según un rango. En caso de que
    no haya mínimo o máximo se usa 'None'"""
    cond_func = False
    while not cond_func:
        entero = integer_input(message)
        # ¿Cumple rango mínimo?
        if (ra_min is not None and entero >= ra_min):
            cond_min = True
        elif ra_min is None:
            cond_min = True
        else:
            cond_min = False
        # ¿Cumple rango máximo?
        if (ra_max is not None and entero <= ra_max):
            cond_max = True
        elif ra_max is None:
            cond_max = True
        else:
            cond_max = False
        # Combina las dos condiciones.
        cond_func = cond_min and cond_max
        # Mensaje de error y reintento.
        if not cond_func:
            system('clear')
            print('Error. Invalid value. Try again..\n')
    return entero


def yes_or_no_input(mensaje):
    """Valida la entrada de un pregunta S/N"""
    condición = False
    while not condición:
        print(mensaje)
        respuesta = input()
        respuesta = (respuesta.strip()).lower()
        condición = respuesta in ('y', 'n')
        if not condición:
            system('clear')
            print('Error. Invalid value. Try again...\n')
    return respuesta


def is_between(x, y, z):
    '''Returns True if x ≤ y ≤ z or
    False otherwise.
    '''
    if x <= y <= z:
        return True
    else:
        return False


def add_to_dict(dict_of_list, key_d, element):
    if key_d in dict_of_list:
        dict_of_list[key_d].append(element)
    else:
        dict_of_list[key_d] = [element]
