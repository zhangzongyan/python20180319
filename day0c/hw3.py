
import random
import time

init_x = [0, 10]
init_y = [0, 10]

# 乌龟类
class Turtle(object):
	def __init__(self):
		self._x = random.randint(init_x[0], init_x[1])	
		self._y = random.randint(init_y[0], init_y[1])	
		self._eng = 100
	def move(self):
		newx = self._x + random.choice([1,2,-1,-2])					
		newy = self._y + random.choice([1,2,-1,-2])					
		# 边界问题
		if newx < init_x[0]:
			self._x = init_x[0] - (newx - init_x[0])
		elif newx > init_x[1]:		
			self_x = init_x[1] - (newx - init_x[1])
		else:
			self._x = newx
		if newy < init_y[0]:
			self._y = init_y[0] - (newy - init_y[0])
		elif newy > init_y[1]:		
			self_y = init_y[1] - (newy - init_y[1])
		else:
			self._y = newy
		self._eng -= 1
		return (self._x, self._y)

	def eat(self):
		self._eng += 10 
		if self._eng > 150:
			self._eng = 150
	def getEng(self):
		return self._eng
		
class Fish(object):
	def __init__(self):
		self._x = random.randint(init_x[0], init_x[1])	
		self._y = random.randint(init_y[0], init_y[1])	
	def move(self):
		newx = self._x + random.choice([1,-1])					
		newy = self._y + random.choice([1,-1])					
		# 边界问题
		if newx < init_x[0]:
			self._x = init_x[0] - (newx - init_x[0])
		elif newx > init_x[1]:		
			self_x = init_x[1] - (newx - init_x[1])
		else:
			self._x = newx
		if newy < init_y[0]:
			self._y = init_y[0] - (newy - init_y[0])
		elif newy > init_y[1]:		
			self_y = init_y[1] - (newy - init_y[1])
		else:
			self._y = newy
		return (self._x, self._y)

t = Turtle()
fish= []
for i in range(1, 6):
	fish.append(Fish())

while True:
	if not len(fish): # 列表中的鱼对象全部被吃掉了
		print("哈哈哈哈!敢惹我龟丞相")
		break
	if not t.getEng():
		print("小龟已饿死!!!!")
		break
	pos = t.move()		
	print("tutle:{}".format(pos))
	for each_fish in fish:
		posf = each_fish.move()
		print("fish:{}".format(posf))
		if posf == pos:
			print("有一条小鱼被吃掉了!!!")
			t.eat()
			fish.remove(each_fish)

	#time.sleep(0.1)
		

