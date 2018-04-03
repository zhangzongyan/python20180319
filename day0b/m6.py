

# 属性获取/设置

print(type([]))
print(type((1)))

print(dir(list)) #dir(class)获取类中所有的方法

class Computer(object):
	count = 0 # 类属性
	def __init__(self, typec, name, price):
		self.typec = typec #实例属性
		self.name = name
		self.price = price	
		self.count += 1
	
	def compute(self):
		print("计算机正在飞速计算")
	def player(self):
		print("计算机正在播放电影")
	def __len__(self):
		return 10000
	def __test__(self): # 不推荐这种命名方式
		print("你累不累啊")
	def getinfo(self):
		print(self.name, self.typec, self.price)

	# 获取类属性值
	def getCount(self):
		return self.count	



'''
print(dir(Computer))
print(len(Computer()))
print(Computer().__test__())
'''
print("***********字符串*************\n")
print(dir(str))
s = "hello"
print(len(s))
print(s.__len__())

# 获取属性
# getattr(object, attr),如果attr是object对应类中的属性,则返回此属性的值
# getattr(object, attr),如果attr不是object对应类中的属性,则默认抛出异常,可以指定值通过第三个参数
c = Computer("T420", "Dell", 4000)
print(getattr(c, "price"))
print(getattr(c, "name"))
print(getattr(c, "score", -1))  

setattr(c, "name", "lenevo")
c.getinfo()
setattr(c, "socre", 100)   
print(getattr(c, "socre", -1))

# 获取类属性
print(c.getCount())

c2 = Computer("S530", "lenevo", 5000)
print(c.getCount())

