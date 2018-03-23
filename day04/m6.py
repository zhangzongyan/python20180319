

# 字符串: ""/ ''由一个或多个字符组成的

name = "caohuan" # unicode
school = 'hua\
dian'
item = '''计算机科学
与技术系'''  

专业 = "软件工程" #不建议

print(name, school, item, 专业)

# 字符串中每一个字符的索引从0开始
stu = "么济恺希雅abc"

# stu[start:end:step]
print("****************************")
print(stu)
print("{}".format(stu[0:]))
print("{}".format(stu[0::3]))
print("{}".format(stu[-1:0:-3]))
print("****************************")

print("{}大人,好好学习".format(stu[0]))
print("{}同志，辛苦了".format(stu[1:]))
print("{}好同学哈哈，你是最帅的".format(stu[1:-3])) #在序列中[a, b]  a<= <b
print("{}同志，辛苦了".format(stu[5::-3])) #在序列中[a, b]  a[5] 从a[5]倒叙数到-3
print("{}同志，辛苦了".format(stu[-1]))

#stu[2] = "欢" 字符串是个常量，不能改变

# 与字符串相关联的运算符
statement = "python"

stu += statement
print(stu)
print(stu+statement)  #连接
print(10 * statement)  #复制
statement *= 5
print(statement)  

# BIF
print(len(statement))

s2 = statement.upper() #大写
print(s2, statement)

print(s2.lower()) #小写

stringS1 = "大家好 我是reala 我最爱语言就是    python"
print(stringS1.split())
print(stringS1.split(sep="是"))  #分割字符串， sep指明分隔符

#format方法
mystrf = "学好Python"
fstr = "改变世界"
print("{},你就能{}".format(mystrf, fstr)) #{}槽
print("{1},你就能{0}".format(mystrf, fstr)) #{}槽

# "学好Python          "
print("{0:20}".format(mystrf))  #左对齐
print("{0:>20}".format(mystrf)) #右对齐
print("{0:^20}".format(mystrf)) #居中对齐
print("{0:*^20}".format(mystrf)) #居中对齐，并补*
print("{0:+^20}".format(mystrf))

# 按进制输出整型
mynum = 11
print("{0:b}, {0:d}, {0:o}, {0:x}, {0:X}".format(mynum))

# 浮点
myfloat = 1.2345
print("{0:.2f}".format(myfloat))
print("{0:.2}".format("hello"))








