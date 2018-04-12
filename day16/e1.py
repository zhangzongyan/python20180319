'''
作者: zhangzongyan
时间: 18-4-12
'''
import threading
import time

def test():
    while True:
        print("hello world")
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=test, args = ())
    t.start() # 新创建的线程如果没有终止,main线程也不会终止
    print("main endding")