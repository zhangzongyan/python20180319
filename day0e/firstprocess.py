#linux / mac 都支持fork创建进程,但windows不支持
import os
import time
import sys

print("the calling process [%d] running" % os.getpid())
n = 100
pid = os.fork()  #一旦fork成功了,当前的代码就相当于有两份同时在执行
if pid == 0:
    #子进程   os.getpid() 获取调用进程pid  os.getppid() 获取父进程pid
    i = 0
    while i < 3:
        n += 1
        print("[%d]good morning, the parent pid is [%d], n = %d" % (os.getpid(), os.getppid(), n))
        time.sleep(1)
        i += 1
    sys.exit(0) #进程终止
else:
    print("pid:%d" % pid) # 在父进程中fork函数返回的子进程pid
    time.sleep(10)
    print("[%d]eat something" % os.getpid())
    print("n = %d" % n)