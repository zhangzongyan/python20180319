'''
作者: zhangzongyan
时间: 18-4-16
'''
# encoding=utf-8
import pymysql

# 链接数据库---->register数据库
mydb = pymysql.connect(host='localhost', user='root', password='123456', db='newdb', charset='utf8') #port默认值3306
# cursor对象
c = mydb.cursor()
# 创建用户信息表
c.execute('''create table if not exists userinfo(no integer primary key, username nvarchar(128) not null,
        passwd text not null)''')

try:
    c.execute('''insert into userinfo(no, username, passwd) values(1, 'zhangqi', '123456') ''')
    c.execute('''insert into userinfo(no, username, passwd) values(2, 'liqiang', '123456') ''')

except Exception as e:
    print(e)
#尝试插入中文
try:
    c.execute('''insert into userinfo(no, username, passwd) values(6, '中文2', '123')''')
except Exception as e:
    print(e)
c.execute('''select * from userinfo ''')
print( c.fetchall())
mydb.commit()
mydb.close()


