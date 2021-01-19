from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import webbrowser as webb
from tkinter.filedialog import *
def web(event):
    url=webb.get().webb.open_new_tab(ent.get())
def open_file():
    o_file=askopenfilename()
def save_as():
    as_file=asksaveasfile(mode='w',defaultextension=(".txt"))
    text=txt.get(0.0,END)
    as_file.write(text)
    as_file.close()
root = Tk()
root.title("Название окна")
root.geometry("700x800")
tab_control=ttk.Notebook(root)
tab1=Frame(tab_control)
tab2=Frame(tab_control)
tab3=Frame(tab_control)
tab_control.add(tab1, text="First")
tab_control.add(tab2, text="Second")
tab_control.add(tab3, text="Trird")
var=IntVar()
var.set(25)
spin=Spinbox(tab1,from_=0, to=100,textvariable=var)
ent=Entry(tab1,width=40)
ent.bind("<Return>", web)
txt=scrolledtext.ScrolledText(tab1, width=50, height=9)
menu=Menu(root)
root.config(menu=menu)
color_menu=Menu(menu,tearoff=0)
menu.add_cascade(label="Colors",menu=color_menu)
color_menu.add_command(label="Red",command=lambda:tab2.configure(bg='Red'))
color_menu.add_command(label="Blue",command=lambda:tab2.configure(bg='Blue'))
color_menu.add_command(label="Green",command=lambda:tab2.configure(bg='Green'))
dialog_m=Menu(menu,tearoff=0)
menu.add_cascade(label="File", menu=dialog_m)
dialog_m.add_command(label="Open...", command=open_file)
dialog_m.add_command(label="Save As",command=save_as)
spin.grid(row=0, column=0)
ent.grid(row=0, column=1)
txt.grid(row=1,column=0, columnspan=2)




tab_control.pack(expand=1,fill="both")

root.mainloop()