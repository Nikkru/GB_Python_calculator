"""
Модуль связи интерфейса и модели
"""
import calc_string
import model_complex_calculator as cc
import model_real_calculator as rc
import calc_view
import logger as log


def button_click():
    calc_str = calc_view.get_calc_str()
    calc_str_list = calc_string.calc_list(calc_str)

    if 'i' in calc_str_list:
        res = 'Простите, операции с комплексными числами пока недотупны.'
        # log_res = calc_view.view_data_lst(result, "result")
        calc_view.print_message(res)
        log_str = calc_str
    else:
        if rc.is_bracket_ok(calc_str) == 0:
            while '(' in calc_str:
                calc_str = rc.bracket_expression(calc_str)
            res = rc.simple_expression(calc_str)
            result = round(float(res), 5)
            print("Результат вычисления: ", result)
        else:
            print('Несоответствие открытых и закрытых скобок')
        log_str = f'{calc_str} = {result}'

    log.log_operation(log_str)


if __name__ == '__main__':
    button_click()
