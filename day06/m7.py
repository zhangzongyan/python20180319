

# set 无序可变不重复

# 去重复
s = set([1,2,2,3,4,5,7,6,5,4,3,2])
print(s)

# 增
s.add(100)
print(s)

# 删
s.pop()
print(s)

s.remove(3)
print(s)

s2 = {10, 19, 5, 7, 4, 20, 25}
print(s, s2)
print(s2.difference(s))

