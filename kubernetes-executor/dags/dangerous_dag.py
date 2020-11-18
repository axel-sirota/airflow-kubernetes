from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    "owner": "airflow",
    "start_date": datetime(2020, 11, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "axel.sirota@gmail.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}


with DAG(dag_id="dangerous_dag",
         schedule_interval="@daily",
         start_date=datetime(2020, 11, 1),
         default_args=default_args,
         catchup=True) as dag:
    tasks = [DummyOperator(task_id=f"{i}") for i in range(10)]
    end = DummyOperator(task_id="none")
    tasks >> end
