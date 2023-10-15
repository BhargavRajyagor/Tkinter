from tkinter import *   
  
top = Tk()  
  
top.geometry("200x200")  
  
#creating a simple canvas  
c = Canvas(top,bg = "pink",height = "200",width = 200)  
canvas_height = 20
canvas_width = 200

x = int(canvas_width / 2)
y = int(canvas_height / 2) 

arc = c.create_arc((5,10,150,200),start = 0,extent = 150, fill= "white")  
line = c.create_line(0, y, canvas_width, y ) 
oval = c.create_oval(50, 50, x+20, y+20,fill="yellow")

c.pack()  
  
top.mainloop() 
