FROM ubuntu:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /django-bank/


RUN apt-get update && apt-get -y install pip

COPY requirements.txt /django-bank/requirements.txt
RUN pip install -r requirements.txt