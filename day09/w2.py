


f = open("new.txt", "w+")

f.write("我好饿啊") #将给定的字符串写入文件

f.seek(0, 0)
print(f.read())

l = ["你", "中午", "吃", "什么"]
f.writelines(l) #将给定的组合类型写入文件
f.seek(0, 0)
print(f.read())

f.close()



