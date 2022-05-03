import tkinter as tk

groot = tk.Tk()
groot.geometry("300x300")

frameBlue = tk.Frame(groot,width=200,height=150,background="Blue")
#grid(where do you want it in the grid)
frameBlue.grid(row=0,column=0)

frameRed = tk.Frame(groot,width=200,height=150,background="Red")
frameRed.grid(row=1,column=0)

frameGreen = tk.Frame(groot,width=100,height=150,background="#00FF00")
frameGreen.grid(row=0,column=1)

frameYellow= tk.Frame(groot,width=100,height=150,background="Yellow")
frameYellow.grid(row=1,column=1)

groot.mainloop()