# create make command to create new image using dockerfile
IMAGE_NAME=essp
IMAGE_TAG=latest
IMAGE_REPOSITORY=kosalama/essp

# Build image using dockerfile and tag it with image name and tag
build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
# command to tag image with repository name and tag
tag:
	docker tag $(IMAGE_NAME):$(IMAGE_TAG) $(IMAGE_REPOSITORY):$(IMAGE_TAG)
# command to push image to docker hub repository called kosalama/essp
push:
	docker push $(IMAGE_REPOSITORY):$(IMAGE_TAG)

# command to run image in container using compose file

# run the mysql container db
run-db:
	docker-compose -f docker-compose-db.yml up -d

down-db:
	docker-compose -f docker-compose-db.yml down

# run the essp container
run-essp:
	docker-compose -f docker-compose.yml up -d

down-essp:
	docker-compose -f docker-compose.yml down
