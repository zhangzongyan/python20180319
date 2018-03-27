

# 不使用python的sort方法，为列表排序
import random

l = []
for i in range(10):
	l.append(random.randint(1, 100))
print(l)

for i in range(9):
	# 每一次无序序列排序的索引范围
	for j in range(10-i-1):
		if l[j] > l[j+1]:
			l[j], l[j+1] = l[j+1], l[j]
print(l)
l.reverse()
print(l)

