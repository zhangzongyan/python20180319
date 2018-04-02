# 迭代字符串
mystr = "good good study"
for s in mystr:
	print(s, end="")
print("")

i = 0
while i < len(mystr):
	print(mystr[i], end="")
	i += 1
print("")

#迭代列表
myls = [1,2,3, "hello", "boys"]
for l in myls:
	print(l, end = "")
print("")

i = 0
while i < len(myls):
	print(myls[i], end="")
	i += 1
print("")

# 获取列表中每个元素及其索引值
for i, value in enumerate(myls):
	print(i, value)

# 迭代字典
mydic = {"name":"xiya", "age":20, "score":100}
for item in mydic:
	print(item)
	print(mydic[item])
for k, v in mydic.items():
	print(k, v)

# 判断是否可迭代
import collections

print(isinstance([1,2,3], collections.Iterable))
print(isinstance("hhh", collections.Iterable))
print(isinstance(1234, collections.Iterable))
print(isinstance(1.23, int))








