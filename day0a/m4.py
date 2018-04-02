
# 迭代器(Iterator):可用for遍历，并且可以使用next()函数访问每一个值
# Iterable 能使用for循环遍历(字符串，list, tuple, dict, set, generator)

from collections import Iterator, Iterable

print("列表{}可迭代的类型".format("是" if isinstance([], Iterable) else "不是"))
print("列表{}迭代器".format("是" if isinstance([], Iterator) else "不是"))

print("生成器{}可迭代的类型".format("是" if isinstance((x for x in range(10)), Iterable) else "不是"))
print("生成器{}迭代器".format("是" if isinstance((x for x in range(10)), Iterator) else "不是"))

g = iter([1,2,3,4,5,6])
#print(next(g))
for i in g:
	print(i)


