
# 用户输入10个人的名字，随机选取一个人作为队长

import random

l = []
for i in range(10):
	l.append(input("请输入第{}个候选人名字:".format(i+1)))


print("恭喜{}！你已称为了我们的队长".format(l[random.randint(0, 9)]))

