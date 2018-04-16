'''
作者: zhangzongyan
时间: 18-4-16
'''

import pymysql

# 链接数据库---->register数据库
mydb = pymysql.connect(host='localhost', user='root', password='123456', db='register', charset='utf8') #port默认值3306
# cursor对象
c = mydb.cursor()
c.execute('''create table if not exists userinfo(no integer auto_increment primary key, username char(20) not null,
        passwd text not null)''')


c.execute('''insert into userinfo(username, passwd) values('zhangqi', '123456') ''')
c.execute('''insert into userinfo(username, passwd) values('liqiang', '123456') ''')
c.execute('''insert into userinfo(username, passwd) values('吴寒', '123456') ''')

mydb.commit()
mydb.close()


