'''
作者: zhangzongyan
时间: 18-4-12
创建三个函数,分别的功能是, 求得斐波那契数列的第n项, 求n的阶乘,求n的前n项和
请比较三个函数单线程分别调用,和三个函数多线程并发的效率(相差多长时间)
假定n的值是15
'''
import time
import mythread

def fib(n):
    time.sleep(0.005)
    if n < 1:
        return -1
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def fact(n):
    time.sleep(0.5)
    if n == 1:
        return 1
    return n * fact(n-1)

def sumn(n):
    time.sleep(0.05)
    if n == 1:
        return 1
    else:
        return n + sumn(n-1)

if __name__ == '__main__':
    fun_list = [fib, fact, sumn]
    print("main is starting at:", time.ctime())
    n = 15
    for i in range(len(fun_list)):
        print(fun_list[i](n))
    print("signal thread done at:", time.ctime())

    print("multi thread start at:", time.ctime())
    threads = []
    for i in range(len(fun_list)):
        t = mythread.MyThread(fun_list[i], (n,), fun_list[i].__name__)
        threads.append(t)
        t.start()
    for i in range(len(fun_list)):
        threads[i].join()
        print(threads[i].getResult())
    print("all done at:", time.ctime())

