'''
多线程,解决main线程等待多个线程终止后,再终止
'''
import time
import _thread

loops = [4, 2]
# nloop线程编号  nsec 睡眠时间 lock 锁
def loop(nloop, nsec, lock):
    print("loop", nloop, "start at:", time.ctime())
    time.sleep(nsec)
    print("loop", nloop, "end at:", time.ctime())
    lock.release() #释放锁  解锁

def main():
    print("the process running at:", time.ctime())
    locks = []
    for i in range(len(loops)):
        locks.append(_thread.allocate_lock()) #创建一个锁
        locks[i].acquire()
    for i in range(len(loops)):
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    # 等待两个锁都释放了,表示任务线程终止了
    for i in range(len(loops)):
        while locks[i].locked():
            pass
    print("all done at:", time.ctime())

if __name__ == '__main__':
    main()