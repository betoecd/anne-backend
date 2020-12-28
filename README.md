# Anne backend ![Ann HM](https://static.wikia.nocookie.net/hmwikia/images/4/46/Ann_%28MM%29.png/revision/latest/scale-to-width-down/95?cb=20120707030207)

## Artificial Neural Network Environment
Repo for creating an API server in Django, using:
* GraphQL
* JWT
* MongoDB

## Initial Setup
Use the docker compose command to pull and configure the mongodb container
```bash
docker-compose up -d
```

Active virtual environment
```bash
pipenv shell
```

Install dependences
```bash
pipenv install
```

## Migrations
Run the following command to run startup migrations.
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
