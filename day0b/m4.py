

# 继承:遗留一个问题,父类Person init方法调用了两次,如果想使得其只调用一次,在调用父类的init方法时候
# 不要直接使用父类的名字,用super()获取父类

class Person(object): # 父类
	def __init__(self, name, gender):
		print("Person init is called")
		self.__name = name
		self.__gender = gender
	def eat(self):
		print("{}正在吃饭".format(self.__name))
	def getinfo(self):
		print("{} {}".format(self.__name, self.__gender))

# 学生类: 继承Person类的时候不会自动调用Person的init方法
class Student(Person):
	def __init__(self, name, gender, score):
		print("Student init is called")
		Person.__init__(self, name, gender)
		self.__score = score
	def getmyinfo(self):
		self.getinfo()
		print("成绩是{}".format(self.__score))

# 员工类
class Employee(Person):
	def __init__(self, name, gender, salory):
		print("Employee init is called")
		Person.__init__(self, name, gender)
		self.__salory = salory

#python允许多重继承
#实习生类
class Cadet(Student, Employee):
	def __init__(self, name, gender, score, salory):
		Student.__init__(self, name, gender, score)
		Employee.__init__(self, name, gender, salory)		



stu2 = Cadet("zhangqi", "男", 99, 10000)
stu2.getmyinfo()




