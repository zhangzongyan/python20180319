
# 读取小客服和小胖的聊天记录，分别存储

import os

def write_your_file(filename, context):
		'''
		fd1 = open(filename, "w")
		fd1.writelines(context)
		fd1.close()
		'''
		with open(filename, "w") as fd1:
			fd1.writelines(context)  #不需要额外进行close()


fd = open("./e2.txt")

xiaopang_list = [] 
kefu_list = []
i = 1

if os.path.exists("./chat") != True:
	os.mkdir("./chat")
if os.path.exists("./chat/xiaopang") != True:
	os.mkdir("./chat/xiaopang")
if os.path.exists("./chat/xiaokefu") != True:
	os.mkdir("./chat/xiaokefu")

for line in fd.readlines():
	if len(line) > 2:
		if line[:6] != "======":
			(role,context) = line.split(":", 1)
			if role == "小胖":
				xiaopang_list.append(context)
			elif role == "小客服":
				kefu_list.append(context)
		else:
			#存文件
			#pass
			file1 = "./chat/xiaopang/"+"xiaopang"+str(i)+".txt"
			file2 = "./chat/xiaokefu/"+"xiaokefu"+str(i)+".txt"
			write_your_file(file1, xiaopang_list)
			write_your_file(file2, kefu_list)
			i += 1
			xiaopang_list = []
			kefu_list = []
			
#最后一次
file1 = "./chat/xiaopang/"+"xiaopang"+str(i)+".txt"
file2 = "./chat/xiaokefu/"+"xiaokefu"+str(i)+".txt"
write_your_file(file1, xiaopang_list)
write_your_file(file2, kefu_list)




