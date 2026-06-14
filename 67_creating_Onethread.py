import threading

def greet():
    print("Hello from thread")

t = threading.Thread(target=greet)

t.start()