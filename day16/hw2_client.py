'''
tcp 客户端
'''
from socket import *

client_sd = socket(AF_INET, SOCK_STREAM)
client_sd.connect(("172.25.1.206", 1234))

# 接收服务其的消息
data = client_sd.recv(100)
print("from server: %s" % data.decode('utf-8'))
client_sd.send("你好啊! 服务器".encode('utf-8'))
data = client_sd.recv(1024)
print('服务器给我回复了:%s' % data.decode('utf-8'))
client_sd.close()