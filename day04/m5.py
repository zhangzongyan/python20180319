

# 运算符

a, b = 10, 15

print(b / a)
print(b // a)


print(a > b and b) # “短路逻辑”
print(a < b and b) # a < b为真,and表达式的值取决于b

print(a or b) 
print(not a or b) 

print(a ** b) #pow(a, b)

a += b # a = a + b
print(a, b)

# 以下两种方式 效果一样的
print(2< a < 15)
print(a > 2 and a < 15)

#b = a
b = 25
c = 25
print(a is b)
print(b is not c)

