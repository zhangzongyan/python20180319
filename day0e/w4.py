'''进程池'''
from multiprocessing import Pool
import time
import os
import random

def child_job(s):
    start = time.time() #时间戳
    print("the new process [%s] running and the pid [%d]" % (s, os.getpid()))
    time.sleep(random.random())
    end = time.time()
    print("the new process [%s] will be done, times:%f" % (s,(end-start)))

if __name__ == '__main__':
    p = Pool()
    for i in range(5):
        p.apply_async(child_job, args=(i,))
    p.close()
    p.join()
    print("main end")


