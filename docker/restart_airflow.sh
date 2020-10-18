#!/usr/bin/env bash

docker stop airflow-pycon
docker rm airflow-pycon
docker build -f docker/Dockerfile -t airflow-docker .
docker run -p 8080:8080 -d --name airflow-pycon airflow-docker
