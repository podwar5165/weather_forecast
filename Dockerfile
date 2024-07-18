FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV V Docerfile
ENV TZ=Europe/Moscow


RUN mkdir /code
WORKDIR /code
COPY . /code


RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn
