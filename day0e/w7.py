'''
进程间通信---Pipe
'''
from multiprocessing import Pipe, Process
import os
# child
def jobs(out, inn):
    inn.close()
    while True:
        try:
            print("[%d]read the data %s" % (os.getpid(), out.recv())) # recv()读管道
        except:
            out.close()
            break

if __name__ == '__main__':
    out_pipe, in_pipe = Pipe() #out_pipe读端  in_pipe写端
    p = Process(target=jobs, args=(out_pipe, in_pipe))
    # parent write_pipe
    # 将不操作的一端关闭
    p.start()
    out_pipe.close()
    for i in ["python", "是", "最好的", "语言"]:
        in_pipe.send(i) #写管道
    in_pipe.close()
    p.join()




