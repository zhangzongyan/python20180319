'''
作者: zhangzongyan
时间: 18-4-12
功能: tkinter图形开发
'''
import tkinter

def buttonfun():
    print("大家休息一下吧")

#创建一个窗口
mytk = tkinter.Tk()
#设置窗口的标题
mytk.title("这是我的第一个窗口")
#设置窗体大小
mytk.geometry("800x600")
# 创建一个Frame框架
fm = tkinter.Frame()
# 创建的聊天列表框
lb = tkinter.Listbox(fm, width=70, height=2)
lb.insert(tkinter.END, "你好啊") #向listbox 最后插入一个字符
lb.insert(tkinter.END, "还好吧")
#lb.delete(0) #删除从start(0)开始,到end为止 (start, end = None)
for l in ['hello', 'python', 'uplooking']:
    lb.insert(tkinter.END, l)
#滚动条
roll = tkinter.Scrollbar(fm)
#绑定列表框 和 滚动条
lb['yscrollcommand'] = roll.set
roll['command'] = lb.yview
lb.pack(side = tkinter.LEFT, expand = 1, fill=tkinter.BOTH)
#使得滚动条在右边, 并且高度填充
roll.pack(side = tkinter.RIGHT, fill=tkinter.Y)
fm.pack(expand = 1, fill = tkinter.BOTH)
roll.pack()
#第二个框架
fm2 = tkinter.Frame()
tx = tkinter.Text(fm2).pack(expand = 1, fill = tkinter.X)
fm2.pack(expand = 1, fill = tkinter.BOTH)
#第三个框架---->发送
fm3 = tkinter.Frame()
#实例化按钮对象
bt = tkinter.Button(fm3, text = "发送", command = buttonfun).pack()
fm3.pack()
# 使得窗口不关闭则已知存在
mytk.mainloop()
