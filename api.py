from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request
from flask_cors import CORS

import art_detail
import art_list
import db

app = Flask(__name__)
CORS(app)


def tick():
    db_art_list = []
    new_art_list = []
    miss_cv_detail_list = []
    db_art = db.get_art_list()
    new_art = art_list.get_arts_data()

    for i in range(len(db_art)):
        db_art_list.append(db_art[i]["cv_id"])

    for i in range(len(new_art)):
        new_art_list.append(new_art[i]["cv_id"])

    miss_cv_list = compare_list(db_art_list, new_art_list)

    for i in range(len(miss_cv_list)):
        for cv_index in range(len(new_art)):
            if new_art[cv_index]["cv_id"] == miss_cv_list[i]:
                miss_cv_detail_list.append(new_art[cv_index])

    for i in range(len(miss_cv_detail_list)):
        html_data = art_detail.get_art_detail_data(miss_cv_detail_list[i]["cv_id"])
        new_img_list = art_detail.paser_art_detail_data(html_data)
        db.insert_meme_img_list(new_img_list)
        db.insert_art_list([miss_cv_detail_list[i]])


def compare_list(old, new):
    new_list = []
    for n_id in range(len(new)):
        if new[n_id] not in old:
            new_list.append(new[n_id])
    return new_list


@app.route("/", methods={"GET"})
def hello_world():
    page = request.args.get("page")
    limit = request.args.get("limit")
    offset = 0
    if page is None:
        page = 1
    if limit is None:
        limit = 10
    if int(page) > 1:
        offset = (int(page) - 1) * int(limit)

    res = db.get_img_list(limit=int(limit), offset=offset)
    print(page)
    print(limit)
    return {"data": res}


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'cron', hour=23, minute=0)
    scheduler.start()
    print("start api server in 8000")
    app.run(host="0.0.0.0", port=8000, debug=False)
