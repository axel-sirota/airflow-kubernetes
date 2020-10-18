#!/usr/bin/env bash

# Initiliase the metastore
airflow initdb

# Create admin user
airflow create_user -r Admin -u admin -f admin -l admin -p admin -e admin@gmail.com

# Store the connection

airflow connections --add --conn_id 'pyconar' --conn_type HTTP --conn_host 'https://eventos.python.org.ar'
airflow connections --add --conn_id 'slack_conn' --conn_type HTTP --conn_host 'https://hooks.slack.com/services' --conn_password "/TGY1U9PP0/B01CLU8CJQN/OQDmrMcoa9noomRHUrikKygm"
# Run the scheduler in background
airflow webserver &> /dev/null &

# Run the web server in foreground (for docker logs)
exec airflow scheduler
