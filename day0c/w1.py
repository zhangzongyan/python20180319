
'这是一个装饰器(deractor)'

# 函数作为另一个函数的返回值(高阶函数) 
def lazy_fun():
	def newnow():
		print("2018-4-4")
	return newnow

import functools

# 装饰器:在函数执行的过程中为函数加功能
def log(fun): # "闭包":内部函数可以保存住外部函数的参数变量
	@functools.wraps(fun) # 将fun函数的属性赋值给wrapper 包括__name__
	def wrapper(*args, **kw):
		print("%s is called" % fun.__name__)
		return fun(*args, **kw)
	return wrapper

@log # now = log(now) 
def now():
	print("2018-4-4")

now()
print("%s" % now.__name__)

#print(lazy_fun()())


