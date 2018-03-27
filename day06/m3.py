

# 模拟进度条

import time

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))


bps = 0 #百分比
scale = 10

for i in range(scale+1):
	a = i*"##"	#已完成
	b = (scale-i)*"--"
	bps = (i / scale) * 100
	print("\r{:^3.0f}% [{}->{}]".format(bps, a, b), end='')
	time.sleep(0.1)
	
print("")

