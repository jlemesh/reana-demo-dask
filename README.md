# reana-demo-dask

```console
helm install dask dask/dask --version 2023.1.0
reeana-client -w dask
```

Custom cluster configuration:

```console
# uninstall helm if previously installed:
helm uninstall dask

helm install --repo https://helm.dask.org --create-namespace -n dask-operator --generate-name dask-kubernetes-operator
k apply -f cluster.yaml
reeana-client run -w dask
```

`distributed.py` contains some examples on how to retrieve logs and events from Dask.
