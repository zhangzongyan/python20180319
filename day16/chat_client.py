'''
作者: zhangzongyan
时间: 18-4-12
'''
import tkinter as tk
import socket
import threading

# 任务线程工作
def recvclient(newsd, remote_addr):
    while True:
        rcvbuf = newsd.recv(1024).decode('utf-8')
        if rcvbuf == '':
            continue
        if rcvbuf == 'byebye':
            newsd.close()
            break
        print('客户端[%s, %s]' % remote_addr, end=' ')
        print('----->服务器说:')
        print(rcvbuf)

class ClientUi(object):
    def __init__(self, serveraddr):
        self.serveraddr = serveraddr
        # 打标记 True,连接已创建  False:连接失败
        self.flag = False
        self.root = tk.Tk()
        self.root.title("python聊天室1.0_客户端")
        #self.root.geometry("600x400")
        #定义三个框架
        frames = [tk.Frame(), tk.Frame(), tk.Frame(), tk.Frame()]
        #实例化列表框对象
        self.listbox = tk.Listbox(frames[0], width = 70,height = 18)
        #实例化一个滚动条
        self.roll = tk.Scrollbar(frames[0])
        frames[0].pack(expand=1, fill=tk.BOTH )
        # 绑定列表框 和 滚动条
        self.listbox['yscrollcommand'] = self.roll.set
        self.roll['command'] = self.listbox.yview
        self.roll.pack(side=tk.RIGHT, expand = 1, fill=tk.Y)
        self.listbox.pack(side = tk.LEFT,expand = 1, fill=tk.BOTH)

        #定义一个Label 隔开列表框和输入框
        self.mylable = tk.Label(frames[1])
        self.mylable.pack(expand = 1, fill=tk.BOTH)
        frames[1].pack(expand = 1, fill=tk.BOTH)
        #输入框
        self.text = tk.Text(frames[2], width = 70, height = 12)
        self.textroll = tk.Scrollbar(frames[2])
        #绑定text和滚动条
        self.text['yscrollcommand'] = self.textroll.set
        self.textroll['command'] = self.text.yview
        self.text.pack(side = tk.LEFT, expand=1, fill=tk.BOTH)
        self.textroll.pack(side=tk.RIGHT, expand = 1, fill=tk.Y)
        frames[2].pack(expand=1, fill=tk.BOTH)

        #发送按钮的框架
        self.button = tk.Button(text = "发送消息", command = self.sendMessages).pack()
        frames[3].pack(expand=1, fill = tk.BOTH)

    #发送消息
    def sendMessages(self):
        if self.flag == False:
            return
        # 获取text输入的内容  显示到listbox中并发送给客户端, 清除text内容
        getmsg = self.text.get("1.0", tk.END) # 获取text中的内容'1.0'第一行,第一列  tk.END最后
        self.listbox.insert(tk.END, getmsg)
        # 清空text
        self.text.delete('1.0', tk.END)
        #将消息通过套接字发送
        self.clientsd.send(getmsg.encode('utf-8'))

    #线程工作:创建套接字,使得套接字处于监听状态,并接收客户端请求
    def reciveMessages(self):
        self.clientsd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsd.connect(self.serveraddr)
        self.flag = True
        while True:
            recvdata = self.clientsd.recv(1024).decode('utf-8')
            if recvdata == '':
                continue
            self.listbox.insert(tk.END,recvdata)
    def startRecive(self):
        t = threading.Thread(target=self.reciveMessages)
        t.setDaemon(True) #使得新线程随着main的终止而终止
        t.start()
if __name__ == '__main__':
    s = ClientUi(("172.25.1.206", 8889))
    s.startRecive()
    s.root.mainloop()
