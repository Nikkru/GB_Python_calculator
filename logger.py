"""
Модуль с логированием действий программы
"""

from _datetime import datetime as dt
import time


def log_operation(data):
    time_ = dt.now().strftime('%H:%M:%S')
    with open('log\log.csv', 'a') as file:
        file.write('[{}]: {}\n'
                   .format(time_, data))