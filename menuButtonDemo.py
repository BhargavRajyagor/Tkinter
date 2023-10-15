from tkinter import *
from tkinter import messagebox 
  
top = Tk()  
  
top.geometry("200x250")  


def hindi():  
    messagebox.showinfo("Hi..!!", "Hello I AM Hindi Language....!!")  
    
menubutton = Menubutton(top, text = "Language", relief = FLAT)  
  
menubutton.grid()  
  
menubutton.menu = Menu(menubutton)  
  
menubutton["menu"]=menubutton.menu  
  
menubutton.menu.add_checkbutton(label = "Hindi",command=hindi, variable=IntVar())  
  
menubutton.menu.add_checkbutton(label = "English", variable = IntVar())  
  
menubutton.pack()  
  
top.mainloop() 
