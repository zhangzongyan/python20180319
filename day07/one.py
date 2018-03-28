

def func():
	print("this is one.py 's function")

if __name__=='__main__': #如果执行的就是本文件，则此条件为真,作用：防止被其他文件import的时候，强制执行某些语句
	print("number one")
	func()
else:
	print("你想干啥")

