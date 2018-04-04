

# 定制类  像__slots__ __len__ __name__ ...方法名/变量名在python中有特殊的含义

class Student():
	def __str__(self):
		return "this is a Student instance"

s = Student()
print(s) # 打印对象s自动调用Student类的__str__方法

# __iter__    __next__
import time

class Fib(object):
	def __init__(self):
		self._a = 0 
		self._b = 1
	def __iter__(self):
		return self
	def __next__(self):
		self._a, self._b = (self._b, self._a + self._b)
		while self._a > 1000:
			raise StopIteration()
		return self._a
f = Fib()
for i in f:
	print(i)	
	#time.sleep(0.1)

# type
class Hello(object):
	def hi(self, word = "world"):
		print("hello, %s"%word)
h = Hello()
h.hi()
print(type(Hello))





