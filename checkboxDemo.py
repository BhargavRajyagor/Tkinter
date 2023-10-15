from tkinter import *
from tkinter import messagebox  
top = Tk()  
top.geometry("200x200") 

checkvar1 = IntVar()  
checkvar2 = IntVar()  
checkvar3 = IntVar()  

def subject():  
    if(checkvar1.get() == 1):
        messagebox.showinfo("Hello I PYTHON..!!", "I am checked..!!")  
    else:
        messagebox.showinfo("Hello I PYTHON..!!", "I am not checked..!!")  
 
chkbtn1 = Checkbutton(top,
                      text = "PYTHON",
                      variable = checkvar1,
                      command = subject,
                      onvalue = 1,
                      offvalue = 0, height = 2, width = 10)  
chkbtn2 = Checkbutton(top, text = "ASP.NET", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10)  
chkbtn3 = Checkbutton(top, text = "ANDROID", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10)
chkbtn1.pack()  
chkbtn2.pack()  
chkbtn3.pack()  
top.mainloop()
