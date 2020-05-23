import threading
import time

def func():
    print('first')
    time.sleep(3)
    print('after')

x = threading.Thread(target=func)
x.start()
print(threading.activeCount())
print("main")