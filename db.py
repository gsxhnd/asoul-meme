import sqlite3

conn = sqlite3.connect('example.db', check_same_thread=False)


def get_sql_connect():
    return conn


def init_sql():
    c = conn.cursor()
    c.execute('''create table if not exists meme_img
    (id  integer
        constraint meme_img_pk
            primary key autoincrement,
    url text,
    width int,
    height int);''')
    c.execute('''create table if not exists art_list
        (cv_id    int not null
        constraint art_list_pk
            primary key,
         cv_title text,
         cv_cover text);''')

    conn.commit()
    c.close()


def insert_art_list(art_data):
    c = conn.cursor()
    for i in range(len(art_data)):
        cv_id = art_data[i]["cv_id"]
        cv_title = art_data[i]["cv_title"]
        cv_cover = art_data[i]["cv_cover"]
        sql_row = "insert into art_list (cv_id, cv_title, cv_cover) values ({},'{}','{}');".format(cv_id, str(cv_title),
                                                                                                   str(cv_cover))
        c.execute(sql_row)
    conn.commit()
    c.close()


def insert_meme_img_list(img_list):
    c = conn.cursor()
    for i in range(len(img_list)):
        sql_row = "insert into meme_img (url,width, height) values ('{}',{},{});".format(img_list[i]["url"],
                                                                                         img_list[i]["width"],
                                                                                         img_list[i]["height"])
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


def get_img_list(offset=0, limit=10, order_by="id desc"):
    c = conn.cursor()
    sql_row = "SELECT *  from meme_img order by {} limit {} offset {}".format(order_by, limit, offset)
    curs = c.execute(sql_row)
    data = []
    for row in curs:
        d = {"id": row[0], "url": row[1], "width": row[2], "height": row[3]}
        data.append(d)
    curs.close()
    return data


def get_all_img():
    c = conn.cursor()
    sql_row = "SELECT url  from meme_img;"
    curs = c.execute(sql_row)
    imgs = []
    for row in curs:
        imgs.append(row[0])
    return imgs


if __name__ == '__main__':
    init_sql()
