"""
Модуль распознавания строки как арифметического вычисления
"""

# Вычисление числа слева от указанной позиции


def previous_digit(string_expression, position):
    position -= 1
    previous = ''
    while position >= 0 and not string_expression[position] in ['+', '-', '*', '/', '(', ')']:
        previous = string_expression[position] + previous
        position -= 1
    if string_expression[position] == '-':
        previous = '-' + previous
    return previous

# Вычисление числа справа от указанной позиции


def next_digit(string_expression, position):
    position += 1
    next_digit = ''
    while position <= len(string_expression)-1 and not string_expression[position] in ['+', '-', '*', '/', '(', ')']:
        next_digit = next_digit + string_expression[position]
        position += 1
    return next_digit

# Замена в строке двух чисел на их частное для первой найденной операции деления


def division_operation(string_expression):
    if '/' in string_expression:
        pos = string_expression.index("/")
        b = previous_digit(string_expression, pos)
        f = next_digit(string_expression, pos)
        result = float(previous_digit(string_expression, pos)) / float(next_digit(string_expression, pos))
        string_expression = string_expression[:pos - len(b)] + str(result) + string_expression[pos + 1 + len(f):]
    return string_expression

# Замена в строке двух чисел на их произведение для первой найденной операции умножения


def mult_operation(string_expression):
    if '*' in string_expression:
        position = string_expression.index("*")
        b = previous_digit(string_expression, position)
        f = next_digit(string_expression, position)
        result = float(previous_digit(string_expression, position)) * float(next_digit(string_expression, position))
        string_expression = \
            string_expression[:position - len(b)] + str(result) + string_expression[position + 1 + len(f):]
    return string_expression

# Замена в строке двух чисел на их сумму для первой найденной операции сложения


def sum_operation(string_expression):
    if '+' in string_expression:
        position = string_expression.index("+")
        b = previous_digit(string_expression, position)
        f = next_digit(string_expression, position)
        result = float(previous_digit(string_expression, position)) + float(next_digit(string_expression, position))
        string_expression = \
            string_expression[:position - len(b)] + str(result) + string_expression[position + 1 + len(f):]
    return string_expression

# Замена в строке двух чисел на их разность для первой найденной операции вычитания


def substraction_operation(string_expression):
    if '-' in string_expression:
        pos = string_expression[1:].index("-") + 1
        b = previous_digit(string_expression, pos)
        f = next_digit(string_expression, pos)
        result = float(previous_digit(string_expression, pos)) - float(next_digit(string_expression, pos))
        string_expression = string_expression[:pos - len(b)] + str(result) + string_expression[pos + 1 + len(f):]
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
        if temp_count<0:
            return temp_count
    return temp_count

# тело программы


try:
    user_expression = \
        input("Введите выражение для вычисления значения (Можно использовать операции +, -, *, /): ").replace(' ', '')
    if is_bracket_ok(user_expression) == 0:
        while '(' in user_expression:
            user_expression = bracket_expression(user_expression)
        user_expression = simple_expression(user_expression)
        print("Результат вычисления: ", round(float(user_expression), 5))
    else:
        print('Несоответствие открытых и закрытых скобок')

except Exception as err:
    print('Возникла ошибка: ', str(err.args))