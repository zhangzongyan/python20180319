


def foo(s):
	s = int(s)
	# 断言 s!=0为True 正常运行  python解释器在解释程序期间,可以通过参数-O关闭断言
	assert s != 0, "0 can not be division"
	return 10 / s

try:
	print(foo('0'))
except AssertionError as e:
	print("exception:%s" % e)


