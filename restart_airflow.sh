#!/usr/bin/env bash

docker-compose down
sleep 10
docker-compose up --build -d --scale worker=4
