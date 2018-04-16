'''
作者: zhangzongyan
时间: 18-4-16
'''
import socket
import pymysql

SERVERIP = '172.25.1.206'
SERVERPORT = 8765

# 连接数据库   register_info
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='register', charset='utf8')
# 游标对象
c = conn.cursor()
# 创建套接字
serversd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 为套接字bind地址
serversd.bind((SERVERIP, SERVERPORT))

while True:
    try:
        rcvdata, raddr = serversd.recvfrom(1024)
        #print("from", raddr, 'recive:', rcvdata.decode('utf-8'))
        rcv = rcvdata.decode('utf-8')
        uname, pwd =  rcv.split(" ")
        #print(username, passwd)
        # 查找用户注册的账号是否存在,如果已存在,则不允许注册, 否则,成功并将用户信息插入到表中
        try:
            sql = "select * from register_info where username = %s"
            c.execute(sql, (uname))
        except Exception as e:
            print("error:", e)
        if c.fetchall() == ():
            # 查询数据为空,此账号未被注册
            serversd.sendto(b"OK", raddr)
            sql = 'insert into register_info(username, password) values(%s, %s)'
            c.execute(sql, (uname, pwd))
            conn.commit()
        else:
            serversd.sendto(b'FAILED', raddr)
    except Exception as e:
        print("operation error:", e)
        break

conn.close()
