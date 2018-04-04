

class Rect():
	def __init__(self, length, width):
		self.__length  = length	
		self.__width = width
	def getRect(self):
		return (self.__length, self.__width)
	def setRect(self, newlen, newwdh):
		self.__length = newlen
		self.__width = newwdh
	def getArea(self):
		return self.__length * self.__width

r = Rect(10, 5)
print(r.getRect())
print(r.getArea())

r.setRect(15, 10)
print(r.getRect())
print(r.getArea())



