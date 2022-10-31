FROM python:3.9

COPY . /app

RUN apt update
RUN pip install -U pip wheel setuptools
    
WORKDIR /app
RUN pip install -r requirements.txt
