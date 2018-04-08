
import sys
import os
import pickle
from enum import Enum, unique

class Person(object):
	def __init__(self, name, tel):
		self._name = name
		self._tel = tel
	def showContactsInfo(self):
		print("name:{}, tel:{}".format(self._name, self._tel))
	def setName(self, name):
		self._name = name
	def setTel(self, tel):
		self._tel = tel

class PhoneBook(object):
	def __init__(self):
		#创建一个字典--->存储所有Person对象
		# python xxx.py books	
		if len(sys.argv) < 2:
			print("you should mark you phonebook")
			sys.exit(100)
		else:
			# sys.argv[1]就是我们的电话本文件	
			try:
				if os.path.exists(sys.argv[1]) == True:
					#电话本文件已存在---->读出联系人信息--->存到字典中	
					with open(sys.argv[1], "rb") as f:
						self.pbdic = pickle.load(f)   #pbdic存放已有联系人的字典
				else:
					#电话本不存在
					self.pbdic = {} #空字典
					print("this is a debug")
			except EOFError:
				#有电话本文件,但是一个空文件
				self.pbdic = {}

	def addPerson(self, name, person):
		# 添加的联系人是否存在
		for key in self.pbdic.keys():
			if key == name:
				# 电话本中已有名字为name的联系人
				print("您添加的联系人已存在")
				return
		self.pbdic[name] = person
		print("联系人:{}已经成功添加到您的电话本".format(name))

	def deletePerson(self, name):
		for key in self.pbdic.keys():
			if key == name:
				self.pbdic.pop(key)			
				print("{}已删除".format(key))
				return
		else:
			print("电话本中没有你要删除的联系人")

	def updateNamePerson(self, name, newname):
		if name == newname:
			#print("你的联系人姓名并未修改!!!!!")
			#return
			raise ValueError("你瞎传递什么呢")		
		for key in self.pbdic.keys():
			if key == name:
				self.pbdic[key].setName(newname)
				key = newname
				return
		else:
			print("您要修改的联系人不存在")

	def updatePersonTel(self, name, newtel):
		for key in self.pbdic.keys():
			if key == name:
				self.pbdic[key].setTel(newtel)
				return
		else:
			print("您要修改的联系人不存在")

	def findPerson(self, name):
		for key in self.pbdic.keys():
			if key == name:
				print("找到了您要找的联系人:")
				self.pbdic[key].showContactsInfo()
				return
		else:
			print("查无此人")

	def showPersons(self):
		for v in self.pbdic.values():		
			v.showContactsInfo()

	#退出通讯录
	def quitBook(self):
		with open(sys.argv[1], "wb") as f:
			pickle.dump(self.pbdic, f)

	def showMenu(self):
		print('''
			****************欢迎使用电话本系统*************
			1.添加联系人
			2.删除联系人
			3.修改联系人信息
			4.查找联系人
			5.显示所有联系人
			9.退出电话本系统
''')

# 将电话本功能枚举
@unique
class Menu(Enum):
	ADD = 1
	DELETE = 2
	UPDATE = 3
	FIND = 4
	SHOW = 5
	QUIT = 9
@unique
class Update(Enum):
	UPDATENAME = 1
	UPDATETEL = 2

if __name__ == "__main__":
	myphone = PhoneBook()
	
	while True:
		myphone.showMenu()	
		choose = input("请输入你的选择")
		choose = int(choose)
		if choose == Menu.ADD.value:
			name = input("请输入你要添加的联系人姓名:")
			tel = input("请输入新联系人的电话号码:")
			p = Person(name, tel)
			myphone.addPerson(name, p)
		elif choose == Menu.DELETE.value:
			name = input("你要删除的用户是:")	
			myphone.deletePerson(name)
		elif choose == Menu.UPDATE.value:
			print("1.修改联系人姓名 2.修改联系人电话")		
			c = int(input())
			name = input("请输入你要修改的联系人姓名:")
			if c == Update.UPDATENAME.value:
				newname = input("请输入修改后的名字:")
				try:
					myphone.updateNamePerson(name, newname)
				except ValueError:
					print("你输入的名字不正确")
			elif c == Update.UPDATETEL.value:
				newtel = input("请输入此联系人的新号码:")
				myphone.updatePersonTel(name, newtel)
			else:
				print("操作错误")	
		elif choose == Menu.FIND.value:
			name = input("输入你要查找的姓名:")
			myphone.findPerson(name)
		elif choose == Menu.SHOW.value:
			myphone.showPersons()
		elif choose == Menu.QUIT.value:
			myphone.quitBook()
			print("***************感谢使用此电话本管理系统***********************")
			break





