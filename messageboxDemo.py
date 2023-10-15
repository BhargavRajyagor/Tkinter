from tkinter import *  
from tkinter import messagebox  
top = Tk()  
top.geometry("400x400")

def info():
   messagebox.showinfo("Information Message", "Hello World")
B1 = Button(top, text = "Information Message", command = info)
B1.pack()

def warn():
   messagebox.showwarning("Warning Message", "Hello World")
B2 = Button(top, text = "Warning Message", command = warn)
B2.pack()

def error():
   messagebox.showerror("Error Message", "Hello World")
B3 = Button(top, text = "Error Message", command = error)
B3.pack()

def ask():
   messagebox.askquestion("Ask question Message", "Hello World")
B4 = Button(top, text = "Ask question", command = ask)
B4.pack()

def askOkCancel():
   answer = messagebox.askokcancel("Ask OK Cancle Message", "Hello World")
   if(answer == 1):
      messagebox.showinfo("Your Selection is.","Ok selected..!!")
   else:
      messagebox.showinfo("Your Selection is.","Cancel Selected..!!")
   

B5 = Button(top, text = "Ask OK Cancle", command = askOkCancel)
B5.pack()

def askRC():
   answer = messagebox.askretrycancel("Ask Retry Cancle Message", "Hello World")
   messagebox.showinfo("Information Message", answer)
   

B6 = Button(top, text = "Ask Retry Cancle", command = askRC)
B6.pack()

def askYN():
   answer = messagebox.askyesno("Ask Yes No Message", "Hello World")
   messagebox.showinfo("Information Message", answer)
   

B5 = Button(top, text = "Ask Yes No", command = askYN)
B5.pack()

top.mainloop()  
