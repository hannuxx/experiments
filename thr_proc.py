from threading import Thread
import time

def task():
    print("Sleeping for 1 second...")
    time.sleep(1)
    print("Done sleeping")

t = Thread(target=task)
t.start()
t.join()


