
# 定义一个Person类,有设置和获取出生年份的方法, 还要有获取年龄的方法

class Person():
	__slots__=("_birth", "name") # 绑定当前类中只能有属性"_birth"

	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self, birth):
		self._birth = birth

	@property
	def age(self):
		return 2018-self._birth

ps = Person()
ps.birth = 1997
print(ps.age)
print(ps.birth)

ps.name = "yongpeng"
#ps.age = 25


