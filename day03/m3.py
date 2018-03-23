

from turtle import *

# 设置窗口大小
setup(400, 400)

# 设置画布大小
#screensize(30, 40)

penup()
backward(50)
pendown()

color("yellow", "red")

begin_fill()
i = 0
while i < 5:
	forward(100)
	right(144)
	i = i+1
end_fill()

penup()
goto(100, 100)
pendown()
color("black", "red")
begin_fill()
circle(20, 360, steps=5)
end_fill()

done()



