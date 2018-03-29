
import w1

# 可变参数

#print(sum(1,2,3,4,5)) 这是错误的 sum方法要求第一个参数是可迭代类型 参数是确定的
#改进sum函数，使得参数可变

def mysum(*number):
	'''
		*number就是一个可变参数
		本质将传递的多个参数看作元祖
	'''
	res = 0
	for i in number:
		res += i
	return res

# 定义一个函数：计算出给定参数的平方和   1, 2, 3
def add_square_all(*arg):
	r = 0
	for i in arg:
		r += w1.power2(i)	
	return r
	

if __name__ == "__main__":
	print(mysum(1,2))
	print(mysum(1,2,3))
	
	l = [3,4,5,6]
	print(mysum(l[0], l[1], l[2], l[3]))
	print(mysum(*l)) #将列表中的每一个元素作为此函数的参数

	print(add_square_all(1,2,3,4,5))

