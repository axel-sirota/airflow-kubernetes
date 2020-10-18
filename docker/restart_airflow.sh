#!/usr/bin/env bash

docker-compose down
docker build -f docker/Dockerfile -t airflow-docker .
docker tag airflow-docker:latest localhost:5000/airflow-docker:latest
docker push localhost:5000/airflow-docker:latest
docker-compose up