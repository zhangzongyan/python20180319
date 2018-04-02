
# 列表生成式
# 生成一个1~10之间所有的数值平方组成的列表
l = []

for i in range(1, 11):
	l.append(i * i)
print(l)

'''
x = 9
print(x if x % 2 == 0 else x+1)
'''
l2 = [x * x for x in range(1, 11)]
print(l2)
l3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(l3)

# 已知有列表myls = ["hello", "uplooking", 123, 345, "python"]所有字符串成员转换为
# 大写生成一个新的列表
myls = ["hello", "uplooking", 123, 345, "python"]
newl = [i.upper() for i in myls if isinstance(i, str)]
print(newl)

# 获取当前目录下所有的文件，组成一个列表
import os

print([f for f in os.listdir(".")])




