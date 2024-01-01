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
- make

***use make commads to build and create the container as below***

1. build the image 
```bash
make build
```
2. run the db container command
```bash
make run-db
```
3. run the essp deployement command
```bash
make run-essp
```
4. open the browser and go to http://localhost:8000

**you can change the configuration in the docker-compose.yml file according to your preference**

#### you can get full documentation about the project from [here](development_docs/documentation.md)