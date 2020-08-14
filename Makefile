all: mypy pylint bandit safety test radon

restart: down up


SERVICE_NAME = backend
SRC_DIR = /app/src


### Static code analizers, tests, and metrics
pylint:
	docker-compose run --rm $(SERVICE_NAME) pylint $(SRC_DIR)

bandit:
	docker-compose run --rm $(SERVICE_NAME) bandit -c bandit.yml -r $(SRC_DIR)

mypy:
	docker-compose run --rm $(SERVICE_NAME) mypy $(SRC_DIR)

safety:
	docker-compose run --rm $(SERVICE_NAME) safety check --full-report


test:
	docker-compose run --rm $(SERVICE_NAME) bash -c "pytest --cov=src tests"


### Docker build shortcuts
build:
	docker-compose build

build-prod:
	docker build -t weather:prod -f Dockerfile.prod .

images:
	docker images | grep thinks


### Compose shortcuts
up:
	docker-compose up -d

down:
	docker-compose down

sh:
	docker-compose run $(SERVICE_NAME) sh

logs:
	docker-compose logs -f
