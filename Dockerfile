FROM python:3.7
ENV PYTHONUNBUFFERED 1

# Creating working directory
RUN mkdir /code && apt update && apt install -y python3-dev default-libmysqlclient-dev build-essential
WORKDIR /code

# Copying requirements
COPY requirements.txt /code/

# Install requirements
RUN pip install -r requirements.txt
COPY . /code/