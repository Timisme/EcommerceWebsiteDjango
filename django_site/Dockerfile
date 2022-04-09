FROM python:3.9-alpine

RUN pip install --upgrade pip 

COPY ./django_site /app
WORKDIR /app 

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]