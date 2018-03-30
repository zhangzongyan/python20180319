

# 斐波那契数列

def febnacii(n):
	if n < 1:
		return -1
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return febnacii(n-1) + febnacii(n-2)	

if __name__ == "__main__":
	for i in range(1, 21):
		print(febnacii(i), end=" ")
	print("")

