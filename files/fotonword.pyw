from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import Menu
from sys import exit
import requests
import webbrowser 
import re
from tkinter.ttk import Combobox
##########
sbg="grey"
main_window = Tk()
main_window.title("Foton Word")
main_window.geometry("1920x1080")
main_window.config(bg=sbg)
tab_control = ttk.Notebook(main_window)
def quitq():
    global main_window
    main_window.destroy()
def openf():
    txt.delete(1.0, END)
    i=filedialog.askopenfilename(filetypes=(("Python files","*.py"),("Spec files","*.spec"),("Text files","*.txt"),("PyCompile files","*.pyc"),("C++ files","*.cxx")))
    try:
        txt.insert(INSERT, open(i).read())
        main_window.title(f"Ford - {i}")
    except:
        ans=messagebox.showerror("Ford", "Not open file!")
        main_window.title("Ford - <untitled>")
def new_file():
    main_window.title("Ford - <untitled>")
    txt.delete(1.0, END)
def save():
    savefn=filedialog.asksaveasfilename()
    f=open(savefn,"w+")
    try:
        f.write(txt.get(1.0, END))
    except:
        f.write("")
    f.close()
    main_window.title("Ford - "+savefn)
def about():
    a=Toplevel()
    a.config(bg=sbg)
    Label(a,text="""




               Ford or Foton Word                    
               Text Editor by Foton Corporation (C)                        



""").pack()
    a.title("Ford")
    a.mainloop()
def sett():
    global sbg
    s=Toplevel()
    s.title("Setting Ford")
    s.geometry("800x600")
    s.config(bg=sbg)
    combo = Combobox(s)  
    combo['values'] = ("red", "black", "green", "blue", "orange", "grey","white","purple","pink","brown","gold","silver","violet")  
    combo.current(0)  # установите вариант по умолчанию  
    combo.pack()
    def tool():
        global sbg
        main_window.config(bg=combo.get())
        s.config(bg=combo.get())
        sbg=combo.get()
    Button(s,text="                      Ok                        ",command=tool,bg=sbg).pack()
    s.mainloop()
menu = Menu(main_window)  
new_item_m = Menu(menu)  
new_item_m.add_command(label='Exit' , command=quitq)
new_item_m.add_command(label='Open' , command=openf)
new_item_m.add_command(label='Save' , command=save)
new_item_m.add_command(label='New file' , command=new_file)
menu.add_cascade(label='File', menu=new_item_m)
tools_m = Menu(menu)
tools_m.add_command(label='About Ford' , command=about)
tools_m.add_command(label='Setting' , command=sett)
menu.add_cascade(label='Tools', menu=tools_m)
txt = scrolledtext.ScrolledText(main_window, width=160, height=40)
txt.pack()
main_window.config(menu=menu)
tab_control.pack(expand=1, fill='both') 
main_window.mainloop()


