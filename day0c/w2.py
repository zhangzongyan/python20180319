
'这是一个装饰器(deractor)'

import functools

def log(mystr):	
	# 装饰器:在函数执行的过程中为函数加功能
	def funarg(fun): # "闭包":内部函数可以保存住外部函数的参数变量
		@functools.wraps(fun) # 将fun函数的属性赋值给wrapper 包括__name__
		def wrapper(*args, **kw):
			print("%s" % mystr)
			return fun(*args, **kw)
		return wrapper
	return funarg

@log("快饿死了")  # now = log("快饿死了")(now)
def now():
	print("2018-4-4")

now()
print("%s" % now.__name__)

#print(lazy_fun()())


