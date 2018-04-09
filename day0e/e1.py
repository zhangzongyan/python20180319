
from multiprocessing import Process
import time
import  os

def job(n):
    time.sleep(1)
    print("the new process [%d] running, and the argument is [%d]" % (os.getpid(), n))
    for i in range(2, n):
        if n % i == 0:
            return
    print("%d 是一个质数" % n)

if __name__ == '__main__':
    l = []
    for i in range(300000, 300201):
        p = Process(target=job, args=(i,))
        p.start()
        l.append(p)
    for i in l:
        i.join()

