
# 求得100内的所有的偶数序列中有多少个是5的倍数

l = []

for i in range(2, 100, 2):
	if i % 5 == 0:
		l.append(i)
print(l)
	


