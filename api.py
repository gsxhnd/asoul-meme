import time
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from apscheduler.schedulers.background import BackgroundScheduler

import art_detail
import art_list
import db


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        req = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(req.query)

        page = query["page"][0]
        limit = query["limit"][0]
        offset = 0
        if int(page) > 1:
            offset = (int(page) - 1) * int(limit)

        res = db.get_img_list(limit=limit, offset=offset)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(res).encode())


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


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'cron', hour=23, minute=0)
    scheduler.start()
    port = 8000
    httpd = HTTPServer(('127.0.0.1', 8000), HttpHandler)
    httpd.serve_forever()
