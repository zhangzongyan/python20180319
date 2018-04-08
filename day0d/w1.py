
# python异常处理

try: # 异常处理,try如论如何都会执行的
	r = 10 / int("a")  #一旦发生了异常,则会判断每一个except语句,一旦异常满足,则不会再向下判断
	print("r = %d" % r)
except Exception as e: #Exception是python常规错的基类,如果异常是Exception的子类,则会满足Exception, e是异常的错误原因 
	print("exception zero...%s " % e)

except (ValueError, ZeroDivisionError):
	print("value error")

else: # 如果所有的异常不满足,则会执行  可以没有
	print("else....")	

finally: #无论如何都会执行的,并可以没有
	print("finally.....")

print("End")


