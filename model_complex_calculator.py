"""
Модуль Модель операций с комплексными числами
"""

x = [0, 0]
y = [0, 0]


def complex_sum():
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    real = a + c
    imaginary = b + d
    return [real, imaginary]


def complex_minus():
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    real = a - c
    imaginary = b - d
    return [real, imaginary]


def complex_mult():
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    real = a * c - b * d
    imaginary = b * c + a * d
    return [real, imaginary]


def complex_div():
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    real = (a * c + b * d) / (c ** 2 + d ** 2)
    imaginary = (b * c - a * d) / (c ** 2 + d ** 2)
    return [real, imaginary]


def init(comp_numb1, comp_numb2):
    global x
    global y
    x = comp_numb1
    y = comp_numb2


def do_it(culculation):
    if culculation == "+":
        return complex_sum()
    elif culculation == "-":
        return complex_minus()
    elif culculation == "*":
        return complex_mult()
    elif culculation == "/":
        return complex_div()