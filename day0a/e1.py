

for i in [1,2,3,4,5]:
	print(i)

f = iter([1,2,3,4,5])

while True:
	try:
		print(next(f))
	except StopIteration:
		break
print("所有的都完成了")

