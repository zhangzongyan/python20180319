
'''
让用户输入他的体重(kg)和身高(m),判断他的BMI，根据他的BMI指标合理的给出建议
BMI = 体重 / 身高*身高
 BMI < 18.5    “你这么瘦,可以肆无忌惮的大吃大喝啦"
 18.5 <= BMI < 25  “兄弟！你离模特就差八块腹肌了”
 25 <= BMI < 30  “控制你自己哦！脂肪有点多啦”
 BMI >= 30   “不能再吃了！跑几圈去吧，你也可以是男神” 
'''

'''
weight = float(input("请输入你的体重(kg)"))
height = float(input("请输入你的身高(kg)"))

#bmi = weight / (height * height)
bmi = weight / pow(height, 2)
if bmi < 18.5:
	print("你这么瘦,可以肆无忌惮的大吃大喝啦")
elif 18.5 <= bmi < 25:
	print("兄弟！你离模特就差八块腹肌了")
elif 25<= bmi and bmi < 30:
	print("控制你自己哦！脂肪有点多啦")
else:
	print("不能再吃了！跑几圈去吧，你也可以是男神")
'''

'''
判断从你出生到今年共有多少的闰年
'''
'''
myyear = int(input("你是哪年出生的呀?"))

count = 0
for year in range(myyear, 2019):
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
		count += 1
else:
	print("{}到今年共有{}个闰年".format(myyear, count))
'''

# 输入一个三位整型数，判断它是否是一个水仙花数(比如153 = 1*1*1 + 5*5*5 + 3*3*3)
# 计算出有多少个水仙花数 

#number = int(input("请输入一个三位整型数"))
'''
count_sxh = 0
for number in range(100, 1000):
	save = number
	n = 0 #统计number有多少位
	sumn = 0
	
	while number > 0:
		tmp = number % 10
		sumn += pow(tmp, 3)
		number //= 10
		n += 1
	else:
		#循环正常终止的
		if n != 3:
			print("你咋这么不听话呢？")
		else:
			if sumn == save:
				print("{}是一个水仙花数".format(save))
				count_sxh += 1
			else:
				#print("{}不是一个水仙花数".format(save))
				pass
	
else:
	print("所有的三位水仙花数共%d个" % count_sxh)
'''
'''
4.读入用户输入的一个日期(年，月， 日)，判断这一天是这年的第几天
'''
'''
year = int(input("year:"))
month = int(input("month:"))
day = int(input("day:"))

sumdays = 0
for m in range(1, month):
	if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
		sumdays += 31 
	elif m == 4 or m == 6 or m == 9 or m == 11:
		sumdays += 30
	elif m == 2:
		if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
			sumdays += 29
		else:
			sumdays += 28
	else:
		break
else:
	sumdays += day	
	print("{}/{}/{}是{}的第{}天".format(year, month, day, year, sumdays))
'''
'''
5.读入用户输入的一个字符串，判断字符串中有多少个大写字母，多少个数字，多少个小写字母
提示：
    判断一个字符串是否是数字：isdigit()  例如"1".isdigit()为True
    得到单个字符串对应的值 ord("A") == 65
'''
mystr = input("请输入字符串")

dig_cnt, up_cnt, low_cnt = 0, 0, 0
for s in mystr:
	if s.isdigit() == True:
		dig_cnt += 1	
	elif ord(s) >= ord("A") and ord(s) <= ord('Z'):
		up_cnt += 1
	elif s.islower() == True:
		low_cnt += 1
	else:
		pass
else:
	print("{}中包含{}数字{}大写{}小写".format(mystr, dig_cnt, up_cnt, low_cnt))





