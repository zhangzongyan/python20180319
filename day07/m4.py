

# eval函数

#得到字符串中相对应的类型
d = eval("{'k1':1, 'k2':2}")
print(d)

a, b= eval("10, 20")
print(a, b)

l = eval(input("输入一个列表"))
print(l)
print(type(l))


