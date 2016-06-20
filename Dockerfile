FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y npm && apt-get -y install sudo
RUN sudo apt-get install libmysqlclient-dev

RUN cd /home/ && mkdir codebase
WORKDIR /home/codebase
ADD requirements.txt /home/codebase

RUN pip install -r requirements.txt

ADD . /home/codebase/
