
# 面向对象编程:1.先抽象类型  核心:类 实例(对象)   
# 面向对象三大特点:封装\继承\多态

class Student(object):
	def __init__(self, name="shagua", score=10): # __init__不需要显示调用,构造方法:当创建此类对象的时候,自动调用的
		self.__name = name  # 限制当前属性只能在类内部修改
		self.__score = score
	def pri_stu(self): # 数据封装:在类内部提供方法访问实例属性
		print("{}:{}".format(self.__name, self.__score))
	def get_level(self):
		ls = ['E', 'E', 'E', 'E', 'E', 'E', 'D', 'C', 'B', 'A', 'A']
		print("你的等级是%s" % ls[self.__score//10])
	# 修改属性
	def setname(self, newname):
		self.__name = newname
	def setscore(self, newscore):
		self.__score = newscore
	


s1 = Student("yaojikai", 100) 
#print(s1.name, s1.score)
s1.pri_stu()
s1.get_level()

#print(s1.__name)  # 报错的,因为实例属性__name私有属性
print(s1._Student__name) #如果属性名字__name,本质并不是私有,仅仅是python解释器在解释的时候在名字前加了_Student

# !!!!!!!!!!!! 不要这么做
s1.__name = "wangzhansen"  # 并没有修改类内部此对象的__name,而是新创建一个__name属性
print(s1.__name)  # 访问的是新创建的__name
s1.pri_stu()

s1.setname("wangzhansen")
s1.pri_stu()


