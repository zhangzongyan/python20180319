'进程池'
from multiprocessing import Process, Pool
import time
import  os

def job(n):
    #print("the new process [%d] running, and the argument is [%d]" % (os.getpid(), n))
    #time.sleep(10)
    for i in range(2, n):
        if n % i == 0:
            return
    print("%d 是一个质数" % n)


if __name__ == '__main__':
    pl = Pool(5) #进程池对象,参数表示池中最大的进程数
    for i in range(300000, 300201):
        pl.apply_async(job, args=(i,)) # 异步向进程池中添加进程  异步:函数不阻塞,事件什么时候发生,以及发生后会是什么结果都是不一定的
        #print("i: %d" % i)
#    time.sleep(1000)
    pl.close() #不允许再向池中添加进程
    pl.join() # 等待进程池中所有的子进程终止
    print("all child process done")