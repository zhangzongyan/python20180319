'''
 main进程创建一个新文件"./myprocess.txt",并写入"0"
   1) 创建20个进程,20个进程的任务都是将"./myprocess.txt"文件中的值读出来,+1写回去(覆盖之前的值)
   2) 当20个进程全部结束后,文件中的值为多少
'''
from multiprocessing import Process, Pool
import time, os

# 多个进程操作同一文件发生了竞争,如何解决使用进程的lock

def newprocess(flname):
    print("the process [%d] running" % os.getpid())
    time.sleep(5)
    f = open(flname, "r+")
    fistline = f.readline()
    fistline = str(int(fistline) + 1)
    print(fistline)
    f.seek(0, 0)
    f.write(fistline)
    f.close()

if __name__ == '__main__':
    f = open("./myprocess.txt", "w")
    f.write("0")
    f.close()
    # 创建一个进程池
    p = Pool(20)
    for i in range(20):
        p.apply_async(newprocess, args=("./myprocess.txt",))
    p.close()
    p.join()

