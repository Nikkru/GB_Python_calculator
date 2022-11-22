"""
Модуль Модель работы с реальными числами
"""

import calc_string

x = 0
y = 0


def r_div():
    return x / y


def r_mult():
    return x * y


def r_minus():
    return x - y


def r_sum():
    return x + y


def init(number1, number2):
    global x
    global y
    x = number1
    y = number2


def do_it(op):
    if op == "+":
        return r_sum()
    elif op == "-":
        return r_minus()
    elif op == "*":
        return r_mult()
    elif op == "/":
        return r_div()


def division_operation(string_expression):
    if '/' in string_expression:
        pos = string_expression.index("/")
        a = calc_string.previous_digit(string_expression, pos)
        b = calc_string.next_digit(string_expression, pos)
        result = float(a) / float(b)
        string_expression = string_expression[:pos - len(a)] + str(result) + string_expression[pos + 1 + len(b):]
    return string_expression

# Замена в строке двух чисел на их произведение для первой найденной операции умножения


def mult_operation(string_expression):
    if '*' in string_expression:
        position = string_expression.index("*")
        a = calc_string.previous_digit(string_expression, position)
        b = calc_string.next_digit(string_expression, position)
        result = float(a) * float(b)
        string_expression = \
            string_expression[:position - len(a)] + str(result) + string_expression[position + 1 + len(b):]
    return string_expression

# Замена в строке двух чисел на их сумму для первой найденной операции сложения


def sum_operation(string_expression):
    if '+' in string_expression:
        position = string_expression.index("+")
        a = calc_string.previous_digit(string_expression, position)
        b = calc_string.next_digit(string_expression, position)
        result = float(a) + float(b)
        string_expression = \
            string_expression[:position - len(a)] + str(result) + string_expression[position + 1 + len(b):]
    return string_expression

# Замена в строке двух чисел на их разность для первой найденной операции вычитания


def substraction_operation(string_expression):
    if '-' in string_expression:
        pos = string_expression[1:].index("-") + 1
        a = calc_string.previous_digit(string_expression, pos)
        b = calc_string.next_digit(string_expression, pos)
        result = float(a) - float(b)
        string_expression = string_expression[:pos - len(a)] + str(result) + string_expression[pos + 1 + len(b):]
    return string_expression

# Вычисление простого выражения (без скобок)


def simple_expression(string_expression):
    while '/' in string_expression:
        string_expression = division_operation(string_expression)
    while '*' in string_expression:
        string_expression = mult_operation(string_expression)
    while '+' in string_expression:
        string_expression = sum_operation(string_expression)
    while '-' in string_expression[1:]:
        string_expression = substraction_operation(string_expression)
    return string_expression

# Нахождение первого по приоритету вычисления в скобках и его арифметическая реализация


def bracket_expression(string_expression):
    left_pos = 0
    right_pos = 0
    for i in range(len(string_expression)):
        if string_expression[i] == '(': left_pos = i
        if string_expression[i] == ')':
            right_pos = i
            if left_pos == 0:
                left_part = ''
            else:
                left_part = string_expression[:left_pos]
            if right_pos == len(string_expression)-1:
                right_part = ''
            else:
                right_part = string_expression[right_pos + 1:]
            string_expression = left_part + simple_expression(string_expression[left_pos + 1:right_pos]) + right_part
            return string_expression
    return string_expression

# Проверка корректности скобок в выражении


def is_bracket_ok(string_expression):
    temp_count = 0
    for i in range(len(string_expression)):
        if string_expression[i] == '(':
            temp_count += 1
        if string_expression[i] == ')':
            temp_count -= 1
        if temp_count < 0:
            return temp_count
    return temp_count
