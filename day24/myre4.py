'''
作者: zhangzongyan
时间: 18-4-24
'''
import re

mystr = 'a, bc,    d,ef'
print(mystr.split(','))

res = re.split(r'\,\s*', mystr)
print(res)