
import e2_extend
import e2

def mycal(year, month):
	l_m = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"]
	print("{}{}月{}年".format(" "*12,l_m[month-1], year))
	print("日  ","一  ", "二  ", "三  ", "四  ", "五  ", "六")
	
	# 得出month.1是星期几
	weekn = e2_extend.dayofweek(year, month)
	# 控制打印1号之前的空格的个数		
	print("{}".format("     "*weekn), end="")
	# 求出Month月有多少天
	days = e2.dayofmonth(month, year)
	for d in range(1, days+1):
		print("{:2}".format(d), end = "")
		if (weekn + d) % 7 == 0:
			print("")
		else:
			print("   ", end="")
	print("")
	


if __name__=='__main__':
	y, m = eval(input("{year,month]:"))
	mycal(y, m)


