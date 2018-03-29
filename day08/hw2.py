
'''
计算l = ["172.16.3.1", “172.16.1.5”, “172.15.2.0”, “172.16.3.1”, “172.16.3.1”, “172.16.1.5”]
不需要定义函数，统计在此列表中每一个ip出现的次数，并输出出现频率最高的成员
'''
l = ["172.16.3.1", "172.16.1.5", "172.15.2.0", "172.16.3.1", "172.16.3.1", "172.16.1.5", "172.16.1.5"]
s = set(l)
ls = list(s) #ls列表中的所有的元素不重复
d = dict()

for i in ls:
	n = l.count(i)
	d[i] = n
print(d)
res = []
#print(d.keys())
max_cnt = -1
for k in d.keys():
	if d[k] == max_cnt:
		res.append(k)
	elif d[k] > max_cnt:
		res = []
		res.append(k)	
		max_cnt = d[k]
print(res)


