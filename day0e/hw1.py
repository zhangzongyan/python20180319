
class Student(object):
	def __init__(self, name, age, scores):
		self.__name = name
		self.__age = age
		self.__scores = scores
		for s in self.__scores:
			if s < 0 or s > 100:
				raise ValueError("你的每一科成绩必须在0到100之间")
	def getName(self):
		return self.__name
	def getAge(self):
		return self.__age
	def getMaxScore(self):
		return max(self.__scores)

s = Student("zhangshile", 20, [90, 89, 100])
print("{} age:{},学的最好的一门成绩:{}".format(s.getName(), s.getAge(), s.getMaxScore()))
try:
	s2 = Student("zhangshile", 18, [90, -89, 100])
	print("{} age:{},学的最好的一门成绩:{}".format(s2.getName(), s2.getAge(), s2.getMaxScore()))
except ValueError as e:
	print("程序出现异常:%s" % e)

print("结束了")


