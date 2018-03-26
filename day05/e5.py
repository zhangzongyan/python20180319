
'''
任意输入一个正整数,判断其是否为质数
求得1到100之间有多少个质数
'''

#number = int(input("请输入一个正整数"))
cnt = 1 # 2
for number in range(3, 101):
	flag = True
	
	# range(2, number)是一个除了1和number之外的序列
	for i in range(2, number//2+1):
		if number % i == 0:
			flag = False
			break
	'''
	else : # for循环是循环条件不满足而终止的，不是break终止的
		print("{}是一个质数".format(number))
	'''
	if flag == False:  
		#print("{}不是一个质数".format(number))
		pass
	else:
		print("{}是一个质数".format(number))
		cnt += 1
		
print("共%d个质数" % cnt)
