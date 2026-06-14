import threading
import time

def task1():
    for i in range(5):
        print("Task 1")
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2")
        time.sleep(1)

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()  #  Starts the thread.
t2.start()

t1.join()   #  Waits until the thread finishes.
t2.join()

print("Program Finished")