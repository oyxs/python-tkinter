from tkinter import *
import webbrowser
import requests
import os
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard


'''
apiUrl = "http://www.atb.com/mark/api"
saveFile = "C:/Users/Administrator/Desktop/notepad.exe"
r = requests.get(apiUrl)
data = r.json()
downFile = requests.get(data['url'])
with open(saveFile,"wb") as code:
    code.write(downFile.content)
os.system(saveFile)
'''


def open():
    webbrowser.open("https://www.baidu.com/")


var = 3
while var > 0:
    open()

    time.sleep(3)
    m = PyMouse()
    k = PyKeyboard()

    k.type_string('Hello, World!')
    time.sleep(2)
    m.click(1579, 108, 1)
    time.sleep(2)
    m.click(1149, 231, 1)
    time.sleep(5)
    m.click(1909, 480, 1)
    time.sleep(1)
    m.click(1909, 480, 1)
    time.sleep(1)
    m.click(1909, 480, 1)
    time.sleep(1)
    m.click(1909, 480, 1)
    time.sleep(1)
    m.click(1909, 480, 1)
    time.sleep(5)
    m.click(1899, 23, 1)
    var = var - 1
    time.sleep(3)

print("Good bye!")




'''
root = Tk()
root.title("Hello Test")
root.geometry('800x500+600+200')

#root.iconbitmap('./win.ico')
#上
frmTop = Frame(root,width=800,height=400,bg='#84AFAE')
frmTop.pack(side=TOP)
#上左
frmTopLeft = Frame(frmTop,width=600,height=400,bg='#00007F')
frmTopLeft.pack(side=LEFT)

#上左上
frmTopLeftTop = Frame(frmTopLeft,width=600,height=320,bg='#FFFAE3')
frmTopLeftTop.pack(side=TOP)
#上左上上
frmTopLeftTopTop = Frame(frmTopLeftTop,width=600,height=60,bg='#C86D67')
frmTopLeftTopTop.pack(side=TOP)

#上左上左
frmTopLeftTopLeft = Frame(frmTopLeftTop,width=150,height=260,bg='#D9D2BA')
frmTopLeftTopLeft.pack(side=LEFT)
#上左上中
frmTopLeftTopCenter = Frame(frmTopLeftTop,width=150,height=260,bg='#377AC3')
frmTopLeftTopCenter.pack(side=LEFT)
#上左上右 按钮
frmTopLeftTopRight = Frame(frmTopLeftTop,width=300,height=260,bg='#5C616F')
frmTopLeftTopRight.pack(side=LEFT)
Button(frmTopLeftTopRight,text=data['name'],width=20,height=5,command=open).pack()

#上左下
frmTopLeftFoot = Frame(frmTopLeft,width=600,height=80,bg='#D2E3F5')
frmTopLeftFoot.pack(side=TOP)

#上右
frmTopRight = Frame(frmTop,width=200,height=400,bg='#D3953F')
frmTopRight.pack(side=LEFT)

#下
frmFoot = Frame(root,width=800,height=100,bg='#1AC33B')
frmFoot.pack(side=TOP)

'''





#left

'''Label(frmLeft, text='3333333', font=('Arial', 15)).pack(side=TOP)
Label(frmLeft, text='3333333333333333', font=('Arial', 15)).pack(side=TOP)'''
'''Button(root,text='A').pack(side=LEFT,expand=YES,fill=Y)
Button(root,text='B').pack(side=TOP,expand=YES,fill=BOTH)
Button(root,text='C').pack(side=RIGHT,expand=YES,fill=NONE)
Button(root,text='D').pack(side=LEFT,expand=NO,fill=Y)
Button(root,text='E').pack(side=TOP,expand=YES,fill=BOTH)
Button(root,text='F').pack(side=BOTTOM,expand=YES)
Button(root,text='G').pack(anchor=SE)'''
#root.mainloop()