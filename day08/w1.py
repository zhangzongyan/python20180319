


def power(x):
	return x * x

# 位置参数
def powern(x, y):
	res = 1	
	while y > 0:
		res *= x
		y -= 1
	return res

# 定义一个函数，默认求平方，也可以通过传参数改变n次方
# 默认参数 ：此参数如果不传递，则使用默认值
def power2(x, y=2):
	res = 1	
	while y > 0:
		res *= x
		y -= 1
	return res
	
def stu_info(name, age = 11, city="beijing"):
	'''
		这是一个说明默认参数必要性的函数
	'''
	print("名字:{} 年龄:{} 城市:{}".format(name, age, city))


# 使用默认参数的时候一定要选择不可变类型作为值
#def getlist(l=[]):
def getlist(l=None):
	if l == None:
		l = []
	
	l.append("TEST")
	return l


if __name__ == "__main__":
	'''
	n = int(input("请输入一个整型数"))
	print("{}的平方是{}".format(n, power(n)))
	
	print(powern(10, 3))
	'''
	print(power2(5))
	print(power2(5, 4))
	stu_info("朝前")
	stu_info("永鹏", 12)
	stu_info("希雅", city="hebei", age = 10)

	ls = [1,2,3]
	ls = getlist(ls)
	print(ls)
	ls = [1,2,3]
	ls = getlist(ls)
	print(ls)

	ls = getlist()
	print(ls)
	ls = getlist()
	print(ls)






