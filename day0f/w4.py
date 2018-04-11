'''
线程创建的高级模块:threading
'''
import threading
import time

def myNewThread():
    print("the new thread is running")
    time.sleep(2)
    print("the new thread done")

if __name__ == '__main__':
    print("main is running")
    t = threading.Thread(target=myNewThread)
    t.start()
    t.join()
    print("all done")