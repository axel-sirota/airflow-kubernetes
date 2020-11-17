# Base Image
FROM puckel/docker-airflow

ENV AIRFLOW_HOME=/usr/local/airflow
WORKDIR $AIRFLOW_HOME
RUN mkdir -p $AIRFLOW_HOME/data
COPY data.csv $AIRFLOW_HOME/data/data.csv
COPY start-airflow.sh $AIRFLOW_HOME/start-airflow.sh
COPY airflow.cfg $AIRFLOW_HOME/airflow.cfg
COPY sql $AIRFLOW_HOME
COPY requirements.txt ./requirements.txt
RUN pip install --user "apache-airflow[async,celery,crypto,jdbc,kubernetes,password,postgres,redis,slack]==1.10.12" --constraint ./requirements.txt
RUN mkdir -p $AIRFLOW_HOME/.kube
COPY config $AIRFLOW_HOME/.kube/config
USER root
RUN chmod +x $AIRFLOW_HOME/start-airflow.sh
RUN chown -R airflow:airflow $AIRFLOW_HOME
USER airflow
ENTRYPOINT ["/usr/local/airflow/start-airflow.sh"]
CMD [ "webserver" ]
