

# 高阶函数:函数通过参数传入的方式称为高阶函数

def sum2abs(a, b, f):
	return f(a) + f(b)


n = abs(-10)
print(n)

# abs 函数名
xiaopang  = abs
print(xiaopang(-100))

'''
abs = 10  #这是允许的  但不要这么做
print(abs + 100)
'''
print(sum2abs(5, -6, abs))
print(sum2abs(100, 120, str))

# 常用的高阶函数之 map
def mypow(x, y = 2):
	return pow(x, y)

import collections

r = map(mypow, [1,2,3,4,5,6])
print(isinstance(r, collections.Iterator))
#l = list(r)
#print(l)

# r是一个迭代器,只能遍历一次
while True:
	try:
		print(next(r))
	except:
		break
#print(next(r))

# 练习1:将整型数列表[1,2,3,4,5,6]转换为字符串列表['1', '2', '3', '4', '5', '6']
print(list(map(str,[x for x in range(1,7)])))

# reduce
from functools import reduce

r = reduce(lambda x, y : x + y, (1,3,5,7,9))
print(r)

# 练习2:将字符串"12345"转换为整型数12345
# 1,2,3,4,5
print(reduce(lambda x, y : x*10 + y, map(lambda x : ord(x) - ord('0'), "12345")))
# reduce(f, (1,2,3,4,5)) f(f(f(f(1, 2), 3), 4), 5)

# filter:过滤所有调用给定的函数为False
def isEven(x):
	return x % 2 == 0
f = filter(isEven, [x for x in range(1, 101)])
print(list(f))

# 练习3:有一个列表["helo", "", "1", "2", "   ", "\n"]
# "  abc".strip()  "abc"
def not_emptystr(s):
	return s and s.strip()
print(list(filter(not_emptystr, ["helo", "", "1", "2", "   ", "\n"])))

# sorted 排序
l = [5, 2, -1, -4, 10, 6]
print(sorted(l))

#绝对值排序
print(sorted(l, key=abs))

#练习4:将["hello", "good", "study", "alice", "Petter", "HANMEIMEI"] 忽略大小写排序
print(sorted(["hello", "good", "study", "alice", "Petter", "HANMEIMEI"], key = str.lower, reverse=True))



