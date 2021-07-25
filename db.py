import sqlite3

conn = sqlite3.connect('example.db')


def get_sql_connect():
    return conn


def insert_art_list(art_data):
    c = conn.cursor()
    for i in range(len(art_data)):
        cv_id = art_data[i]["cv_id"]
        cv_title = art_data[i]["cv_title"]
        cv_cover = art_data[i]["cv_cover"]
        sql_row = "insert into art_list (cv_id, cv_title, cv_cover) values ({},'{}','{}');".format(cv_id, str(cv_title),
                                                                                                   str(cv_cover))
        print(sql_row)
        c.execute(sql_row)
    conn.commit()
    c.close()


def insert_meme_img_list(img_list):
    c = conn.cursor()
    for i in range(len(img_list)):
        sql_row = "insert into meme_img (url) values ('{}');".format(img_list[i])
        c.execute(sql_row)
    conn.commit()
    c.close()


def get_art_list():
    c = conn.cursor()
    curs = c.execute("SELECT *  from art_list")
    data = []
    for row in curs:
        d = {"cv_id": row[0], "cv_title": row[1], "cv_cover": row[2]}
        data.append(d)
    curs.close()
    return data


def get_img_list(offset=0, limit=10):
    c = conn.cursor()
    sql_row = "SELECT *  from meme_img order by id desc  limit {} offset {}".format(limit, offset)
    curs = c.execute(sql_row)
    data = []
    for row in curs:
        d = {"id": row[0], "url": row[1]}
        data.append(d)
    curs.close()
    return data


if __name__ == '__main__':
    img_data = ["1", "2", "3"]
    # arts = get_art_list()
    # insert_meme_img_list(img_data)
    # imgs = get_img_list()
    # print(imgs)
