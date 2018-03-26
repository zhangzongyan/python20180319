
# 获得一个整型数的每一位   回文整型数(对称数) 12321  11 111   889959988

n = int(input("请输入一个整型数值: "))
res = 0
save = n
# 123
while n > 0:
	res = res * 10 + n % 10 #求得当前n的最低位
	#print(res, end=" ")
	n //= 10

if save == res:
	print("%d 是一个回文整型数" % save)
else:
	print("%d 不是一个回文整型数" % save)
	

