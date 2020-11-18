#!/usr/bin/env bash

docker build -t pycon-java-example -f Dockerfile-java .
docker build -t pycon-python-example -f Dockerfile-python .
docker build -t pycon-spark-example -f Dockerfile-spark .
docker tag pycon-java-example:latest localhost:5000/pycon-java-example:latest
docker tag pycon-python-example:latest localhost:5000/pycon-python-example:latest
docker tag pycon-spark-example:latest localhost:5000/pycon-spark-example:latest
docker push localhost:5000/pycon-java-example:latest
docker push localhost:5000/pycon-python-example:latest
docker push localhost:5000/pycon-spark-example:latest
