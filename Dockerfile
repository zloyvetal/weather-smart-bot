FROM python:3.8.5-alpine3.12

COPY ["requirements.txt", "requirements.dev.txt", "/app/"]

RUN apk add --no-cache --virtual build-deps \
        build-base \
        musl-dev \
        libffi-dev \
        openssl-dev \
    && pip install --no-cache-dir -r /app/requirements.dev.txt \
    && apk del build-deps

ENV PYTHONPATH "${PYTHONPATH}:/app/src"
WORKDIR /app
