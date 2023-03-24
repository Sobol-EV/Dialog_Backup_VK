from auth import vk_api, asctime, sleep
from functions.messages import get_count_massage


def active_users(id_mas, ogr):
    """Функция получения актуальных пользователей"""
    m = []
    for i in range(len(id_mas)):
        if get_count_massage(id_mas[i])[2] > int(ogr):
            print(f"{asctime()} - C пользователем id {id_mas[i]} более {ogr} сообщений!")
            m.append(id_mas[i])
        else:
            print(f"{asctime()} - C пользователем id {id_mas[i]} менее {ogr} сообщений!")
        sleep(0.6)
    return m


def get_friends_id():
    """Функция получения списка id друзей"""
    friends = vk_api('friends.get', v="5.126")
    return friends["items"]


def get_fio(id):
    """Функция получения имени и фамилии"""
    fio = vk_api('users.get', user_ids=id, v="5.126")
    return fio[0]["first_name"], fio[0]["last_name"]


def get_friends_list_id(all: list):
    c_count_f = len(all) // 25
    ost_count_f = len(all) % 25
    start = 0
    arr = []
    if c_count_f:
        for i in range(1, c_count_f + 1):
            arr.append(all[start:i * 25])
            start += 25
    if ost_count_f:
        arr.append(all[start:])
    return arr


def get_count_msg_dialog_25(users, ac_value):
    vk_get_message_ids = vk_api("execute", v="5.126", code=f'''
    var users= {users};
    var arr_msg = [];
    var i = 0;
    var current_count = 0;
    while (i < users.length){{
        current_count = API.messages.getHistory({{"peer_id":users[i], "v":"5.126"}})["count"];
        if ({ac_value} <= current_count){{
            arr_msg.push([users[i],current_count]);
        }}
        i = i + 1;
    }}
    return arr_msg;
    ''')
    sleep(0.7)
    return vk_get_message_ids


def get_actual_user(actual_value):
    actual_users = []
    arr_user = get_friends_list_id(get_friends_id())
    for i in arr_user:
        response = get_count_msg_dialog_25(i, actual_value)
        if response:
            actual_users += response
    return actual_users
