
# 列表的定义
l = []
print(type(l))
l1 = ['lucy', 'lilei', 'hanmeimei']
print(l1)

l1.sort()
print(l1)

# 迭代列表
for i in l1:
	print(i)

# 末尾增
l1.append(100)
print(l1)
l1.append(['小胖', '可爱'])
print(l1)

print("{:-^20}".format("查找"))
# 查 列表的索引从0开始的
print(l1[4][0])
print(l1[2])
print(l1[:3])
print(l1[-1])
print(l1[3:])
print(l1[1::2])


print("{:-^20}".format("增加"))
# 任意位置增
l1.insert(1, '永鹏')
print(l1)

print("{:-^20}".format("修改"))
# 改
l1[1] = '曹欢'
print(l1)

print("{:-^20}".format("删除"))
# 删
l1.pop() #末尾删除
print(l1)
l1.pop(2) #指定位置删除
print(l1)
l1.remove(100)
print(l1)

print("\n{:-^20}".format("list"))
l2 = list()
print(type(l2))
l2 = list((2, 3))
print(l2)




