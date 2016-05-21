# MacDash

## Running on OS X
#### Beginning steps for running with PostgreSQL on OSX
Download Postgres.app for OSX from http://postgresapp.com
Follow the setup instructions that page to add postgres to your $PATH.

### Change working directory to web
```
cd web
```
If you're using `virtualenv` activate it at this point

### Install Requirements
```
pip install -r requirements.txt
```

### Create the SQLite3 Database and Migrate to 
Create Tables(temporary)
```
python manage.py migrate
```

### Create a super user
```
python manage.py createsuperuser
```

### Run the built in server
```
python manage.py runserver
```

## Running with Docker
These instructions are based on using `docker-machine` and `docker-compose` while running locally. The `docker-machine` command may be different based on where you deploy this docker image.

### Create the docker-machine
```
docker-machine create -d virtualbox macdash
```

### Build the docker containers
```
docker-compose build
```

### Start docker containers
```
docker-compose up -d
```

### Create the Database and Superuser
This should only be done on first initial build
```
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

