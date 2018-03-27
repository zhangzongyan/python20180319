
# 随机产生100以内的100个整型数值，存储在一个列表中
 # 遍历次列表，统计产生的数值中有多少个整型数

from random import randint

l = []
for i in range(100):
	l.append(randint(0, 99))
# 打印列表 一行有10个元素

count = 0
for i in range(0, 100):
	print("{:>3}{}".format(l[i], " " if (i+1) % 10 != 0 else "\n"), end="")
	if l[i] % 2 != True:
		count += 1
print("偶数的个数是:", count)



