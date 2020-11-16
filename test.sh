#!/usr/bin/env bash

AIRFLOW_HOME=$(pwd)
airflow initdb
airflow connections --add --conn_id 'data_path' --conn_type File --conn_extra '{ "path" : "data" }'
airflow connections --add --conn_id 'postgres' --conn_type Postgres --conn_host 'postgres' --conn_login 'airflow' --conn_password 'airflow' --conn_schema 'pluralsight'
airflow connections --add --conn_id 'slack_conn' --conn_type HTTP --conn_host 'https://hooks.slack.com/services' --conn_password "/TGY1U9PP0/B01E91SPC9E/mkIvO6L8vAnTJEHg0aUHanCT"
airflow connections --add --conn_id 'pyconar' --conn_type HTTP --conn_host 'https://eventos.python.org.ar' >/dev/null 2>&1
pytest
rm airflow.db
rm unittests.cfg
rm airflow.cfg
