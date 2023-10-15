from tkinter import *  
from tkinter import messagebox
  
root = Tk()  
  
root.geometry("200x200")  
def callMe():  
    messagebox.showinfo("Hello I Am Button..!!", "CALLED FROM PARENT") 
    

def open():  
    top = Toplevel(root)  
    b1 = Button(top,text = "CHILD",command = callMe,activeforeground = "red",activebackground = "pink",pady=10)
    b1.pack(side = TOP)
    top.mainloop()  
  
btn = Button(root, text = "open", command = open)  
  
btn.place(x=75,y=50)  
  
root.mainloop() 