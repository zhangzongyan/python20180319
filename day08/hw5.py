

'''
定义一个函数，判断用户输入的成绩所属于的等级
   1) 90~100：A
   2) 80~89 :B
   3) 70~79:C
   4) 60~69:D
   5) 0~59:E
'''


def get_level(grade):
	if grade >100 or grade < 0:
		return -1
	level = ['E', 'E', 'E', 'E', 'E', 'E', 'D', 'C', 'B', 'A', 'A']
	return level[grade//10]	

if __name__ == "__main__":
	yougrade = int(input("请输入你的成绩"))
	print(get_level(yougrade))



