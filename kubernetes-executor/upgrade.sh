#!/usr/bin/env bash

new_version=$1

docker build -t pycon-kubernetes:"$new_version" .
docker tag pycon-kubernetes:"$new_version" localhost:5000/pycon-kubernetes:"$new_version"
docker push localhost:5000/pycon-kubernetes:"$new_version"
helm upgrade  airflow -n airflow --set images.airflow.repository=localhost:5000/pycon-kubernetes --set images.airflow.tag="$new_version" --set workers.persistence.enabled=true --set workers.persistence.size=10Mb astronomer/airflow --version 0.15.6
