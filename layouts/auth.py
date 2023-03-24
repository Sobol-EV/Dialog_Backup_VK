import PySimpleGUI as sg


def layout():
    """Графическая отображение экрана авторизации"""
    layout_auth = [
        [sg.Text('АВТОРИЗАЦИЯ', font='Any 15', pad=(235, 0 or (5, 5)))],
        [sg.Text('Токен:', font='Any 15'), sg.InputText(pad=(81, 0 or (5, 5)), size=(46, 0))],
        [sg.Text('Кол-во сообщ. от:', size=(15, 1), font='Any 13'), sg.InputText(size=(46, 1))],
        [sg.Output(size=(70, 0), pad=(70, 0 or (5, 5)), text_color="Green")],
        [sg.Submit("Авторизация", size=(40, 0), pad=(154, 0 or (5, 5)))]
    ]
    window = sg.Window('Авторизация', layout=layout_auth)
    return window


