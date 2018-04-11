'''
扩展threading.Thread类---->定制自己的线程类
'''
import threading
from time import ctime,sleep

class MyThread(threading.Thread):
    def __init__(self, func, args, name = ''):
        super().__init__()
        self.func = func
        self.args = args
        self.name = name

    def getResult(self):
        return self.res

    def run(self):# 重写父类的run方法
        print("the thread {} is running at:{}".format(self.name, ctime()))
        self.res = self.func(*self.args)
        print("the thread {} end at {}".format(self.name, ctime()))

def loop(nsec):
    sleep(nsec)
    return 100

def main():
    print("main is running")
    t = MyThread(loop, (5,), "xiaobaiya")
    t.start()
    t.join()
    print("the new thread exit with", t.getResult())
    print("all finished")

if __name__ == '__main__':
     main()




