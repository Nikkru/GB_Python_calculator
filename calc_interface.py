"""
Модуль с интерфейсом программы
"""
calc_str = ''
str_num_1 = ''
str_num_2 = ''
str_calc = ''
complex = False


def init():
    global calc_str
    global str_num_1
    global str_num_2
    global str_calc
    global complex


def chec_str(num):
    if 'i' in num:
        return True  # комплексные
    return False  # рациональные


# def racional(num):
#     num = float(num)
#     return num


# def complex_parser(num):
#     num_1 = float(num[:num.index('+')].strip())
#     num_2 = float(num[num.index('+') + 1:-1].strip())
#     return num_1, num_2


# def input_num():
#     res_list = []
#     str_num_1 = input("введите первое число: ")
#     complex = complex_parser(str_num_1)
#     res_list.append(complex)
#     str_num_2 = input("введите второе число: ")
#     complex = complex_parser(str_num_2)
#     res_list.append(complex)
#     str_calc = input("введите вычисление: ")