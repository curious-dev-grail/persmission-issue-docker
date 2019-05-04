uid:
	id -g

image: Dockerfile src
	docker build --build-arg uid=$$(id -g) --build-arg gid=$$(id -g) -t file-uploader .

container: docker-compose.yml
	docker-compose up -d fileService
