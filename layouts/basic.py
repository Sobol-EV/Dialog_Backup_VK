from auth import my_id, f_name, l_name, sg
from functions.utilits import save_image


def layout(sp):
    """Графическое отображение основного экрана"""
    lay_basic = [[sg.Text('Пользователь', font='Any 15', pad=(280, 0 or (5, 5)))],
               [sg.Image(filename=save_image(my_id), pad=(300, 0 or (5, 5)))],
               [sg.Text(f'{f_name} {l_name}', font='Any 15', pad=(275, 0 or (5, 5)))],
               [sg.Output(size=(100, 10), pad=(0, 0 or (5, 5)), text_color="Green", key='-OUT-')],
               [sg.Text('Укажите куда сохранить: '), sg.InputText(pad=(0, 0 or (5, 5))),
                sg.FileBrowse("Выбрать", pad=(10, 0 or (5, 5)), file_types=(("Text Files", "*.txt"),))],
               [sg.Text('Укажите цель: ', size=(15, 1)),
                sg.Combo(sp, size=(43, 30), pad=(35, 0 or (5, 5)), key='-THEME-', readonly=True)],
               [sg.Button('Начать', size=(25, 1), pad=(100, 0 or (5, 5))), sg.Button('Очистить', size=(25, 1))]]

    window = sg.Window('VK MESSAGE SAVE', layout=lay_basic)
    return window
