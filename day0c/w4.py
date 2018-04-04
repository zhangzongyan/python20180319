

'枚举类'
JAN = 1 #不推荐此方法进行枚举 JAN本质还是一个变量


JAN = 2
month = JAN
print(month)

# 枚举类模块
from enum import Enum, unique

#枚举一个月份类Enum(类名,(枚举成员))  枚举的值默认从1开始
month = Enum('MONTH', ("JAN", "FEB", "MAR"))
print(month.__members__)
for name, member in month.__members__.items():
	print(name, member, member.value)

@unique  #确保定义的枚举类型中的每一个成员不重复
class Week(Enum):
	SUN = 0
	MON = 1
	THU = 22
	WED = 3 
	THR = 4
	FRI = 5
	SAT = 6

# 访问定义的枚举类中的枚举成员
print(Week.SUN.value)
print(Week.WED.value)
print(Week['SAT'].value)
print(Week(22)) #获取值为22的枚举成员
#Week.SUN.value = 100 错误的 不能改变枚举成员的值


