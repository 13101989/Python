FROM python:3.12.3-slim-bullseye

RUN apt-get update && apt-get install -y \
    zlib1g-dev \
    libjpeg-dev \
    libtiff-dev \
    libfreetype6-dev \
    liblcms2-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .