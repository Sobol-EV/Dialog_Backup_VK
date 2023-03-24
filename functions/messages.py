
from auth import vk_api, asctime, sleep


def get_count_massage(pr_id):
    """Функция получения количества сообщений"""
    dialogs = vk_api('messages.getHistory', peer_id=pr_id, v="5.126")
    print(f"{asctime()} - С ПОЛЬЗОВАТЕЛЕМ id {pr_id} НАЙДЕНО:{dialogs['count']}  (сообщ.)")
    return dialogs["count"] // 200, dialogs["count"] % 200, dialogs["count"]


def get_dialogs(pr_id, ofs=0):
    """Функция получения сообщений из диалога (макс. 200 сообщений)"""
    dialogs = vk_api('messages.getHistory', peer_id=pr_id, count=200, offset=ofs, v="5.126")
    sleep(0.7)
    return dialogs["items"]


def get_dialogs_25(pr_id, arr_ofs):
    """Функция получения сообщений из диалога (макс. 5000 сообщений)"""
    try:
        vk_get_message_ids = vk_api("execute", v="5.126", code=f'''
        var pr_id = {pr_id};
        var arr_ofs = {arr_ofs};
        var arr_msg = [];
        var i = 0;
        while (i < arr_ofs.length){{
            arr_msg.push(API.messages.getHistory({{"peer_id":pr_id, "count":200, "offset":arr_ofs[i], "v":"5.126"}})["items"]);
            i = i + 1;
        }}
        return arr_msg;
        ''')
        return vk_get_message_ids
    except Exception as e:
        print("An error occurred: ", e)
        vk_get_message_ids = vk_api("execute", v="5.126", code=f'''
                var pr_id = {pr_id};
                var arr_ofs = {arr_ofs};
                var arr_msg = [];
                var i = 0;
                while (i < arr_ofs.length){{
                    arr_msg.push(API.messages.getHistory({{"peer_id":pr_id, "count":200, "offset":arr_ofs[i], "v":"5.126"}})["items"]);
                    i = i + 1;
                }}
                return arr_msg;
                ''')
        return vk_get_message_ids

