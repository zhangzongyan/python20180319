

# 递归函数 找到递归点 递归终止条件

def sumn(n):
	if n == 0:
		return 0
	return n + sumn(n-1)

print(sumn(5))


