ARG PYTHON_BASE_IMAGE="python:3.8-slim"
FROM ${PYTHON_BASE_IMAGE} as airflow-apt-deps-ci-slim
MAINTAINER axel.sirota@gmail.com

ENV AIRFLOW_HOME=/data/airflow
ENV PYTHONPATH=$AIRFLOW_HOME:$AIRFLOW_HOME/lib:$AIRFLOW_HOME/contrib
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
ENV INITRD No
ENV C_FORCE_ROOT true

WORKDIR /data/airflow

RUN apt-get update -yqq && apt-get install -yqq --no-install-recommends \
    libpq-dev \
    libssl-dev \
    nano \
    netcat \
    locales \
    build-essential \
    libsnappy-dev \
    default-libmysqlclient-dev \
    libkrb5-dev \
    libsasl2-dev \
    libssl-dev \
    libffi-dev \
    apt-utils libusb-1.0-0 \
    procps lsof strace ltrace \
    gnupg \
    rng-tools \
    git curl unzip zip wget ssh rsync

COPY requirements.txt ./
RUN pip install --upgrade pip && \
    useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow && \
    pip install --no-cache-dir apache-airflow[all]==1.10.12 --constraint ./requirements.txt


ADD ./dags $AIRFLOW_HOME/dags
ADD ./contrib $AIRFLOW_HOME/contrib
ADD ./docker/start_web.sh $AIRFLOW_HOME/start_web.sh


COPY ./docker/entrypoint.sh $AIRFLOW_HOME/entrypoint.sh
COPY ./airflow.cfg $AIRFLOW_HOME/airflow.cfg
RUN chmod +x ./entrypoint.sh
RUN chown -R airflow: ${AIRFLOW_HOME}

USER airflow

WORKDIR ${AIRFLOW_HOME}

EXPOSE 8080 5555 8793

ENTRYPOINT [ "./entrypoint.sh" ]

CMD ["scheduler"]
