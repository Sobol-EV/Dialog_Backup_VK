from layouts.loading import layout, sg
from auth import message_count_limit
from functions.utilits import dt_id_fio
from functions.users import get_actual_user


def loading():
    """Функциональность экрана загрузки"""
    window = layout()
    while True:
        event, values = window.read(timeout=10)
        act_us = get_actual_user(message_count_limit)
        act_us = dt_id_fio(act_us)
        if event == sg.WIN_CLOSED:
            window.close()
            break
        sp = []
        for key in act_us:
            sp.append(str(key) + " - " + str(act_us[key]))
        window.close()
        return sp, act_us
