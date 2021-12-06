FROM python:3.9

RUN apt-get update && \
    apt-get install -y && \
    pip3 install daphne

COPY . /opt/pricey

WORKDIR /opt/pricey

RUN pip3 install -r /opt/pricey/requirements.txt

RUN pip3 install psycopg2

WORKDIR /opt/pricey/pricey

RUN python3 manage.py collectstatic

ENV DJANGO_ENV=dev
ENV DOCKER_CONTAINER=1

EXPOSE 9020

CMD ["daphne", "-b", "0.0.0.0", "-p", "9020", "pricey.asgi:application"]