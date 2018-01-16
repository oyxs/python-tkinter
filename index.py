from tkinter import *
root = Tk()
root.title("Hello Test")
root.geometry('800x500+600+200')

#root.iconbitmap('./win.ico')
#上
frmTop = Frame(root,width=800,height=400,bg='green')
frmTop.pack(side=TOP)
#上左
frmTopLeft = Frame(frmTop,width=600,height=400,bg='yellow')
frmTopLeft.pack(side=LEFT)

#上左上
frmTopLeftTop = Frame(frmTopLeft,width=600,height=320,bg='grey')
frmTopLeftTop.pack(side=TOP)
#上左下
frmTopLeftFoot = Frame(frmTopLeft,width=600,height=80,bg='purple')
frmTopLeftFoot.pack(side=TOP)

#上右
frmTopRight = Frame(frmTop,width=200,height=400,bg='red')
frmTopRight.pack(side=LEFT)

#下
frmFoot = Frame(root,width=800,height=100,bg='blue')
frmFoot.pack(side=TOP)






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
root.mainloop()