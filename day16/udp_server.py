'''
作者: zhangzongyan
时间: 18-4-12
'''
import socket as s
import time

# 创建报式套接字
serversd = s.socket(s.AF_INET, s.SOCK_DGRAM)
# 为套机字bind地址
serversd.bind(("0.0.0.0", 1234))

while True:
    # 接收对端数据 rcvdata数据 raddr 数据来源地址 1024 最多接收1024bytes
    rcvdata, raddr = serversd.recvfrom(1024)
    print("from client:", rcvdata.decode('utf-8'))
    snddata = time.ctime() + rcvdata.decode('utf-8')
    # 数据发送
    serversd.sendto(snddata.encode('utf-8'), raddr)

serversd.close()










