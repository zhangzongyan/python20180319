
# 这是单行注释

'''
这是一个多行注释
在一行
'''
print(1 + 100)
# 输出多个内容，以逗号分开 sep指明多个输出内容分隔符  end指明结束符
print("1+100", 1+100, sep="=", end="this is my first python")

# *10将字符串复制10次
print("你是最棒的" * 10)
# 拼接 拼接的内容必须在""内
print("你是最棒的" + "10")


# python不允许将一条语句直接写在两行，如果要提高代码阅读性，换行则加\
print("你今天心情怎么样啊？你中午吃什么啊？\
明天放假了吧 可是我还要上课")

print('''你今天心情怎么样啊？你中午吃什么啊？
明天放假了吧 可是我还要上课''')

# 不推荐将两条语句在同一行，如果有需求，加;
print("你好"); print("同学们")

# '\'开头的称为转义字符 \t制表符  \n换行
print("good morning", end='\t')
print("good morning \"classes\"", end='\t')
print('good morning "classes"', end='\t')
print("good morning \"classes\" \\thello ", end='\t')





