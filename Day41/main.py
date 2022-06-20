from queue import Queue
import time
from threading import Thread



q = Queue(maxsize=0)
num_threads = 10

def do_stuff(q):
  while True:
    print(q.get())
    q.task_done()
    time.sleep(10)


for i in range(num_threads):
  thread = Thread(target=do_stuff, daemon=True, args=(q,))
  thread.start()

a = [123, 344, 4556, 23, 1, 0]
for x in a:
  q.put(x)

q.join()