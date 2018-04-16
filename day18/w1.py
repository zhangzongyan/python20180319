'''
作者: zhangzongyan
时间: 18-4-16
'''
import pymysql

# 链接数据库---->register数据库
mydb = pymysql.connect(host='localhost', user='root', password='123456', db='register', charset='utf8') #port默认值3306
# cursor对象
c = mydb.cursor()
c.execute('''create table if not exists userinfo(no integer primary key , username text not null,
        passwd text not null)''')
try:
    c.execute('''insert into userinfo(no, username, passwd) values(2, 'zhangqi', '123456') ''')
    c.execute('''insert into userinfo(no, username, passwd) values(5, 'liqiang', '123456') ''')
except :
    pass
mydb.commit()
mydb.close()


