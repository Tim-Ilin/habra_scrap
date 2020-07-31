FROM python:3.8-alpine
MAINTAINER Timofey Ilin

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN echo '0 0 1/1 * *    habra_parser.py' > /etc/crontabs/root
CMD ['crond', '-l 2', '-f']