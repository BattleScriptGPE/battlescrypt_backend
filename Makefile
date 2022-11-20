PROJECT_NAME	= fast-api

all:	up

image:
	@docker build -t fast-api-gpe:dev -f ./api/Dockerfile . 
	@docker build -t db-gpe:dev -f ./databases/Dockerfile . 

build:	image


down:
	@yes | docker-compose down -v

up:
	@docker-compose up -d

bash:	up
	@docker-compose exec $(PROJECT_NAME) bash

test:   up
	@docker-compose exec -T $(PROJECT_NAME) pytest



.PHONY:	all build up bash 
