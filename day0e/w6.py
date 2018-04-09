'''
进程间通信:Queue  Pipe
'''
from multiprocessing import Queue,Process
import os

def writeQueue(myq):
    print("the write process running [%d]" % os.getpid())
    for i in ['hello', 'boys', 'girls', 'python']:
        myq.put(i)
def readQueue(myq):
    print("the read process running [%d]" % os.getpid())
    while True:
        print("read:")
        print("****%s****" % myq.get())

if __name__ == '__main__':
    q = Queue() #实例化队列对象,用户进程间通信
    pw = Process(target=writeQueue, args=(q,))
    pr = Process(target=readQueue, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate() #终止此进程
