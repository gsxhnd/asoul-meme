import db
import requests
from time import sleep


def download_img(img_urls):
    for i in range(len(img_urls)):
        file_name = str(img_urls[i]).split("/")[3]
        response = requests.get("https://" + img_urls[i])
        print("downloading img: ", file_name)
        open("./img/" + file_name, "wb").write(response.content)
        sleep(1)


if __name__ == '__main__':
    imgs = db.get_all_img()
    print("download images count", len(imgs))
    download_img(imgs)
