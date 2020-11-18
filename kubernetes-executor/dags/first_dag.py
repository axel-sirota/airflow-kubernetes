from datetime import datetime, timedelta

from airflow import DAG
from airflow.contrib.operators.slack_webhook_operator import \
    SlackWebhookOperator
from airflow.hooks.base_hook import BaseHook
from airflow.sensors.http_sensor import HttpSensor

default_args = {
    "owner": "airflow",
    "start_date": datetime(2020, 10, 1),
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "axel.sirota@gmail.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

slack_token = BaseHook.get_connection("slack_conn").password

with DAG(dag_id="pycon_dag", schedule_interval="*/5 * * * *",
         default_args=default_args, catchup=False) as dag:
    esta_todo_bien = HttpSensor(
        task_id="ping_webpage",
        method="GET",
        http_conn_id="pyconar",
        endpoint="events/pyconar2020/",
        response_check=lambda response: 200 == response.status_code,
        poke_interval=5,
        timeout=20
    )

    sending_slack_notification = SlackWebhookOperator(
        task_id='sending_slack',
        http_conn_id='slack_conn',
        webhook_token=slack_token,
        message="Esta todo bien! \n Ahora toma un gatito! "
                "https://www.youtube.com/watch?v=J---aiyznGQ",
        username='airflow',
        icon_url='https://raw.githubusercontent.com/apache/'
                 'airflow/master/airflow/www/static/pin_100.png',
        dag=dag
    )

    esta_todo_bien >> sending_slack_notification

