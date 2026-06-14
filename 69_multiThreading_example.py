import threading
import time

def download():
    for i in range(5):
        print("Downloading...")
        time.sleep(1)

def upload():
    for i in range(5):
        print("Uploading...")
        time.sleep(1)

t1 = threading.Thread(target=download)
t2 = threading.Thread(target=upload)

t1.start()  # Starts the thread.
t2.start()

t1.join()    # Waits until the thread finishes.
t2.join()

print("All tasks completed")

""" 
When to Use Multithreading?

✅ File downloading

✅ Web scraping

✅ Network requests

✅ Chat applications

✅ Games

✅ Background tasks

✅ GUI applications
"""