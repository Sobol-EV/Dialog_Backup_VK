import PySimpleGUI as sg


def layout():
    """Графическое отображение экрана загрузки"""
    layout_load = [
        [sg.Text('ЗАГРУЗКА...', font='Any 18', pad=(240, 0 or (5, 5)))],
        [sg.Output(size=(75, 20), pad=(57, 0 or (5, 5)), text_color="Green", key='-OUTPUT-')]
    ]
    window = sg.Window('Загрузка', layout=layout_load)

    return window
