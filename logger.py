"""
Модуль с логированием действий программы
"""

from _datetime import datetime as dt
# from time import time


def log_operation(data):
    time = dt.now().strftime('%H:%M:%S')
    with open('log.csv', 'a') as file:
        file.write('[{}]: {}\n'
                   .format(time, data))