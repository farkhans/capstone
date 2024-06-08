FROM python:3.12.1

ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install -r requirements.txt

RUN chmod +x start.sh

CMD ["/start.sh"]