

class Printm(object):
	def printcontext(self): # self 实例对象   不是类
		print("打印机正在打印")

# 继承
class BlackPrint(Printm):
	def printcontext(self):
		print("黑白打印机打印黑白字")

class ColorPrint(Printm):
	def printcontext(self):
		print("彩色打印机能打印照片")

def show(pri):
	pri.printcontext()

p1 = Printm()
show(p1)

p2 = BlackPrint()
show(p2)

p3 = ColorPrint()
show(p3)

