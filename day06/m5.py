
#建议使用中，如果能用tuple替换list，则替换，以保证数据安全

# tuple :元祖是一旦初始化后，成员不能改变的序列
t = tuple()
print(type(t))
l = [1, "你好", 100]
t2 = tuple(l)
print(t2)

# 空元祖
t3 = ()
print(type(t3))

# t4 = (1)  t4是一个整型
# 元祖内,号才是元祖的符号
t4 = (1,)
print(type(t4))

# 利用元祖实现两个数的交换
a = 100
b = 200
a, b = b, a #(200, 100)
print(a, b)

#
tnew = (1, 2, 3, 2, 1, 7, 9, 2, 1)
print(tnew.count(1)) #统计元祖tnew中所有1的个数
print(tnew.index(2, 1, 5)) #得到从下标1到下标5第一次出现值2的索引
#tnew[1] = 100 元祖是不可变的









