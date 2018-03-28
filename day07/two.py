
import one

def func():
	print("this is two.py 's funtion")

if __name__=='__main__': #如果执行的就是本文件，则此条件为真,作用：防止被其他文件import的时候，强制执行某些语句
	func()
	one.func()


