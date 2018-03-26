

weeks = "星期一星期二星期三星期四星期五星期六星期日"
# 1----->星期一
# 2----->星期二
weekind = int(input("输入你心中的数字(1-7)"))
pos = (weekind-1) * 3
print(weeks[pos:pos+3])




