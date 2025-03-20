FROM python:3.12-alpine

LABEL authors="Ckala"

WORKDIR /src

COPY ./src/requirements.txt .

RUN apk --update add mc curl curl bash nano
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/ap

#ENV TZ = Europa/Moscow
#CMD ["timedatectl", "set-timezone", "Europe/Moscow"]
