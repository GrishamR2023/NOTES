from tkinter import *
import time
from datetime import datetime
root=Tk()

def update():
     s=str(datetime.now().strftime("%H:%M:%S"))
     myLabel.config(text=s)
     myLabel.after(1000,update)

myLabel = Label(root,text="Old Text")
myLabel.pack(pady=20)


myLabel.after(1000,update)
root.mainloop()