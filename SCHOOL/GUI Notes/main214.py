import tkinter as tk
#global variable section
masterUsername = "ElRickyBobby"
materPassword = "-123456"

#function section
def testMyButton():
     #print("Test My Button")

     #get the information from the text box
     username = entUsername.get()  #accessor
     password = entPassword.get()
     print(username,password)

     #check the entry to the master password

     #tkraise() puts this frame at the very top
     frameAuth.tkraise()

#VIEW section
#main window
root = tk.Tk()      #root is the window   
root.wm_geometry("200x100")
root.title("Authorization")

#Frame for successful log in
frameAuth = tk.Frame(root)
frameAuth.grid(row=0,column=0, sticky='news')

#create an empty Frame
frameLogin = tk.Frame(root)
frameLogin.grid(row=0,column=0, sticky='news') #constraint layout

#                     (positionalArgument, keyWord Argument)
lblUsername = tk.Label(frameLogin,         text="Username:")
lblUsername.pack(pady=5)
#hungarian naming syntax that shows what the variable is a type of entPassword
entUsername = tk.Entry(frameLogin,bd=3)
entUsername.pack(pady=5)
#hungarian naming syntax that shows what the variable is a type of entPassword
lblPassword = tk.Label(frameLogin,         text="Password:", font="Courier")
lblPassword.pack(pady=5)
#hungarian naming syntax that shows what the variable is a type of entPassword
entPassword = tk.Entry(frameLogin,bd=3)
entPassword.pack(pady=5)

#                   (frame     ,text for button, command or method to run)
btnLogin = tk.Button(frameLogin,text="Log In", command=testMyButton)
btnLogin.pack(pady=20,padx=175)

lblDisplay=tk.Label(frameAuth,text="Hello there")
lblDisplay.pack(padx=5)

root.mainloop()     #you need this at the bottom of your file to run everything