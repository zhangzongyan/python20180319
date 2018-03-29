

# 定义一个函数:实现两个整型数的交换
# 局部变量:在函数内指明的变量
def swap2num(a, b):
	num1, num2 = b, a #当局部变量与全局变量同名，则会创建新的局部变量
	a, b = b, a
	print("swap2num:", "num1:", num1, "num2:", num2)

def swap2num_r():
	global num1, num2  #global关键字 表明在函数内使用的是全局的num1和num2
	num1, num2 = num2, num1 

def testlist(arg):   # !!!!!!组合类型作为函数的参数，传递就是本身
	i = 0
	while i < len(arg):
		arg[i] += 1
		i += 1


if __name__ == "__main__":
	num1 = 100   #num1 num2 全局的
	num2 = 200

	print("num1:", num1, "num2:", num2)
	swap2num_r()
	print("num1:", num1, "num2:", num2)

	l = [1,2,3,4]
	testlist(l)
	print(l)




