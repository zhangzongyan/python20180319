'''
作者: zhangzongyan
时间: 18-4-13
'''
import sqlite3
'''
使用sqlite3注意的地方
    1.虽然他是支持动态类型,但推荐将字段加类型,特别是primary key(唯一的)
    Python type	SQLite type
    None	      NULL
    int	          INTEGER
    float	      REAL
    str	          TEXT
    bytes	      BLOB
    2.CREATE TABLE IF NOT EXISTS listname()
    IF NOT EXISTS 如果创建的表不存在,则创建
    3.INSERT OR IGNORE / REPLACE
    IGNORE / REPLACE 仅针对字段有主键时有意义

'''
# 创建并连接数据库
conn = sqlite3.connect('./student.db')
# 创建Cursor对象, 使用此对象操作数据库
c = conn.cursor()
# 创建一张学生表
# 使得cursor对象,执行指定的sql语句 主键推荐使用整型,不是必备的
c.execute('''CREATE TABLE IF NOT EXISTS  students(stuNo integer PRIMARY KEY AUTOINCREMENT, stuName TEXT NOT NULL , age, score)''')
# 向表中插入一条记录
#c.execute('''INSERT INTO students(stuNo, stuName, age, score)
# INSERT OR IGNORE 插入如果失败了则忽略此sql语句
c.execute('''INSERT OR IGNORE INTO students(stuNo, stuName, age, score)
VALUES(1, '朝前', 23, 100)''')
c.execute('''INSERT OR IGNORE INTO students(stuNo, stuName, age, score)
VALUES(2, '曹旭', 23, 99)''')
# 如果插入的元素已存在则替换
c.execute('''INSERT OR REPLACE INTO students(stuNo, stuName, age, score)
VALUES(3, '永鹏', 24, 89)''')

c.execute('''INSERT  OR IGNORE INTO students(stuName, age, score)
VALUES ('张起', 22, 87)''')

ls = [('张立强', 21, 90), ('刘淇', 20, 88), ('吴寒', 23, 98)]
c.executemany('''INSERT OR IGNORE INTO students(stuName, age, score)
VALUES (?,?,?)''', ls)

c.execute('''INSERT OR REPLACE INTO students(stuName, score) VALUES (?,?)''', ('占森', 77))
#c.execute('''INSERT OR REPLACE INTO students(age, score) VALUES (?,?)''', (25, 77)) 名字不能为空
# 提交数据
conn.commit()

#关闭数据库
conn.close()

