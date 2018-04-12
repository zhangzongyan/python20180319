'''
作者: zhangzongyan
时间: 18-4-12
'''
import socket as s

# 创建报式套接字
clientsd = s.socket(s.AF_INET, s.SOCK_DGRAM)
# 将标准输入输入的内容发送
snddata = input("你的梦想是什么")
clientsd.sendto(snddata.encode('utf-8'), ("172.25.1.206", 1234))
# 接收服务器的反馈
rcvdata, raddr = clientsd.recvfrom(1024)
print("服务器说了:", rcvdata.decode('utf-8'))
clientsd.close()

