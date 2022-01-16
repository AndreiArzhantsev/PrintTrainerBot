FROM python:3.8-slim-buster

WORKDIR /app
COPY deploy/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN chmod +x deploy/start.sh
CMD [ "deploy/start.sh" ]

