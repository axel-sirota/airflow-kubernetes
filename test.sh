#!/usr/bin/env bash

docker-compose down --rmi 'all'
sleep 10
docker-compose up --build