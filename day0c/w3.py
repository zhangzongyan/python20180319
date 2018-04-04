

class Student():
	@property #使得类内部的方法的使用方式,变成与使用属性的方法一样
	def score(self):
		return self._score

	@score.setter
	def score(self, value): # 对类中实例属性的设置,相应提供方法,好处可以对值进行错误处理
		if not isinstance(value, int):
			raise ValueError("the value must be a integer")
		elif value < 0 or value > 100:
			raise ValueError("the value should between 0 and 100")
		else:
			self._score = value
		

'''
s = Student()
s.name = "yongpeng"
print(s.name)
'''
s1 = Student()
s1.score = 100

print(s1.score)
#s1.score(120)








