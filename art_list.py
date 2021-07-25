import requests
from time import sleep

import db


def get_arts_url(pn, ps):
    url = "https://api.bilibili.com/x/space/article?mid=15073186&pn={}&ps={}&sort=publish_time&jsonp=jsonp".format(pn,
                                                                                                                   ps)
    return url


def parse_arts_data(data):
    arts_data = data["data"]["articles"]
    _arts_data = []
    for i in range(len(arts_data)):
        cv_id = arts_data[i]["id"]
        cv_title = arts_data[i]["title"]
        cv_cover = arts_data[i]["image_urls"][0]
        _arts_data.append({"cv_id": cv_id, "cv_title": cv_title, "cv_cover": cv_cover})
    return _arts_data


def get_arts_data():
    pn, ps = 1, 10
    arts_data = []
    url = get_arts_url(pn, ps)
    header = {
        "Referer": "https://space.bilibili.com/15073186/article"
    }
    res = requests.get(url, headers=header)
    json_data = res.json()
    json_data_count = json_data["data"]["count"]
    arts_data = arts_data + parse_arts_data(res.json())

    while pn * ps < json_data_count:
        sleep(1)
        pn += 1
        url = get_arts_url(pn, ps)
        res = requests.get(url, headers=header)
        p_data = parse_arts_data(res.json())
        arts_data = arts_data + p_data
    return arts_data


if __name__ == '__main__':
    art_data_list = get_arts_data()
    print(art_data_list)
    db.insert_art_list(art_data_list)
