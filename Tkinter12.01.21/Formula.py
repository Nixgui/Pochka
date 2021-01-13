from tkinter import *
from math import *
root=Tk()
root.title("Решение уровнения")
root.geometry("500x400")
#
def text_to_lbl(event):
    global d,x1,x2,x
    a=int(enta.get())
    print(a)
    enta.delete(0, END)
    b=int(entb.get())
    print(b)
    entb.delete(0, END)
    c=int(entc.get())
    print(c)
    entc.delete(0, END)
    d=(b**2)-4*a*c
    print(d)
    lbl1["text"] = d
    if d>0:
        lblx.grid_remove()
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        rx1=round(x1,1)
        rx2=round(x2,1)
        lblx1["text"] = f"X1: {rx1}"
        lblx2["text"] = f"X2: {rx2}"
        lblx1.grid()
        lblx2.grid()
    elif d==0:
        lblx1.grid_remove()
        lblx2.grid_remove()
        x= (-b / 2*a)
        lblx["text"] = f"x: {x}"
        lblx.grid()
    else:
        lblx.grid_remove()
        lblx1.grid_remove()
        lblx2.grid_remove()
        dd="Корень вычеслить невозможно!"
        lbl1["text"] = dd
##############################################################
lbl_formula=Label(root,text="D=b**2-4*a*c",font="Arial 20")
txta=Label(root,text="a:",font="Arial 20")
txtb=Label(root,text="b:",font="Arial 20")
txtc=Label(root,text="c:",font="Arial 20")
lbl1=Label(root,text="",font="Arial 15")
lbl2=Label(root, text="Дискременант равен: ",font="Arial 15")
enta=Entry(root) #a
entb=Entry(root) #b
entc=Entry(root) #c
btn1=Button(root, text="решение", font="Arial 15", width=15)
lblx=Label(root,text="",font="Arial 15")
lblx1=Label(root, text="",font="Arial 15")
lblx2=Label(root, text="",font="Arial 15")
#grid
lbl_formula.grid(row=0, column=0, columnspan=2,sticky="e")
txta.grid(row=1,column=0)
txtb.grid(row=2,column=0)
txtc.grid(row=3,column=0)
enta.grid(row=1,column=1,columnspan=1)
entb.grid(row=2,column=1,columnspan=1)
entc.grid(row=3,column=1,columnspan=1)
btn1.bind("<Button-1>",text_to_lbl)
btn1.grid(row=4,column=1,columnspan=1)
lbl2.grid(row=5,column=0,columnspan=2)
lbl1.grid(row=5,column=2)
lblx.grid(row=6,column=1,columnspan=5)
lblx1.grid(row=6,column=1,columnspan=5)
lblx2.grid(row=7,column=1,columnspan=5)



root.mainloop()