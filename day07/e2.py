

# 定义一个函数 实现求得任意日期对应的月份有多少天
# 参数列表 ------> 已知条件----->带求得的月份和年份(2月有多少天取决于年)
# 返回值  ------->结果-----> return 求得的天数

def isleap(year):
	if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
		return 1
	return 0

def dayofmonth(month, year):
	days = 0

	if month in (1,3,5,7,8,10,12):
		days = 31
	elif month in (4,6,9,11):
		days = 30
	elif month == 2:
		days = 28 + isleap(year)	
	else:
		days = -1

	return days

if __name__ == "__main__":
	y, m = eval(input("请输入年份和月份(year, month):"))
	print("{}/{} 有{}天".format(y, m, dayofmonth(m, y)))




