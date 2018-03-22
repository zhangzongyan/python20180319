
# 求得100的前n项和

# 将1到100累加起来 ---》结果打印

# 定义累加器
sum_res = 0
num = 100

while num > 0:
	# 如果是偶数则累加---->if    %
	if num % 2 == 0:
		sum_res = sum_res + num
	num = num - 1

#print("100的前n项和是", sum_res)
print("100的前n项偶数和是", sum_res)

