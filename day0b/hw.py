


from operator import itemgetter

d = {"chaoqian":87, 'caoxu':90, 'caohuan':98, 'wuhan':82, 'zhijia':89}

l = [11,22,33,44,55,66]
b = itemgetter(2)
print(b(l))

l = list(d.items())
# [('chaoqian', 87), ('caoxu', 90), ('caohuan', 98), ('wuhan', 82), ('zhijia', 89)]

print(l)
print(list(sorted(l, key = itemgetter(1))))
print(list(sorted(l, key = itemgetter(0))))



