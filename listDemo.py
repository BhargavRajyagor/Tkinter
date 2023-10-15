# !/usr/bin/python3  
from tkinter import *  
top = Tk()  
top.geometry("200x250")  
lbl = Label(top,text = "A list of favourite countries...")  
listbox = Listbox(top)  
listbox.insert(1,"India")  
listbox.insert(2, "USA")  
listbox.insert(3, "Japan")  
listbox.insert(4, "Austrelia")  
#this button will delete the selected item from the list   
#You need to create a function without parameters that you can use as the command.
# A lambda can refer to variables outside it; this is called a closure. 
btn = Button(top,
             text = "delete",
             command = lambda listbox=listbox: listbox.delete(ANCHOR))  
lbl.pack()  
listbox.pack()  
btn.pack()  
top.mainloop()  
