import tkinter as tk
top = tk.Tk()
top.title("Hello Test")
top.geometry('800x500+600+200')
top.iconbitmap('D:\\www\\scrapy\\new\\grammar\\win.ico')

labelHello = tk.Label(top, text = "Hello Tkinter!",bg = "green").pack()


top.mainloop()
