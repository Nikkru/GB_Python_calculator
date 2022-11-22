"""
Модуль взаимодействия пользователя с программой
"""


def view_data(data, title):
    print(f'{title} = {data}')


def view_data_lst(data, title):
    if data is str:
        print(f'{title} = {data}')
    else:
        calc = '+' if data[1] > 0 else '-'
        if data[1] != 0:
            print(f'{title} = {data[0]}{calc}{abs(data[1])}*i')
            return f'{data[0]}{calc}{abs(data[1])}*i'
        else:
            print(f'{title} = {data[0]}')
            return f'{data[0]}'

# метод получения строки вычисления


def get_calc_str():
    return input('введите требуемое вычисление: ').replace(' ', '')


def print_message(message):
    print(message)
