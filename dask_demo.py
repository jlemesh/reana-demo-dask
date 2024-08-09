from time import sleep
import dask
import dask.array
import dask.distributed
import os
from dask.distributed import print

def my_task():
  print("dask_worker_log_msg", flush=True)
  dask.distributed.get_worker().log_event("runtimes", {"start": "1", "stop": "10"})
  # raise ValueError("my_task failed")
  return "some_dask_value"

print("sleeping", flush=True)
sleep(10)
print("done sleeping", flush=True)

DASK_SCHEDULER_URI = os.getenv("DASK_SCHEDULER_URI", "tcp://127.0.0.1:8786")
client = dask.distributed.Client(DASK_SCHEDULER_URI)
print(DASK_SCHEDULER_URI)

x = dask.array.random.random((10000, 10000), chunks=(1000, 1000))
print("x created", flush=True)
y = x + x.T
print("y created", flush=True)
z = y[::2, 5000:].mean(axis=1)
print("z created", flush=True)
print("computing", flush=True)
result = z.compute()
print(result)
future = client.submit(my_task)
print(future.result())
sleep(5)
ev = client.get_events("runtimes")
for e in ev:
  print(e, flush=True)
print(client.get_worker_logs(), flush=True)
print(client.get_scheduler_logs(), flush=True)
print("done", flush=True)
