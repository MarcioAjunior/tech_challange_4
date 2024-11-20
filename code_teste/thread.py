from concurrent.futures import ThreadPoolExecutor
import signal
import time

def worker_task():
    print("Worker iniciado")
    time.sleep(5)
    print("Worker finalizado")

executor = ThreadPoolExecutor(max_workers=1)

def handle_exit(signum, frame):
    print("BBB")
    executor.shutdown(wait=False)
    exit(0)

signal.signal(signal.SIGINT, handle_exit)

executor.submit(worker_task)
while True:
    print("AAA")
    time.sleep(1)
