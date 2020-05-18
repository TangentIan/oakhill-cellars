FROM python:3.7

ARG BUILD
ENV PYTHONUNBUFFERED 1
ENV WITH_DOCKER True
RUN apt-get update && apt-get install -y --no-install-recommends binutils libproj-dev gdal-bin python-dev python3-lxml \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code

# Install python dependencies
COPY Pipfile* ./
COPY install.sh .
RUN chmod +x ./install.sh
RUN ./install.sh

RUN mkdir /var/log/celery
RUN chmod 777 -R /var/log/celery
# COPY etc/supervisor/conf.d/. /etc/supervisor/conf.d/

COPY . /code/
