

# 字典(dict)：有0个或多个(key, value)组成的无序序列

# 空字典
d = dict()
print(type(d))

d2 = {"前景色":"red", "背景色":"blue"}
print(d2)

# 查 字典无序，所以无index
print(d2["前景色"])

print("{:#^10}".format("key"))
# 获得字典中所有的key
for key in d2.keys():
	print(key)
	print(d2[key])

print("{:#^10}".format("value"))
for value in d2.values():
	print(value)

print("{:#^10}".format("item"))
for item in d2.items():
	print(item)


# 改
d2["前景色"] = "yellow"
print(d2)

# 增
d2["字体颜色"] = "purple"
print(d2)

print("{:#^20}".format("delete"))
# 删除
d2.pop("前景色")
print(d2)

print(d2.pop("新颜色", -10))
print(d2)

# 检验字典中是否含有某一个key
print("python" in d2)
print("背景色" in d2)

print(d2.get("python", -1))
print(d2.get("背景色", -1)) #如果字典中有key“背景色”则返回对应的value，如果没有返回-1,默认返回None


# 注意：字典中的Key一定是不可变对象(整型数，浮点数，元祖，字符串) value 没要求

#key = [1,2]
key = (1,2)
d2[key] = [11,22,33] 
print(d2)
d2[3] = "test"
d2[5.8] = "test2"
print(d2)

num = 10
d2[num] = "integer"
print(d2)

num = 20
print(d2)

