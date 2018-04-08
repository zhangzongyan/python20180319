
import logging

# 配置日志文件信息
logging.basicConfig(filename="./w4_log", format = "%(asctime)s-%(name)s-%(message)s")

def foo(s):
	s = int(s)
	return 10 / s

try:
	print(foo('0'))
except Exception as e:
	print("exception:%s" % e)
	# logging.ERROR 错误级别 DEBUG = 10 INFO = 20 WARNING = 30 ERROR = 40 CRITICAL = 50
	logging.log(logging.ERROR, e)

