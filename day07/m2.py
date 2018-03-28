
# 祝小胖生日快乐

# 函数的定义
'''
happy:函数名(标识符)
(参数列表) 可以有0个或任意多个，已知条件
'''
def happy():
	#函数体
	print("happy birthday to you")
	#return None 可省略


# person  形式参数 (形参)
def sing(person):
	happy()
	happy()
	print("happy birthday, dear"+person+"!!!!")
	happy()

#调用
sing("曹欢") #"曹欢"实参
sing("占森")

