'''在进程创建的基础上添加功能,进一步了解Process类, 扩展了解'''
from multiprocessing import Process
import os
def test():
    print("你看到这个函数了吗")
class MyProcess(Process):
    def __init__(self, name, fun = None):
        super().__init__(target=fun) #继承Process类的__init__方法
        self._name = name
        self._fun = fun
    def run(self):
        print("[%d]%s is running"%(os.getpid(), self._name))

print("the calling process %d" % os.getpid())
m = MyProcess("testProcess", fun = test)
m.start() #调用MyProcess类中的run方法


