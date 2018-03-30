
# 文件操作

f = open("./e1.py") # "rt"

#按字节读取 read的参数表明待读取的字节数  如果为-1表示读取整个文件
#print(f.read(10))

# 读取文件的所有行存放在列表中
'''
for line in f.readlines():
	print(line)
'''
print(f.readline())
print(f.readline())

# 读取当前偏移量
n = f.tell()

s = f.readline()
print(s)
# 读取与上一行一样的内容
'''
获取文件当前偏移量,f.tell()
	偏移量:当我们打开一个文件的时候，文件偏移量已经存在，值取决于打开方式
			打开方式如果是r/w/r+/w+ 偏移量初始值就是0
			随着文件的读写操作，偏移量会随之改变
设置文件的偏移量: f.seek(offset, whence=0)
	offset:决定偏移的字节个数
	whence:决定的是位置(0：开头，1：当前，2：末尾)
	如果文件的打开方式是t(默认),只允许在用绝对位置偏移(开头),whence=0
	如果是b方式，则相对位置也允许(whence=1 / whence = 2)

'''
f.seek(n,0)
print(f.readline())

# 按行读取文件
f.seek(0, 0)
while True:
	l = f.readline()
	if (l == ""):# 文件末尾有结束标志(EOF),当读到此结束标志时返回""
		break
	print(l)


f.close()


