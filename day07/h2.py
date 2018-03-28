
import random 

num = random.randint(1, 100)
print("{}的二进制是:".format(num), end="")
l = []

while num > 0:
	l.append(num % 2)
	num //= 2
	
l.reverse()

for i in range(0,len(l)): #index(l[-1])+1
	print(l[i], end="")
print("")


'''
stra = "abc"
print(stra.replace("a", "A"))
print(stra)
'''

