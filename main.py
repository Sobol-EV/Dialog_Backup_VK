import PySimpleGUI as sg
import traceback
from basic import basic
from functions.messages import get_dialogs, get_count_massage, asctime, get_dialogs_25
from functions.save_messages import history
from functions.utilits import get_count_message_25
from functions.pars import gen_html_img


def main():
    try:
        window, act_us = basic()
        while True:
            event, values = window.read(timeout=100)
            if event == "Начать":
                target_id = values["-THEME-"].split(" ")[0]
                if values[1] != "":
                    name_file = values[1]
                else:
                    name_file = target_id + ".txt"
                count, ost, count_all = get_count_massage(target_id)
                arr_ofs, ost_dict = get_count_message_25(count_all)
                s_all = ""
                k = -1
                if arr_ofs:
                    for iter_ofs in arr_ofs:
                        msg_dlg = get_dialogs_25(target_id, iter_ofs)
                        i_msg = 0
                        if msg_dlg:
                            for m_msg in msg_dlg:
                                if m_msg:
                                    s_all += history(m_msg, k)
                                    print(f"{asctime()} - Загружено {iter_ofs[i_msg] + 200} сообщений из {count * 200 + ost} из диалога с " +
                                          act_us[int(target_id)])
                                    i_msg += 1
                            i_msg = 0
                if ost_dict:
                    s_all += history(get_dialogs(target_id, ost_dict["ofs"]), k)
                    print(f"{asctime()} - Загружено {count * 200 + ost} сообщений из {count * 200 + ost} из диалога с " +
                          act_us[int(target_id)])
                with open(name_file, 'w', errors='ignore') as f:
                    f.write(s_all)
                print(f"{asctime()} - Диалоги выгружены в файл: {name_file}")
                gen_html_img(name_file)
            if event == "Очистить":
                window['-OUT-'].update('')
            if event == sg.WIN_CLOSED:
                window.close()
                break
    except Exception as e:
        sg.popup('Ошибка:\n', print(traceback.format_exc()))


if __name__ == '__main__':
    main()

