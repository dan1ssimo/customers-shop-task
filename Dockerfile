FROM python:3.9

COPY . /app
WORKDIR /app

RUN apt update
RUN pip install -U pip wheel setuptools
RUN pip install -r requirements.txt
WORKDIR /app/task_2/

CMD ["python", "app.py"]
