'''
作者: zhangzongyan
时间: 18-4-12
'''
import socket as s
import time

GROUP = "224.2.3.4"
PORT = 1234
# 创建报式套接字
serversd = s.socket(s.AF_INET, s.SOCK_DGRAM)
# 使得服务器实现组播
serversd.setsockopt(s.IPPROTO_IP, s.IP_MULTICAST_TTL, 255)
# serversd.setsockopt(s.IPPROTO_IP,
#         s.IP_ADD_MEMBERSHIP,
#         s.inet_aton(GROUP) + s.inet_aton("0.0.0.0"))#加入到组播组

while True:
    serversd.sendto(b'hello', (GROUP, PORT))
    time.sleep(1)

serversd.close()










