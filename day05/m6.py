
# -*- coding=utf-8 -*-

# 凯撒密码
'''
	  97                119 120 121 122
源码: abcdefghijklmn..uvwxyz
加密: defghijklmn.....  zabc
(SRC + 3) % 26

ord("A") ---> 65

ASCII---->127
"a" --->97
"A" --->65

GB2312 ---->2byte

世界编码:
	UNICODE---->2byte / 4byte
最推荐:UTF-8

'''

# print(ord('A'))
passwd = input("输入你要发送的密码为多少?")
# "abcd" "defg"
for s in passwd:
	if ord('a')<= ord(s) <= ord('z'):
		res = ord(s)+3
		if res > ord('z'):
			res -= 26	
		print("%s" % chr(res), end=" ")
print("")


for i in range(len(passwd)):
	print(passwd[i])






