#import
from tkinter import *

#create root
root = Tk()
root.geometry("312x324")
root.title("Calculator")
root.resizable(0,0)  #prevents from resizing the root

#functions
def buttonClick(item):
     global expression
     expression += str(item)
     print(expression)
     outputText.set(expression)

def clearButton():
     global expression
     expression=""
     print(expression)
     outputText.set(expression)
     
def equalButton():
     global expression
     result=str(eval(expression))
     expression=""
     print(result)
     outputText.set(result)

#global variables
expression=""
outputText = StringVar() #StringVar() is a var that is used in widgets
                         #if you're wanting to pass values to a widget, you need a StringVar()


#add your widgets
inputFrame = Frame(root,width=312,height=50,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
inputFrame.pack(side=TOP)     #this will make sure it stays on the top

inputField = Entry(inputFrame, bd=0, justify=RIGHT, width=312, textvariable=outputText, font=('Times New Roman', 18, 'bold'))
inputField.grid(row=0,column=0)
inputField.pack(ipady = 10) #ipady is internal padding

buttonFrame = Frame(root,width=312,height=272.5,bg="grey")
buttonFrame.pack()

clear = Button(buttonFrame,text="C",fg="black",width=32,height=3,bd=0,bg="#eee",command=lambda:clearButton(),cursor="hand2")
clear.grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide = Button(buttonFrame,text="/",fg="black",width=10,height=3,bd=0,bg="#eee",command=lambda:buttonClick("/"),cursor="pirate")
divide.grid(row=0,column=3,padx=1,pady=1)

seven = Button(buttonFrame,text="7",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(7),cursor="heart").grid(row=1,column=0,padx=1,pady=1)
eight = Button(buttonFrame,text="8",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(8),cursor="trek").grid(row=1,column=1,padx=1,pady=1)
nine = Button(buttonFrame,text="9",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(9),cursor="mouse").grid(row=1,column=2,padx=1,pady=1)
multiply = Button(buttonFrame,text="*",fg="black",width=10,height=3,bd=0,bg="#eee",command=lambda:buttonClick("*"),cursor="spraycan").grid(row=1,column=3,padx=1,pady=1)

# third row
four = Button(buttonFrame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(4),cursor="fleur").grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(buttonFrame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(5),cursor="watch").grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(buttonFrame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(buttonFrame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",command=lambda:buttonClick("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

# fourth row
one = Button(buttonFrame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(1),cursor="shuttle").grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(buttonFrame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(2),cursor="spider").grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(buttonFrame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(3),cursor="exchange").grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(buttonFrame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",command=lambda:buttonClick("+"),cursor="plus").grid(row = 3, column = 3, padx = 1, pady = 1)

# fourth row
zero = Button(buttonFrame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(buttonFrame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",command=lambda:buttonClick(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(buttonFrame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",command=lambda:equalButton()).grid(row = 4, column = 3, padx = 1, pady = 1)

root.mainloop()