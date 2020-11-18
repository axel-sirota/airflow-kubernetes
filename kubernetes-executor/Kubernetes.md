# Deployando Airflow a Kubernetes con KubernetesExecutor

0) `helm repo add astronomer https://helm.astronomer.io`
1) Buildear nuestra imagen de Airflow (ya tenemos por lo anterior)
1+) Pushearla a un registry local asi lo puede pullear K8s
2) `kubectl create namespace airflow`
3) Instalar en Helm

1-3) Desde el directorio kubernetes-executor

```
./install.sh "1.0.0"
```
Y esperar!

4) Agregar las Connections!
