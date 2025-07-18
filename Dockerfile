FROM python:3.12.0-slim

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /opt/bbot
WORKDIR /opt/bbot

COPY . /opt/bbot/

RUN apt-get update && apt-get install -y curl \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

RUN chmod +x start.sh

CMD ["bash", "start.sh"]
