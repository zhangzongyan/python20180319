'''
作者: zhangzongyan
时间: 18-4-16
'''

import pymysql

# 链接数据库---->register数据库
mydb = pymysql.connect(host='localhost', user='root', password='123456', db='register', charset='utf8') #port默认值3306
# cursor对象
c = mydb.cursor()
# 创建用户信息表
c.execute('''create table if not exists userinfo(no integer primary key, username char(20) not null,
        passwd text not null)''')

try:
    c.execute('''insert into userinfo(no, username, passwd) values(1, 'zhangqi', '123456') ''')
    c.execute('''insert into userinfo(no, username, passwd) values(2, 'liqiang', '123456') ''')

except Exception as e:
    print(e)
c.execute('''select * from userinfo ''')
print( c.fetchall())
mydb.commit()
mydb.close()


