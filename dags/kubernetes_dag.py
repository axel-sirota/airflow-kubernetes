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

with DAG(dag_id="kubernetes_dag", schedule_interval="*/5 * * * *",
         default_args=default_args, catchup=False) as dag:
    say_hello_to_my_little_friend = kubernetes_pod_operator.KubernetesPodOperator(
        # The ID specified for the task.
        task_id='kubernetes_task',
        # Name of task you want to run, used to generate Pod ID.
        name='kubernetes_task',
        image='busybox',
        is_delete_operator_pod=True,
        cmds=['sh', '-c', 'echo "Hello, Kubernetes!" && sleep 30'],
        in_cluster=False,
        namespace='default',
        config_file="/usr/local/airflow/.kube/config"
    )

    sending_slack_notification = SlackWebhookOperator(
        task_id='sending_slack',
        http_conn_id='slack_conn',
        webhook_token=slack_token,
        message="Esta todo bien desde Kubernetes! \n Ahora toma un gatito! "
                "https://www.youtube.com/watch?v=J---aiyznGQ",
        username='airflow',
        icon_url='https://raw.githubusercontent.com/apache/'
                 'airflow/master/airflow/www/static/pin_100.png',
        dag=dag
    )

    say_hello_to_my_little_friend >> sending_slack_notification

