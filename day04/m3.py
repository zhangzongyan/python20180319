
# 变量

# 变量的名字，函数的名字统称为标识符
# 标识符的命名规范:字母、数字、下划线组成，并数字不能开头,大小写是区分的
# 建议最好变量名字都不要以_开头(在类中以_开头的变量有特殊含义)
# 标识符名字还要避开python关键字(keyword)
'''
关键字
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

# 动态语言----》定义变量的时候不需要指明类型
'''
stat = input("你饿不饿")
print("啊！{} 那我也没办法啊".format(stat))

stat = 100
print(stat)

STAT = "hello"
print(stat, STAT)
'''

# 数值类型: BIF 
num = 100  #整型integer

#num = 1.2  #浮点 100.2==>1.002 * 10^2===>1.002e2

# dir(__builtin__)查看python内置方法
h = hex(num)
print(h)

o = oct(num)
print(o)

print(abs(-100))

a, b = 10, 90
max2num = max(a, b, 100, 40, 178, 2)
print(max2num)

c = 2
print(pow(a, c)) # a ** c
print(pow(a, c, 3)) #a ** c % 3


'''
python对于数据运算专门提供了数学库（math）,所谓库称为模块
如果我们要使用ptyhon所提供的库，有以下方法
	import math
		math.fabs()
	from math import *
		fabs()
	from math import fabs, xxx
'''
from math import *

ceil_floorn = 1.93
print(ceil(ceil_floorn))
print(floor(ceil_floorn))


n = True
# 获得变量类型
print(type(n))
print(type(num))
print(isinstance(n, int))  #bool属于int
print(isinstance(n, str))









