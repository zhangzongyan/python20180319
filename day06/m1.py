
# random模块的简介

import random

# 产生一个0到1之间数值 [0.0, 1.0)
print(random.random())

#随进产生一个[10, 20]之间的整数
print(random.randint(10, 20))

for i in range(1, 11):
	#[10,20) step=2
	print(random.randrange(10, 20, 2))

# [10, 20)浮点
print("{:.2f}".format(random.uniform(10, 20)))

