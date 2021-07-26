FROM python:3.8-alpine

MAINTAINER gsxhnd <gsxhnd@gmail.com>

WORKDIR /app

ADD ./* /app/

RUN pip3 install -r requirements.txt