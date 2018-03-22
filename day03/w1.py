

# febnacii

# 0 1 1 2 3 

a = 0
b = 1

#a = b, b = a + b
#a, b = b, a+b # a, b = 1, 1
#print(a, b) #a = 1, b = 1 / b = 2

#res = a + b  1
# a = b, b = res res = a + b   2
# a = b,a == 1 ;b = res, b = 2; res = a + b  res = 3
# a = b,a == 2 ;b = res, b = 3; res = a + b  res = 5
res = 0
while res < 100: 
	res = a + b
	print(res, end=",")
	a = b
	b = res
print()

#另一种方法求得febacii
a, b = 0, 1

#a, b = b, a
#print(a, b)

while a < 100:
	print(a)
	a, b = b, a+b

