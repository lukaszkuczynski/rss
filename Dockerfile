FROM luk/rpi-miniconda 
MAINTAINER Lukasz Kuczynski <kuczynskilukasz@gmail.com>

ENTRYPOINT python rss.py
WORKDIR /root/app
COPY app/requirements.txt /root/app/requirements.txt
RUN pip install -r requirements.txt

COPY app /root/app

