'''
作者: zhangzongyan
时间: 18-4-13
'''
import  sqlite3

conn = sqlite3.connect('./student.db')
c = conn.cursor()
c.execute('SELECT * FROM students')
# 获取表中所有的项
print(c.fetchall())
# 查询表中所有姓张的
c.execute('''SELECT stuNo FROM students WHERE stuName LIKE '张%%' ''')
print(c.fetchall())

#查询年龄的范围在22到24之间的
c.execute('''SELECT  * FROM students WHERE age BETWEEN 22 AND 24''')
print(c.fetchall())

# 修改
c.execute('''UPDATE students set age = 18 WHERE stuName = '张立强' ''')

#将分数100删除
c.execute('''DELETE FROM students WHERE score = 100''')

c.execute('SELECT * FROM students')
# 获取表中所有的项
print(c.fetchall())

conn.close()
