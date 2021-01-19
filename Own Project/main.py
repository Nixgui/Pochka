import functions
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
root=Tk()
root.wm_state('zoomed')
root.title("Запись")
def Login(event):
    fail = open("users.txt", "r")
    mas1 = []
    mas2 = []
    for line in fail:
        n = line.find(":")
        mas1.append(line[0:n].strip())
        mas2.append(line[n + 1:len(line)].strip())
    for l in mas1:
        if l == login.get():
            for p in mas2:
                if p == password.get():
                    login.grid_remove()
                    password.grid_remove()
                    login1.grid_remove()
                    password1.grid_remove()
                    messagebox.showinfo("Вход","Добро пожаловать")
                else:
                    messagebox.showerror("Вход", "Логин или пароль введены неверно")
        else:
            messagebox.showerror("Вход", "Логин или пароль введены неверно")
################################################
login=Entry(root,text="")
password=Entry(root,text="")
login1=Label(root,text="Login: ")
password1=Label(root,text="Password: ")

################################################
password1.grid(row=1, column=0)
login1.grid(row=0,column=0)
login.grid(row=0,column=1)
password.bind("<Return>", Login)
password.grid(row=1, column=1)
root.mainloop()