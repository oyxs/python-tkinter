import tkinter as tk
root = tk.Tk()
root.title("Hello Test")
root.geometry('800x500+600+200')
root.iconbitmap('D:\\www\\scrapy\\new\\grammar\\win.ico')

labelHello = tk.Label(root, text = "Hello Tkinter!",bg = "green").pack()


root.mainloop()
