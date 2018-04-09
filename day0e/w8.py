'''
 main进程创建一个新文件"./myprocess.txt",并写入"0"
   1) 创建20个进程,20个进程的任务都是将"./myprocess.txt"文件中的值读出来,+1写回去(覆盖之前的值)
   2) 当20个进程全部结束后,文件中的值为多少
'''
from multiprocessing import Process, Pool, Lock

import time, os

# 多个进程操作同一文件发生了竞争,如何解决使用进程的lock
# 将多进程/多线程发生进程的代码--->称为临界区  并发程序需要使得临界区同步
def newprocess(flname, mylock):
    #mylock.acquire() #加锁
    #time.sleep(1)
    with mylock: #推荐使用with语法锁,with语句结束块的时候,锁自然释放
        f = open(flname, "r+")
        fistline = f.readline()
        fistline = str(int(fistline) + 1)
        f.seek(0, 0)
        f.write(fistline)
        f.close()
    #mylock.release() #解锁

if __name__ == '__main__':
    f = open("./myprocess.txt", "w")
    f.write("0")
    f.close()
    #初始化锁对象
    mylock = Lock()
    # 创建一个进程池
   # p = Pool(20)
    pl = []
    for i in range(20):
        p = Process(target=newprocess, args=("./myprocess.txt", mylock))
        p.start()
        pl.append(p)
    for l in pl:
        l.join()
