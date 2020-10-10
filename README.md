# Rate service

Rate service is a service that return the exchange rate between 2 currencies

## Installation

### Install and Run Postgres [Recommended to user docker](https://www.docker.com/)

### create a docker network to link the 2 containers

```bash
docker network create -d bridge flextock --subnet 10.0.0.0
```

### Run postgres server

```bash
docker run --network flextock --name postgres-server -p 5432:5432 -e POSTGRES_PASSWORD=admin@@1234 -d postgres
```

### Create new Database in the docker container

```bash
docker exec -it postgres-server bash

```

```bash
su - postgres
```

```bash
psql
```

```bash
CERATE ROLE admin WITH LOGIN;
```

```bash
\password admin;
```

```bash
CREATE DATABASE rates_db;
```

```bash
GRANT ALL PRIVILEGE ON DATABASE "rates_db" TO "admin";
```

### Install and Run Rate Service

Clone The repository

```bash
git clone https://github.com/ahmedmenaem/rate-service.git
```

```bash
cd rate-service
```

Use the package manager [pipenv](https://pypi.org/project/pipenv/) to install dependencies and create a virtualenv.

```bash
pipenv install
```

Run the service

```bash
pipenv run start
```

## Deployment

### create a docker network to link the 2 containers

```bash
docker network create -d bridge flextock --subnet 10.0.0.0
```

### build rate service

```bash
docker build -t rate-service:latest . -f ./infrastructure/Dockerfile
```

### run service

```bash
docker run -d --network flextock --name rate-service -p 8080:8080 -e POSTGRES_HOST="10.0.0.1" rate-service:latest
```
