

'''
# 面向过程
def pri_stuinfo(stu):
	print("%s %d" % (stu[0],stu[1]))

d = {"lily":89, "lilei":90, "lisa":100}
for i in d.items():
	pri_stuinfo(i)
'''

# 面向对象 ---->抽象类型

class Student(object):
	def __init__(self, name="shagua", score=10): # __init__不需要显示调用,构造方法:当创建此类对象的时候,自动调用的
		self.name = name
		self.score = score
	def pri_stu(self): # 数据封装:在类内部提供方法访问实例属性
		print("{}:{}".format(self.name, self.score))
	def get_level(self):
		ls = ['E', 'E', 'E', 'E', 'E', 'E', 'D', 'C', 'B', 'A', 'A']
		print("你的等级是%s" % ls[self.score//10])


s1 = Student("yaojikai", 100) 
#print(s1.name, s1.score)
s1.pri_stu()
s1.get_level()

s2 = Student("zhangzhen", 99)
#print(s2.name, s2.score)
s2.pri_stu()

s3 = Student()
#print(s3.name, s3.score)
s3.pri_stu()

