

# 将出1~100之间所有的偶数输出

'''
for i in range(1, 100): # 序列1~99的序列
	print(i, end=" ")

for i in range(100): # 序列0~99的序列
	print(i, end=" ")
'''

for n in range(1, 101):
	# 判断n的奇数还是偶数	
	if (n == 50):
		#break;  #终止循环语句,不会执行for的else中的语句
		continue;#终止当前循环，继续下一次循环，不影响for的else语句
	if n % 2 == 0:
		print(n)
else:
	print("所有的偶数都已经输出")


