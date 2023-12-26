### Run Employee self-service portal locally

pre-requisites:
- python 3.8
- pip
- virtualenv
- mysql database setup

1. install the required python packages
```bash
pip install -r requirements.txt
```
2. migrate the database
```bash
python manage.py migrate
```
3. run the server
```bash
python manage.py runserver
```
4. open the browser and go to http://localhost:8000

### Run Employee self-service portal in docker

pre-requisites:
- docker
- docker-compose

1. build the docker image
```bash
docker build -t essp:latest .
```
2. run the docker-compose for the database setup
```bash
docker-compose -f docker-compose-db.yml up -d
```
3. run the docker-compose for the application
```bash
docker-compose -f docker-compose.yml up -d
```
4. open the browser and go to http://localhost:8000

**you can change the configuration in the docker-compose.yml file according to your preference**

#### you can get full documentation about the project from [here](development_docs/documentation.md)