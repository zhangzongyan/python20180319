
# python异常处理

try:
	r = 10 / 0
	print("r = %d" % r)
except (ValueError, ZeroDivisionError):
	print("value error")

'''
except ZeroDivisionError:
	print("zero can not be division")

'''



