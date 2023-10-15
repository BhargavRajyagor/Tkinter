from tkinter import *  
top = Tk()  
top.geometry("400x400")
def getSpinCount():
    cnt = spin1.get()
    print("Current Spin Conut is :: " + str(cnt))  
spin1 = IntVar()
b1 = Button(top,
            text = "Get Spin Value..!!",
            command = getSpinCount,
            activeforeground = "red",
            activebackground = "pink",
            pady=10)

b1.pack()
spin1 = Spinbox(top, from_= 0, to = 25)  
spin1.pack()  
top.mainloop()  
