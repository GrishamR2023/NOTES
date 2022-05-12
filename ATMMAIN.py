#import
from tkinter import *

#create root
root = Tk()
root.geometry("900x810")
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
mainFrame = Frame(root,width=900,height = 810,bg = 'grey')
mainFrame.pack()

inputFrame = Frame(mainFrame,width=900,height=525,bg ="grey")
inputFrame.place(x=0,y=0)

leftButtonFrame = Frame(mainFrame,width = 100, height = 800,bg = "grey")
leftButtonFrame.place(x=0,y=0)

firstBTN = Button(leftButtonFrame,text = "1",width = 10,height = 5,bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1.5)
firstBTN.grid(row = 0,padx = 7, pady=25)

secondBTN = Button(leftButtonFrame,text = "2",width = 10,height = 5,bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1.5)
secondBTN.grid(row = 1,padx = 7, pady=25)

thirdBTN = Button(leftButtonFrame,text = "3",width = 10,height = 5,bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1.5)
thirdBTN.grid(row = 2,padx = 7, pady=25)

fourthBTN = Button(leftButtonFrame,text = "4",width = 10,height = 5,bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1.5)
fourthBTN.grid(row = 3,padx = 7, pady=25)



rightButtonFrame = Frame(mainFrame,width = 100, height = 800,bg = "grey")
rightButtonFrame.place(x=800,y=0)

fifthBTN = Button(rightButtonFrame,text = "5",width = 10,height = 5,bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1.5)
fifthBTN.grid(row = 0,padx = 7, pady=25)

sixthBTN = Button(rightButtonFrame,text = "6",width = 10,height = 5,bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1.5)
sixthBTN.grid(row = 1,padx = 7, pady=25)

seventhBTN = Button(rightButtonFrame,text = "7",width = 10,height = 5,bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1.5)
seventhBTN.grid(row = 2,padx = 7, pady=25)

eigthBTN = Button(rightButtonFrame,text = "8",width = 10,height = 5,bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1.5)
eigthBTN.grid(row = 3,padx = 7, pady=25)





middleScreen = Frame(mainFrame,width = 700, height = 525,bg = "teal",highlightbackground="black",highlightcolor="black",highlightthickness=1.5)
middleScreen.place(x=100,y=0)

inputLabel = Label(root,width = 30,bd = 0)
inputLabel.pack()

buttonFrame = Frame(mainFrame,width=312,height=272.5,bg="grey")
buttonFrame.place(x=275,y=525)



seven = Button(buttonFrame,text="7",fg="black",width=10,height=4,bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1,bg="#fff",command=lambda:buttonClick(7),cursor="heart").grid(row=1,column=0,padx=1,pady=1)
eight = Button(buttonFrame,text="8",fg="black",width=10,height=4,bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1,bg="#fff",command=lambda:buttonClick(8),cursor="trek").grid(row=1,column=1,padx=1,pady=1)
nine = Button(buttonFrame,text="9",fg="black",width=10,height=4,bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1,bg="#fff",command=lambda:buttonClick(9),cursor="mouse").grid(row=1,column=2,padx=1,pady=1)
multiply = Button(buttonFrame,text="*",fg="black",width=10,height=4,bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1,bg="#eee",command=lambda:buttonClick("*"),cursor="spraycan").grid(row=1,column=3,padx=1,pady=1)

# third row
four = Button(buttonFrame, text = "4", fg = "black", width = 10, height = 4, bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1, bg = "#fff",command=lambda:buttonClick(4),cursor="fleur").grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(buttonFrame, text = "5", fg = "black", width = 10, height = 4, bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1, bg = "#fff",command=lambda:buttonClick(5),cursor="watch").grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(buttonFrame, text = "6", fg = "black", width = 10, height = 4, bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1, bg = "#fff",command=lambda:buttonClick(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(buttonFrame, text = "-", fg = "black", width = 10, height = 4, bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1, bg = "#eee",command=lambda:buttonClick("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

# fourth row
one = Button(buttonFrame, text = "1", fg = "black", width = 10, height = 4, bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1, bg = "#fff",command=lambda:buttonClick(1),cursor="shuttle").grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(buttonFrame, text = "2", fg = "black", width = 10, height = 4, bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1, bg = "#fff",command=lambda:buttonClick(2),cursor="spider").grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(buttonFrame, text = "3", fg = "black", width = 10, height = 4, bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1, bg = "#fff",command=lambda:buttonClick(3),cursor="exchange").grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(buttonFrame, text = "+", fg = "black", width = 10, height = 4, bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1, bg = "#eee",command=lambda:buttonClick("+"),cursor="plus").grid(row = 3, column = 3, padx = 1, pady = 1)

# fourth row
zero = Button(buttonFrame, text = "0", fg = "black", width = 22, height = 4, bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1, bg = "#fff",command=lambda:buttonClick(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(buttonFrame, width = 10, height = 4, bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1, bg = "#eee",command=lambda:buttonClick(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(buttonFrame, width = 10, height = 4, bd=2,highlightbackground="black",highlightcolor="black",highlightthickness=1, bg = "#eee",command=lambda:equalButton()).grid(row = 4, column = 3, padx = 1, pady = 1)

root.mainloop()