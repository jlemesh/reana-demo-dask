import dask
import dask.distributed
import os
from dask.distributed import print

DASK_SCHEDULER_URI = os.getenv("DASK_SCHEDULER_URI", "tcp://127.0.0.1:8786")
client = dask.distributed.Client(DASK_SCHEDULER_URI)

ev = client.get_events("runtimes")
for e in ev:
  print(e)

dask_log = ""
for k, l in client.get_worker_logs().items():
  dask_log += "worker: " + k + "\n"
  for lvl, e in l:
    dask_log += e + "\n"

print(dask_log)

dask_log = ""
for k, l in client.get_scheduler_logs():
  dask_log += l + "\n"

print(dask_log)

print("done")
