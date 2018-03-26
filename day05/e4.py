
# 字符串中如果有大写，则全部转小写，如果都是小写，则都转换为大写

mystr = input("你想说什么?")

# mystr.islower() 如果mystr中的字符都是小写则返回True
if mystr.islower() == True:
	newstr = mystr.upper()
else:
	newstr = mystr.lower()

#%s 字符串   %d 整型
print("result:%s" % newstr)
print("source:%s result:%s" % (mystr, newstr))
#print("source:{} result:{}".format(mystr, newstr))

