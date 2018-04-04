

class Ticket(object):
	def __init__(self, vacation = False, student = False):
		self.__price = 100
		if vacation:
			self.__increace = 1.2
		else:
			self.__increace = 1
		if student:
			self.__discout = 0.5
		else:
			self.__discout = 1
	def getPrice(self, num):
		return self.__price * self.__increace * self.__discout * num

# 此对象是社会青年并没有在节假日买票
adult1 = Ticket()
ap1 = adult1.getPrice(2)
student1 = Ticket(student = True)
sp1 = student1.getPrice(1)
print("非节假日:两个成年人的票价是{},一个学生的票价是{}".format(ap1, sp1))

# 节假日
adult2 = Ticket(vacation = True)
ap2 = adult2.getPrice(2)
student2 = Ticket(vacation = True, student = True)
sp2 = student2.getPrice(1)
print("节假日:两个成年人的票价是{},一个学生的票价是{}".format(ap2, sp2))



