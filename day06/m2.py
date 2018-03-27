
# 简介time模块的用法

import time

# 时间戳
t = time.time()
#print(t)

# 将时间戳转换为时间结构
#tl = time.localtime(t)
tl = time.localtime(988888888.8888)
#print(tl)

time.sleep(1.5)

# 将时间结构转换为时间字符串
ts = time.strftime("%Y-%m-%d %H:%M:%S", tl)
print(ts)

