'''
创建多线程:_thread threading(高级)
'''
import _thread
from time import sleep,ctime

def loop0():
    print("starting loop 0 at:", ctime())
    sleep(4)
    print("loop 0 done at:", ctime())

def loop1():
    print("starting loop 1 at:", ctime())
    sleep(2)
    print("loop 1 done at:", ctime())

def main():
    print("the process is running at:", ctime())
    #创建两个线程
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())

    sleep(6) #为了主线程不终止,这不是一个好的方法
    print("all Done at:", ctime())

if __name__ == '__main__':
    main()
