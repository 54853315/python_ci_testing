FROM python:3.8

RUN mkdir /app

ENV PYTHONIOENCODING=utf-8
ENV PYTHONPATH=/app
ENV PATH /usr/local/bin:$PATH

COPY requirements.txt /

RUN pip3 install -r /requirements.txt && rm /requirements.txt

COPY . /app
WORKDIR /app

ENV TZ=Asia/Shanghai