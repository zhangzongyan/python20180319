
import logging

# 配置日志文件信息
logging.basicConfig(filename="./w5_log", format = "%(asctime)s-%(name)s-%(message)s-%(levelname)s")

def foo(s):
	s = int(s)
	return 10 / s

try:
	print(foo('0'))
	# logging.ERROR 错误级别 DEBUG = 10 INFO = 20 WARNING = 30 ERROR = 40 CRITICAL = 50
except:
	# level--->logging.ERROR
	logging.exception("这是一个错误信息") # 将调用栈中的所有的错误信息写入日志

