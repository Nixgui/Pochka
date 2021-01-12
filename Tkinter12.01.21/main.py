from tkinter import *
from PIL import ImageTk, Image
c=0
cc=12
def lkm(event):
    global c, cc
    c+=1
    cc+=c
    lbl.configure(text=c, font=f"Arial {cc}")
def pkm(event):
    global c, cc
    if c>0:
        c-=1
        cc-=c
    else:
        cc=10
    lbl.configure(text=c, font=f"Arial {cc}")
def text_to_btn(event):
    btn["text"]=ent.get()
    ent.delete(0,END)
def text_to_lbl():

    lbl.configure(text=var.get()) #ent.insert(END,var.get())
root = Tk()
root.title("Название окна")
root.geometry("500x800")
btn=Button(root,
           text="Нажми \nна меня",
           fg="red",
           bg="lightblue",
           font="Arial 40",
           width=15)
lbl=Label(root,
          text="0",
          height=3)

image=Image.open("click.jpg")
photo=ImageTk.PhotoImage(image)
btn_image=Button(root,image=photo)
ent=Entry(root,
          fg="red",
          bg="lightblue",
          font="Arial 40",
          width=15)
var=IntVar()
var.set(2) #Заранее выбрана значение Value
rad1=Radiobutton(root,
                 text="Uks",
                 variable=var,
                 value=1,
                 command=text_to_lbl)
rad2=Radiobutton(root,
                 text="Kaks",
                 variable=var,
                 value=2,
                 command=text_to_lbl)
rad3=Radiobutton(root,
                 text="Kolm",
                 variable=var,
                 value=3,
                 command=text_to_lbl)
btn.pack()
lbl.pack()
btn_image.pack()
ent.pack(padx=20,pady=20)
rad1.pack(side=LEFT, padx=20)
rad2.pack(side=LEFT, padx=20)
rad3.pack(side=LEFT, padx=20)
btn.bind("<Button-1>", lkm)
btn.bind("<Button-3>", pkm)
ent.bind("<Return>", text_to_btn)
root.mainloop()