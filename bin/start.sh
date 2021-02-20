#!/bin/bash
docker-compose up -d db

sleep 30

docker-compose up -d back
docker exec -ti data_converter_back_1 pip3 install -r requirements.txt
docker exec -ti data_converter_back_1 python manage.py makemigrations
docker exec -ti data_converter_back_1 python manage.py migrate
docker logs -f data_converter_back_1
