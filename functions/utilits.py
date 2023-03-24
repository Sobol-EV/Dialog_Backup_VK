from time import sleep, strftime, localtime
from auth import ac, get
from PIL import Image

from functions.users import get_fio


def dt_id_fio(id_list):
    """Функция создаёт словарь id:ФИ"""
    m = []
    m_id = []
    for i in range(len(id_list)):
        im_fam = get_fio(id_list[i][0])
        f_name = str(im_fam[0])
        sleep(0.5)
        l_name = str(im_fam[1])
        print(f"id {id_list[i][0]} - {f_name} {l_name} ({id_list[i][1]})")
        m.append(f_name + ' ' + l_name + " (" + str(id_list[i][1]) + ")")
        m_id.append(id_list[i][0])
    return dict(zip(m_id, m))


def get_time_message(t):
    """Функция превращения время в формат"""
    return strftime("%d:%m:%Y %H:%M", localtime(t))


def download_photo(url):
    """Функция скачивания изображения"""
    k = 0
    r = get(url, stream=True)
    filename = url.split("/")[-1]
    for i in range(len(filename)):
        if filename[i] == "?":
            k = 1
    if k == 1:
        filename = filename.split("?")[0]
    with open(filename, 'bw') as file:
        for chuk in r.iter_content(4096):
            file.write(chuk)
    return filename


def save_image(id):
    jsn = get("https://api.vk.com/method/users.get",
              params={
                "access_token": ac,
                "user_ids": id,
                "fields": "photo_100",
                "v": 5.126
                }).json()
    for key in jsn.keys():
        if key != "response":
            raise ValueError(f"Ошибка загрузки данных!")
    jsn = jsn['response'][0]['photo_100']
    im_name = download_photo(jsn)
    im = Image.open(im_name)
    im_name = im_name.split(".")[0]
    im_name = im_name + ".png"
    im.save(im_name)

    return im_name


def get_count_message_25(count_message):
    с_count_message = count_message // 200
    ost_count_message = count_message % 200
    arr_msg = []
    arr_msg_w = []
    ost_dict = {}
    for i in range(с_count_message):
        arr_msg.append(i*200)
    n = 0
    for i in range(1, (len(arr_msg) // 25) + 1):
        arr_msg_w.append(arr_msg[n:i*25])
        n = i*25
    if arr_msg[n:]:
        arr_msg_w.append(arr_msg[n:])
    if с_count_message == 0:
        if ost_count_message != 0:
            ost_dict["ofs"] = 0
            ost_dict["count"] = ost_count_message
    else:
        if ost_count_message != 0:
            ost_dict["ofs"] = arr_msg_w[-1][-1] + 200
            ost_dict["count"] = ost_count_message

    return arr_msg_w, ost_dict



