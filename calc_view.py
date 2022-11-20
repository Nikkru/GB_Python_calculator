"""
Модуль взаимодействия пользователя с программой
"""


def view_data(data, title):
    print(f'{title} = {data}')


def view_data_lst(data, title):
    calc = '+' if data[1] > 0 else '-'
    if data[1] != 0:
        print(f'{title} = {data[0]}{calc}{abs(data[1])}*i')
        return f'{data[0]}{calc}{abs(data[1])}*i'
    else:
        print(f'{title} = {data[0]}')
        return f'{data[0]}'


def get_value():
    return input('введите числоЖ ')


def get_op():
    return input('введите вычисление (+, -, *, /): ')