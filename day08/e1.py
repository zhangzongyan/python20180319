

import datetime
import e1_module as mye
import turtle


def mytime(mytimestr):
	for i in mytimestr:
		mye.drawDigit(int(i))


if __name__ == "__main__":
	turtle.setup(800, 600, 200, 200)
	turtle.penup()
	turtle.backward(300)
	turtle.pendown()
	
	# 获取当前的年月日
	s = datetime.date.strftime(datetime.datetime.now(), "%Y%m%d")
	mytime(s)
	
	turtle.done()
	
