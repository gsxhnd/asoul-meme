import time
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from apscheduler.schedulers.background import BackgroundScheduler

import db


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        req = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(req.query)

        page = query["page"][0]
        limit = query["limit"][0]
        res = db.get_img_list()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(res).encode())


def tick():
    art_list = db.get_art_list()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), " tick")


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), " tick")
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()
    port = 8000
    httpd = HTTPServer(('127.0.0.1', 8000), HttpHandler)
    httpd.serve_forever()
