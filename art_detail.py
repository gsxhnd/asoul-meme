import re
import time
from time import sleep
import requests
from bs4 import BeautifulSoup
import db


def get_art_detail_url(cv_id):
    return "https://www.bilibili.com/read/cv{}".format(cv_id)


def get_art_detail_data(cv_id):
    url = get_art_detail_url(cv_id)
    res_data = requests.get(url)
    return res_data.text


def paser_art_detail_data(data):
    img_list = []
    soup = BeautifulSoup(data, "html5lib", from_encoding="utf-8")
    content = soup.find_all("div", attrs={"id": "article-content"})
    content_soup = BeautifulSoup(str(content[0]), "html5lib", from_encoding="utf-8")
    content_data = content_soup.find_all("img")
    for index in range(len(content_data)):
        if index != 0:
            img_list.append(re.sub("//", "", content_data[index]["data-src"]))
    return img_list


if __name__ == '__main__':
    art_list = db.get_art_list()
    art_list.reverse()
    for i in range(len(art_list)):
        print("get cv id: ", art_list[i])
        html_data = get_art_detail_data(art_list[i]["cv_id"])
        img_list = paser_art_detail_data(html_data)
        db.insert_meme_img_list(img_list)
        time.sleep(10)
