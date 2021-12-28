FROM python:3.6-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y postgresql gcc python3-dev musl-dev

RUN python3 -m pip install --upgrade pip
COPY ./requirements.txt .
RUN python3 -m pip install -r requirements.txt 

RUN apt-get install -y netcat

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]