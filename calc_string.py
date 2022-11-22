"""
Модуль распознавания строки как арифметического вычисления
"""

signs_list = ['+', '-', '*', '/', '(', ')']

# вычисление первого числа


def previous_digit(string_expression, position):
    position -= 1
    previous = ''
    while position >= 0 and not string_expression[position] in signs_list:
        previous = string_expression[position] + previous
        position -= 1
    if string_expression[position] == '-':
        previous = '-' + previous
    return previous

# Вычисление числа справа от указанной позиции


def next_digit(string_expression, position):
    position += 1
    next_digit = ''
    while position <= len(string_expression)-1 and not string_expression[position] in signs_list:
        next_digit = next_digit + string_expression[position]
        position += 1
    return next_digit

# вычисление членов и знаков вычисления


def find_calc_operands(string_expression):
    a = 0
    b = 0
    sing = ''
    for i in signs_list:
        if i in string_expression:
            sing = i
            break
    pos = string_expression.index(sing)
    a = previous_digit(string_expression, pos)
    b = next_digit(string_expression, pos)
    return a, b, sing
