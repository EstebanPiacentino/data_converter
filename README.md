# Data Converter Website

### Development Installation (don't use docker for production)

1. Clone the repository (don't change folder name)

2. Copy .env.example file to .env and change the variables

3. Start the Docker containers Django + MySQL

```sh
./bin/start.sh
```

On the first time:

4. Create a superuser

```sh
docker exec -ti data_converter_back_1 python manage.py createsuperuser
docker exec -ti data_converter_back_1 python manage.py makemigrations backend
docker exec -ti data_converter_back_1 python manage.py migrate
```

Preview the page at: http://127.0.0.1:8000/


