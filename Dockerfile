FROM python:3.6-alpine

EXPOSE 5000
WORKDIR /home/app


COPY requirements.txt requirements.txt
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

COPY . /home/app
RUN chmod +x boot.sh

ENV FLASK_APP app

CMD ["./boot.sh"]