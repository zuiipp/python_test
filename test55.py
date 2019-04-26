#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import tkinter as tk  # 使用Tkinter前需要先导入

window = tk.Tk()

window.title('第一个GUI')

window.geometry('500x300')  # 此处乘是小x，不能用*



e1 = tk.Entry(window, show='*', font=('Arial', 14))   # 显示成密文形式
e2 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
e1.place(x=0, y=0)
e2.pack()

window.mainloop()
