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
#实例化按钮对象
bt = tkinter.Button(mytk, text = "发送", command = buttonfun).pack()
lb = tkinter.Listbox(mytk, width=70, height=2)
lb.insert(tkinter.END, "你好啊") #向listbox 最后插入一个字符
lb.insert(tkinter.END, "还好吧")
#lb.delete(0) #删除从start(0)开始,到end为止 (start, end = None)
for l in ['hello', 'python', 'uplooking']:
    lb.insert(tkinter.END, l)

#滚动条
roll = tkinter.Scrollbar(mytk)

#绑定列表框 和 滚动条
lb['yscrollcommand'] = roll.set
roll['command'] = lb.yview
lb.pack()
#使得滚动条在右边, 并且高度填充
roll.pack(side = tkinter.RIGHT, fill=tkinter.Y)

# 使得窗口不关闭则已知存在
mytk.mainloop()
