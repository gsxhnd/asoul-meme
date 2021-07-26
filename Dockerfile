FROM centos:centos8

MAINTAINER gsxhnd <gsxhnd@gmail.com>

WORKDIR /app

ADD ./* /app/

RUN pip3 install -r requirements.txt