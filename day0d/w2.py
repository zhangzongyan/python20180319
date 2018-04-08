

def foo(s):
	if s == 1: #伪装异常
		raise ValueError("1做除数没有什么问题,这只是一个测试")
	return 10 / s

def bar(s):
	return foo(s) * 2


def main():
	n = input()	
	try:
		print(bar(int(n)))
	except ZeroDivisionError as e:
		print("exception: %s" % e)
	except ValueError as e:
		print("exception: %s" % e)
		raise ZeroDivisionError("哈哈哈哈 谎报军情")  #对于不能处理的异常,建议raise向上抛 
		#允许抛出,与捕获的异常不一样的异常,但不相关的错误,不要随意乱抛
	finally:
		print("End")

main()

