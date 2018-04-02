
# 生成器:通过给定的算式，一边计算一边得到每一个值的
# 生成一个1~10之间所有的数值平方组成的列表
l2 = [x * x for x in range(1, 11)]
print(l2)


g1 = (x * x for x in range(1, 11))
print(g1)
'''
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
'''
# 生成器是可迭代的
for g in g1:
	print(g)

# 定义一个函数，将斐波那契数列的前n项打印

# 第n项
def febn(n):
	print("debug")
	if n <= 0:
		return -1
	if n == 1 or n == 2:
		return 1
	return febn(n-1) + febn(n-2)

# 前m项
def printfebn(m):
	for i in range(1,m+1):
		#print(febn(i))
		yield febn(i)


g = printfebn(8)
print(g)
next(g)
'''
for res in g:
	print(res, end=" ")
print("")
'''

# 说明yield用法

def test():
	print("step1")
	yield 1
	print("step2")
	yield 2
	print("step3")
	yield 3

t = test()
print(next(t))
print(next(t))
print(next(t))
print(next(t))










