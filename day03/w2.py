

import turtle

# 设置画笔宽度
turtle.pensize(8)
# 设置笔的颜色和填充的颜色
turtle.color("red", "blue")

# 开始填充
turtle.begin_fill()

# 向前画100像素点
turtle.forward(100)

# 逆时针旋转90度
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
# 结束填充
turtle.end_fill()

turtle.done()


