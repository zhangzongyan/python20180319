

class Flowers(object):
	def __init__(self, color, name, shape):
		self.__color = color
		self.__name = name
		self.__shape = shape
	def showinfo(self):
		print("{}的颜色是{} 形态是{}".format(self.__name, self.__color, self.__shape))	
	def setcolor(self, newcolor):
		self.__color = newcolor

yc = Flowers("黄色", "迎春", "扇形")
yc.showinfo()
yc.setcolor("红色")
yc.showinfo()



