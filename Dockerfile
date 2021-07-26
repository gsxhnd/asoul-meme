FROM python:3.8-alpine

MAINTAINER gsxhnd <gsxhnd@gmail.com>

WORKDIR /app

ADD ./* /app/

RUN pip3 install -r requirements.txt
RUN python3 db.py
RUN python3 art_list.py
RUN python3 art_detail.py
