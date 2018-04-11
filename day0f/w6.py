'''
多线程同步
'''
import w5
import time
import threading

#定义全局变量
n = 100
# 任务线程
def job(flname, l):
    global n
    l.acquire()
    n += 1
    #time.sleep(1)
    with open(flname, "r+") as f:
        data = str(int(f.readline()) + 1)
        f.seek(0, 0)
        f.write(data)
    l.release()

if __name__ == '__main__':
    with open("./w6.txt", "w") as f:
        f.write("0")
    thlist = []
    # 创建一个锁对象
    lock = threading.Lock()
    for i in range(20):
        t = w5.MyThread(job, ("./w6.txt", lock), "thread"+str(i))
        thlist.append(t)
    for i in range(20):
        thlist[i].start()
    for i in range(20):
        thlist[i].join()

    print(n)


