
import e2

def dayofweek(year, month):
	# 1990.1.1 ~ year.month.1有多少天	
	sumdays = 0
	# 1990.1.1 ～ year-1
	for i in range(1990, year):
		if e2.isleap(i) == 1:
			sumdays += 366
		else:
			sumdays += 365
	# year.1.1 到 year.month.1（不包含1号）
	for i in range(1, month):
		sumdays += e2.dayofmonth(i, year)
	# year.mont.1
	sumdays += 1
	return sumdays % 7

if __name__ == "__main__":
	y, m = eval(input("请输入日期(y, m)"))
	d = dayofweek(y, m)
	print("{}/{}的1号是星期{}".format(y, m, d))


