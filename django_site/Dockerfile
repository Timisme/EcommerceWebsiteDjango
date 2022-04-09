FROM python:3.9-slim-buster

RUN pip install --upgrade pip 
RUN apt-get update
RUN apt-get install -y gcc 

COPY . /app
WORKDIR /app 

RUN pip install -r requirements.txt

# COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/app/entrypoint.sh"]