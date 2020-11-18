from datetime import datetime, timedelta

from airflow import DAG
from airflow.contrib.operators import kubernetes_pod_operator
from airflow.contrib.operators.slack_webhook_operator import \
    SlackWebhookOperator
from airflow.hooks.base_hook import BaseHook

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

with DAG(dag_id="kubernetes_multilanguage_dag", schedule_interval="*/5 * * * *",
         default_args=default_args, catchup=False) as dag:
    first_python = kubernetes_pod_operator.KubernetesPodOperator(
        # The ID specified for the task.
        task_id='python',
        # Name of task you want to run, used to generate Pod ID.
        name='python',
        image='localhost:5000/pycon-python-example',
        is_delete_operator_pod=True,
        in_cluster=True,
        namespace='default'
    )

    second_java = kubernetes_pod_operator.KubernetesPodOperator(
        # The ID specified for the task.
        task_id='java',
        # Name of task you want to run, used to generate Pod ID.
        name='java',
        image='localhost:5000/pycon-java-example',
        is_delete_operator_pod=True,
        in_cluster=True,
        namespace='default'
    )

    third_spark = kubernetes_pod_operator.KubernetesPodOperator(
        # The ID specified for the task.
        task_id='spark',
        # Name of task you want to run, used to generate Pod ID.
        name='spark',
        image='localhost:5000/pycon-spark-example',
        is_delete_operator_pod=True,
        in_cluster=True,
        namespace='default'
    )

    sending_slack_notification = SlackWebhookOperator(
        task_id='sending_slack',
        http_conn_id='slack_conn',
        webhook_token=slack_token,
        message="Mira que DAG multilingue! Que te la das!! \n Ahora toma un gatito! "
                "https://www.youtube.com/watch?v=J---aiyznGQ",
        username='airflow',
        icon_url='https://raw.githubusercontent.com/apache/'
                 'airflow/master/airflow/www/static/pin_100.png',
        dag=dag
    )

    [first_python, second_java, third_spark] >> sending_slack_notification
