FROM continuumio/miniconda3 
MAINTAINER Lukasz Kuczynski <kuczynskilukasz@gmail.com>

COPY app /root/app
WORKDIR /root/app
RUN pip install -r requirements.txt

ENTRYPOINT python rss.py