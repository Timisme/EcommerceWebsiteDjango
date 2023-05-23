FROM django-ecommerce-website-base:latest

ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY . $APP_HOME

ENTRYPOINT ["sh", "/app/entrypoint.sh"]