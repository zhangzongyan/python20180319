

# 面向对象之继承 和多态

# 定义一个动物类
class Animal(object):
	def run(self):
		print("animal is running")	

# 定义一个狗类 ---->继承了Animal类,Dog类就是Animal的子类,Animal类称为Dog的父类,基类,超类
class Dog(Animal):
	#pass
	def run(self): # 多态:使得继承父类的方法在当前类中可以有不同的表现形态
		print("dog is running")

# 定义猫类
class Cat(Animal):
	#pass
	def run(self):
		print("cat is running")

class Turtorial(Animal):
	def run(self):
		print("我要一步步往上爬")

# "鸭子类型"
class Child(object):
	def run(self):
		print("走两步")

def run_twice(animal):
	animal.run()	
	animal.run()	


ani = Animal()
ani.run()

xiaobai = Dog()
xiaobai.run()

mao = Cat()
mao.run()

print(isinstance(xiaobai, Dog))
print(isinstance(xiaobai, Animal))

run_twice(xiaobai)
run_twice(mao)

run_twice(Turtorial())

run_twice(Child())


