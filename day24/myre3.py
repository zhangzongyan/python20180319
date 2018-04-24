'''
作者: zhangzongyan
时间: 18-4-24
'''
import re

string = 'good after noon  abc cd12'
restr = r'a\w+'
re_obj = re.compile(restr) # 先编译为re对象
res = re_obj.search(string)  # 等效于 re.search(restr, string)
print(res.group())

print(re_obj.findall(string))

restr = r'a(\w+)[a-zA-Z\s]+(\d)'
re_obj = re.compile(restr) # 先编译为re对象
res = re_obj.search(string)  # 等效于 re.search(restr, string)
print(res.group())
print(res.groups())

#If one or more groups are present in the pattern,return a list of groups
print(re_obj.findall(string))


