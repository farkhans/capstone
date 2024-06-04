FROM python:alpine

ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py migrate

RUN python manage.py runserver 0.0.0.0:8000
