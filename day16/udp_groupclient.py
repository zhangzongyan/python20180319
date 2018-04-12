'''
作者: zhangzongyan
时间: 18-4-12
'''
import socket as s

GROUP = "224.2.3.4"
PORT = 1234
# 创建报式套接字
clientsd = s.socket(s.AF_INET, s.SOCK_DGRAM)
# 端口复用
clientsd.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
# 为套机字bind地址  客户端是从多播组中接收数据
clientsd.bind(("0.0.0.0", PORT))
# 加入多播组
'''
加入多播组setsockopt(level, option, multiaddr)
level:IPPROTO_IP
option:IP_ADD_MEMBERSHIP
multiaddr:ipv4 32整型数地址
点分十进制--->整型 inet_aton()
'''
clientsd.setsockopt(s.IPPROTO_IP, s.IP_ADD_MEMBERSHIP, s.inet_aton(GROUP)+s.inet_aton("0.0.0.0"))

rcvdata, raddr = clientsd.recvfrom(1024)
print("服务器:", rcvdata.decode('utf-8'))

clientsd.close()

