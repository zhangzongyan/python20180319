

# 定义一个函数：求得两个整型数的和

def sum2num(m, n):
	res = m + n
	return res

# 定义求得两个整型数中较大的整型
def max2num(n1, n2):
	return n1 if n1 > n2 else n2

'''
a, b = eval(input("请输入两个整型数(m, n)"))

res = sum2num(a, b)
print("{} + {} = {}".format(a, b, res))
print("{}和{}中较大的是{}".format(a, b, max2num(a, b)))
'''

# 匿名函数 lambda 适用于函数功能简单，函数体内容少

# lambda 参数列表:返回值

f = lambda x : x * x
print(type(f))
print(f(10))



