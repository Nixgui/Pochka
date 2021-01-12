from tkinter import *
from PIL import ImageTk, Image
from Function import *
from math import *
def text_to_lbl(event):
    global d,x1,x2,x
    b=int(ent1.get())
    ent1.delete(0, END)
    a=int(ent2.get())
    ent2.delete(0, END)
    c=int(ent3.get())
    ent3.delete(0, END)
    d=(b**2)-4*a*c
    lbl1["text"] = d
    if d>0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        lblx1["text"] = f"X1: {x1}"
        lblx2["text"] = f"X2: {x2}"
    elif d==0:
        x= (-b / 2*a)
        lblx["text"] = f"x: {x}"
    else:
        dd="Корень вычеслить невозможно!"
        lbl1["text"] = dd
root= Tk()
root.title("Решение дискременанта")
root.geometry("500x700")
lbl_formula=Label(root,text="D=b**2-4*a*c",font="Arial 30")
lbl1=Label(root,text="", font="Arial 15")
lbl2=Label(root, text="Дискременант равен: ",font="Arial 15")
ent1=Entry(root) #b
ent2=Entry(root) #a
ent3=Entry(root) #c
btn1=Button(root, text="Показать решение", font="Arial 15", width=15)
lbl_formula.pack()
lblx=Label(root,text="", font="Arial 15")
lblx1=Label(root,text="", font="Arial 15")
lblx2=Label(root,text="", font="Arial 15")
ent1.pack()
ent2.pack()
ent3.pack()
btn1.pack()
lbl2.pack(side=LEFT)
lbl1.pack(side=LEFT)
lblx.pack(side=BOTTOM)
lblx1.pack(side=BOTTOM)
lblx2.pack(side=BOTTOM)
btn1.bind("<Button-1>", text_to_lbl)
root.mainloop()