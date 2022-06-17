FROM python:3.8.8

MAINTAINER xiaomai

ENV PYTHONUNBUFFERED 1
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

COPY pip.conf /root/.pip/pip.conf

RUN mkdir -p /usr/bin/EasyTest

WORKDIR /usr/bin/EasyTest

ADD . /usr/bin/EasyTest

RUN pip install -r requirements.txt
