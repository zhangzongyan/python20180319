'''
作者: zhangzongyan
时间: 18-4-24
'''
import re

mystr = 'hello_girls1 every one , you are the best boy'
m = re.match(r'h\w+', mystr)
print(m.group()) # 获取与之匹配的字符串
print(m.groups()) # 获取组中匹配, 未分组,为空

# ()分组
m = re.match(r'h(\w+)([a-z]{2})', mystr)
print(m.group()) # 获取所有匹配结果
print(m.groups()) # 获取匹配结果,显示分组
print(m.groupdict()) # 未指定key 字典为空

# ()分组
m = re.match(r'h(?P<k1>\w+)(?P<k2>[a-z]{2})', mystr) # '(?P<key>)' 指明结果字典的key
print(m.group()) # 获取所有匹配结果
print(m.groups()) # 获取匹配结果,显示分组
print(m.groupdict()) # 获取匹配结果字典



