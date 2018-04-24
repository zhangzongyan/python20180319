'''
作者: zhangzongyan
时间: 18-4-24
'''
import re

'00\d' #'001' '002' '007'
'\d\d\d' #任意三位数字字符
'\w\w\w\d' #前三位是[a-zA-Z0-9_]第四位是数字
'python.' #
'\d{3}\s+\d{2,8}'
'[a-z0-9A-Z\_]' # 'a' '_'
'[a-z0-9A-Z\_]+' # 'a001' 'a' 'a_123'
'[a-zA-Z\_][0-9a-zA-Z\_]*' #
'[a-zA-Z\_][0-9a-zA-Z\_]{0,20}'
'^py$'
'(p|P)ython'

# r正则 使得正则表达式完全不需考虑字符串规则 推荐使用
s = re.match(r'00\n\d', "00\n12")
print(s)

# 详谈 re模块  re.method(pattern, string)
# macth()---->在string的开头进行匹配
m = re.match(r'[a-d]{3,8}', "abjhello abcdefworldhelloworld")
print(m)

# search()--->找string中第一个与pattern匹配的
m = re.search(r'[a-d]{3,8}?', "abjhello abcdefworldhelloworldaabbccdd")
print(m)

# findall()---->找到string中所有与pattern匹配的,返回一个列表
m = re.findall(r'[a-d]{3,8}?', "abjhello abcdefworldhelloworldaabbccdd")
print(m)

# search()--->找string中第一个与pattern匹配的
m = re.search(r'(?<=world)hello', "worldhelloabchello, worldhello")
print(m)
# findall()---->找到string中所有与pattern匹配的,返回一个列表
m = re.findall(r'(?<=world)hello', "worldhelloabchello, worldhello")
print(m)

