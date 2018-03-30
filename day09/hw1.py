
'''
1. 编写一个函数：
   1) 计算所有参数的和的基数倍(默认基数为base=3)
'''
def sumn(*arg, base=3): #命名关键字参数
	res = 0	
	for n in arg:
		res += n
	return res*base

if __name__ == "__main__":
	print(sumn(1,2,3))
	print(sumn(0,2,3,4,5,6, base = 2))

	l = ["1","2","3","4","5","6"]
	s = "\n".join(l)
	print(s)


