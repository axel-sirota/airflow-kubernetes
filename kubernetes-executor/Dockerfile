FROM quay.io/astronomer/ap-airflow:latest-onbuild
RUN apk add --no-cache --virtual .build-deps  python3-dev libffi-dev gcc musl-dev make
RUN pip install --no-cache-dir  gevent
RUN apk del .build-deps
RUN mkdir -p $AIRFLOW_HOME/data
COPY include/data.csv $AIRFLOW_HOME/data/data.csv
COPY include/sql $AIRFLOW_HOME
COPY dags $AIRFLOW_HOME
COPY airflow_settings.yaml $AIRFLOW_HOME/airflow_settings.yaml

# Tuneos para que les ande rapido! Robenselos todos! :D

ENV AIRFLOW__SCHEDULER__MIN_FILE_PROCESS_INTERVAL=60
ENV AIRFLOW__SCHEDULER__SCHEDULER_MAX_THREADS=3
ENV AIRFLOW__WEBSERVER__WORKERS=9
ENV AIRFLOW__WEBSERVER__WORKER_REFRESH_INTERVAL=1800
ENV AIRFLOW__WEBSERVER__WEB_SERVER_WORKER_TIMEOUT=300
ENV AIRFLOW__WEBSERVER__WORKER_CLASS="gevent"
