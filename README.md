# reana-demo-dask

## Usage

Install Dask and run workflow:

```console
helm install dask dask/dask --version 2023.1.0
reana-client -w dask
```

## Custom cluster configuration

```console
# uninstall helm if previously installed:
helm uninstall dask
```

Install Dask Operator, Dask cluster and run workflow:

```console
helm install --repo https://helm.dask.org --create-namespace -n dask-operator --generate-name dask-kubernetes-operator
k apply -f cluster.yaml
reana-client run -w dask
```

## Files

`distributed.py` contains some examples on how to retrieve logs and events from Dask.
