
# 汉诺塔
def hano(n, a, b, c):
	if n == 1:
		print(a, "---->", c)
		return None
	hano(n-1, a, c, b)
	hano(1, a, b, c)
	hano(n-1, b, a, c)
hano(7, 'A', 'B', 'C')

