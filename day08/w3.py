

# 关键字参数

def student(name, age, **kw):
	print("name:",name, "age", age, "kw", kw)

#命名关键字参数
def person(name, age, *, city, height):
	print("name:", name, "age:", age, "city:", city, "height", height)

def otherperson(name, age, *arg, city, height = 170):
	print("name", name, "age", age)	
	for a in arg:
		print(a, end=" ")
	print("")
	print("city", city, "height", height)

if __name__ == "__main__":
	student("李飞", 24, height=180, weight=60, city="河北", school="华电")
	
	person("张起", 24, city = "beijing", height = 186)

	otherperson("曹欢", 23,1, 2,3,4, city = "邢台", height = 180)
	otherperson("小沈阳", 23,1, 2,3,4, city = "邢台")



