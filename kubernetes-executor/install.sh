#!/usr/bin/env bash

new_version=$1

kubectl delete namespace airflow
kubectl create namespace airflow
docker build -t pycon-kubernetes:"$new_version" .
docker tag pycon-kubernetes:"$new_version" localhost:5000/pycon-kubernetes:"$new_version"
docker push localhost:5000/pycon-kubernetes:"$new_version"
helm install  airflow -n airflow --set images.airflow.repository=localhost:5000/pycon-kubernetes --set images.airflow.tag="$new_version" --set workers.persistence.enabled=true --set workers.persistence.size=10Mb astronomer/airflow --version 0.15.6
