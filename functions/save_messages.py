from time import strftime, localtime


def repost(gt, k):
    """Сохраняет содержание репоста сообщения"""
    k += 1
    gl = ""
    for i in range(k):
        gl += "     "
    s_all = ""
    s_all += gl + "-----------------------\n"
    if "date" in gt.keys():
        s_all += gl + "Время размещения:" + "\n"
        s_all += gl + str(strftime("%m/%d/%Y, %H:%M:%S", localtime(gt["date"]))) + "\n"
    if "owner_id" in gt.keys():
        if gt["owner_id"] != "":
            s_all += gl + "Размещена на стене id" + str(gt['owner_id']) + "\n"
    if "from_id" in gt.keys():
        if gt["from_id"] != "":
            s_all += gl + "Автор записи id" + str(gt['from_id']) + "\n"
    if "text" in gt.keys():
        s_all += gl + "Текст репоста:" + "\n"
        gt["text"] = gt["text"].split("\n")
        for i in range(len(gt["text"])):
            s_all += gl + gt['text'][i] + "\n"
    if "attachments" in gt.keys():
        if gt["attachments"]:
            s_all += gl + "Вложения: \n"
            for j in range(len(gt["attachments"])):
                if "photo" in gt["attachments"][j].keys():
                    s_all += gl + "  Фото: \n"
                    s_all += gl + gt["attachments"][j]["photo"]["sizes"][-1]["url"] + "\n"
                if "audio" in gt["attachments"][j].keys():
                    s_all += gl + "  Аудио: \n"
                    s_all += gl + gt["attachments"][j]["audio"]["url"] + "\n"
                if "doc" in gt["attachments"][j].keys():
                    s_all += gl + "  Документ: \n"
                    s_all += gl + gt["attachments"][j]["doc"]["url"] + "\n"
                if "link" in gt["attachments"][j].keys():
                    s_all += gl + "  Ссылка: \n"
                    s_all += gl + gt["attachments"][j]["link"]["url"] + "\n"
                if "wall" in gt["attachments"][j].keys():
                    s_all += gl + "  РЕПОСТ ЗАПИСИ: \n"
                    s_all += gl + repost(gt["attachments"][j]["wall"], k)
                if "video" in gt["attachments"][0].keys():
                    s_all += gl + "  ВИДЕО: \n"
                    video = gt["attachments"][0]['video']
                    if "files" in video.keys():
                        if "hls_ondemand" in video["files"].keys():
                            s_all += str(video["files"]["hls_ondemand"])
                        if "hls"in video["files"].keys():
                            s_all += str(video["files"]["hls"])
    return s_all


def history(gt, k):
    """Сохраняет содержание сообщения"""
    k += 1
    gl = ""
    for i in range(k):
        gl += "     "
    s_all = ""
    if gt:
        for i in range(len(gt)):
            if i:
                s_all += gl + "-------------------------------------------\n"
                if "date" in gt[i].keys():
                    s_all += gl + str(strftime("%m/%d/%Y, %H:%M:%S", localtime(gt[i]["date"]))) + "\n"
                if "from_id" in gt[i].keys():
                    if "out" in gt[i].keys():
                        if gt[i]['out'] == 1:
                            s_all += gl + "От себя id" + str(gt[i]['from_id']) + "\n"
                        else:
                            s_all += gl + "От id " + str(gt[i]['from_id']) + "\n"
                    else:
                        s_all += gl + "От id " + str(gt[i]['from_id']) + "\n"
                if "text" in gt[i].keys():
                    s_all += gl + gt[i]['text'] + "\n"
                if "attachments" in gt[i].keys():
                    if gt[i]["attachments"]:
                        s_all += gl + "Вложения: \n"
                        for j in range(len(gt[i]["attachments"])):
                            if "photo" in gt[i]["attachments"][j].keys():
                                s_all += gl + "  Фото: \n"
                                s_all += gl + gt[i]["attachments"][j]["photo"]["sizes"][-1]["url"] + "\n"
                            if "audio" in gt[i]["attachments"][j].keys():
                                s_all += gl + "  Аудио: \n"
                                s_all += gl + gt[i]["attachments"][j]["audio"]["url"] + "\n"
                            if "sticker" in gt[i]["attachments"][j].keys():
                                s_all += gl + "  Стикер: \n"
                                s_all += gl + gt[i]["attachments"][j]["sticker"]["images"][-1]["url"] + "\n"
                            if "audio_message" in gt[i]["attachments"][j].keys():
                                s_all += gl + "  Аудиосообщение: \n"
                                s_all += gl + gt[i]["attachments"][j]["audio_message"]["link_mp3"] + "\n"
                            if "doc" in gt[i]["attachments"][j].keys():
                                s_all += gl + "  Документ: \n"
                                s_all += gl + gt[i]["attachments"][j]["doc"]["url"] + "\n"
                            if "link" in gt[i]["attachments"][j].keys():
                                s_all += gl + "  Ссылка: \n"
                                s_all += gl + gt[i]["attachments"][j]["link"]["url"] + "\n"
                            if "wall" in gt[i]["attachments"][j].keys():
                                s_all += gl + "  РЕПОСТ ЗАПИСИ: \n"
                                s_all += gl + repost(gt[i]["attachments"][j]["wall"], k)
                            if "video" in gt[i]["attachments"][0].keys():
                                s_all += gl + "  ВИДЕО: \n"
                                video = gt[i]["attachments"][0]['video']
                                if "files" in video.keys():
                                    if "hls_ondemand" in video["files"].keys():
                                        s_all += video["files"]["hls_ondemand"]
                                    if "hls" in video["files"].keys():
                                        s_all += video["files"]["hls"]
                if "fwd_messages" in gt[i].keys():
                    if gt[i]["fwd_messages"]:
                        s_all += gl + "ПЕРЕСЛАННЫЕ СООБЩЕНИЯ: \n"
                        s_all += gl + history(gt[i]["fwd_messages"], k)
                        s_all += gl + "КОНЕЦ ПЕРЕСЫЛАНЕМЫХ СООБЩЕНИЙ: \n"
        return s_all
