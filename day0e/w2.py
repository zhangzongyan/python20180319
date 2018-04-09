# 无论是什么os都支持的多进程模块
from multiprocessing import Process
import os
import time

def child_job(arg):
    print("the process [%d] is running, arg:%s" % (os.getpid(), arg))
    time.sleep(10)

print("the calling process [%d] will create a new process" % os.getpid())
# 实例化进程对象
p = Process(target=child_job, args=("你好啊",))
# 使能子进程
p.start()
# 等待子进程终止
p.join(timeout=None) # timeout阻塞时间,默认是永久阻塞,直到子进程终止为止
print("the child process done")
