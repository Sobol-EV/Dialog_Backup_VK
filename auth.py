from requests import get
from time import asctime, sleep
from layouts.auth import sg, layout
from vk import Session, API


def authorization():
    """Функция обработки экрана авторизации"""
    window = layout()
    while True:
        event, values = window.read()
        if event == "Авторизация":
            jsn = get("https://api.vk.com/method/users.get",
                      params={
                              "access_token": values[0],
                              "v": 5.126
                              }).json()
            if isinstance(values[1], str):
                ogr_count = None
                if not values[1].isalpha():
                    ogr_count = values[1] if values[1] != "" else 2
            else:
                ogr_count = 2
                print(f"Т.к вы ввели неверное значение сообщений, количество будет равно 2")
            for key in jsn.keys():
                if key == "response":
                    vk_id = jsn['response'][0]['id']
                    first_name = jsn['response'][0]['first_name']
                    last_name = jsn['response'][0]['last_name']
                    print("Успешно!")
                    print(
                        f"{asctime()} - ПОЛЬЗОВАТЕЛЬ:{jsn['response'][0]['first_name']}  {jsn['response'][0]['last_name']}")
                    ac = values[0]
                    session = Session(access_token=ac)
                    api = API(session)
                    sleep(1)
                    window.close()
                    return api, vk_id, first_name, last_name, ac, ogr_count
                else:
                    print(f"{asctime()} - Авторизация не удалась! Попробуйте ещё раз.")
            if values[0] == "":
                print("Укажите токен!")
        if event == sg.WIN_CLOSED:
            window.close()
            break


vk_api, my_id, f_name, l_name, ac, message_count_limit = authorization()
