#https://www.youtube.com/watch?v=Z_0ISFfT_eM&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=100&ab_channel=Codemy.com
from tkinter import *
from tkinter import filedialog
import os

root=Tk()
root.geometry("500x450")

'''
    read only r
    read and write r+ (beginning of file)
    write only w (over-written)
    write and read w+ (over written)
    append only a (end of file)
    append and read a+ (end of file)
    create and write x (cannot already exist)
'''

def openText():
    textFile=filedialog.askopenfilename(initialdir=os.getcwd(),filetypes=(("Text Files","*.txt"),))
    textFile=open(textFile,'r')
    stuff = textFile.read()

    myText.insert(END, stuff)
    textFile.close()

def saveText():
    textFile = open('sample.txt','w')
    textFile.write(myText.get(1.0,END))


myText=Text(root,width=40,height=10,font=("hellvetica",16))
myText.pack(pady=10)

#pack() is okay on the buttons but not on the Text widgets.  It actually changes the type.
openButton=Button(root,text="Open text file",command=openText).pack(pady=20)
saveButton=Button(root,text="save file",command=saveText).pack(pady=20)

root.mainloop()