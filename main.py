#coding:utf8
##ax^2+bx+c=0
##d=b^2-4ac
##sqrt(d)
import math
import Tkinter as tk
def click(event):
    try:
        a = int(entrya.get())
    except BaseException:
        a=0
    try:
        b = int(entryb.get())
    except BaseException:
        b=0
    try:
        c = int(entryc.get())
    except BaseException:
        c=0
    d=(b**2)-(4*a*c)
    x1=0.1
    x2=0.1
    if d>0:
        try:
            x1=(-b-math.sqrt(d))/(2*a)
            x2=(-b+math.sqrt(d))/(2*a)
        except ZeroDivisionError:
            try:
                x1=c/b
                x2 = 'Идиентичен x1'
            except ZeroDivisionError:
                x1='Не существует'
                x2='Не существует'
    elif d==0:
        try:
            x1=(-b)/(2*a)
            x2='Идиентичен x1'
        except ZeroDivisionError:
            try:
                x1=c/b
                x2 = 'Идиентичен x1'
            except ZeroDivisionError:
                x1 = 'Не существует'
                x2 = 'Не существует'
    else:
        x1='Не существует'
        x2='Не существует'
    label_x1["text"]='x1='+str(x1)
    label_x2["text"]='x2='+str(x2)
if __name__=="__main__":
    window=tk.Tk()

    frame=tk.Frame(master=window,width=400,height=100)
    frame.pack()

    hello=tk.Label(master=frame,text="Привет, это приложения для решения уровнения")
    hello.place(x=0,y=0)

    entrya = tk.Entry(width=3)
    entrya.place(x=0,y=20)

    label1=tk.Label(master=frame,text='x²+')
    label1.place(x=33,y=20)

    entryb = tk.Entry(width=3)
    entryb.place(x=60, y=20)

    label2 = tk.Label(master=frame, text='x+')
    label2.place(x=93, y=20)

    entryc = tk.Entry(width=3)
    entryc.place(x=115, y=20)

    label2 = tk.Label(master=frame, text='=0')
    label2.place(x=148, y=20)

    label_x1=tk.Label(master=frame, text='x1=')
    label_x1.place(x=200, y=20)

    label_x2 = tk.Label(master=frame, text='x2=')
    label_x2.place(x=200, y=40)
    button=tk.Button(text="Посчитать")
    button.bind("<Button-1>",click)
    button.place(x=60,y=50)

    window.mainloop()
