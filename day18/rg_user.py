'''
作者: zhangzongyan
时间: 18-4-16
'''
import tkinter as tk
import tkinter.messagebox
import socket
import threading

SERVERIP = '172.25.1.206'
SERVERPORT = 8765

class RgsGui():
    def __init__(self):
        self.root = tk.Tk() #创建窗口
        self.root.geometry("150x150")
        self.umvar = tk.StringVar() #
        username_e = tk.Entry(self.root, textvariable = self.umvar)
        self.umvar.set("用户名")
        username_e.pack()

        self.pwvar = tk.StringVar()
        passwd_e = tk.Entry(self.root, textvariable = self.pwvar)
        self.pwvar.set("密码")
        passwd_e.pack()
        b = tk.Button(self.root, text="立即注册", command = self.button_fun)
        b.pack()

        # 创建用户通讯的套接字
        self.sd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 创建一个任务线程,用于接收服务器反馈
        t = threading.Thread(target=self.thread_job, args=())
        t.setDaemon(True)
        t.start()

    # 线程函数
    def thread_job(self):
        while True:
            rcvdata, raddr = self.sd.recvfrom(1024)
            if rcvdata.decode('utf-8') == 'OK':
                # print('成功')
                tk.messagebox.showinfo("成功", "恭喜你!注册成功")
            else:
                tk.messagebox.showinfo("注册失败", "您注册的账号已存在")
                self.root.destroy()
                exit(1)
    def button_fun(self):
        # 获取用户输入的账号和密码
        snddata = self.umvar.get() + ' ' + self.pwvar.get()
        self.sd.sendto(snddata.encode('utf-8'), (SERVERIP, SERVERPORT))

if __name__ == '__main__':
    r = RgsGui()
    r.root.mainloop()