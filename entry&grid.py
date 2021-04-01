from tkinter import *
def getvals():
    print(f"The username of current user is {uservalue.get()}")
    print(f"The password of current user is {passvalue.get()}")
root=Tk()
root.geometry("455x333")
username=Label(root,text="Username")
password=Label(root,text="Password")
username.grid()
password.grid(row=1)


# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(text="Submit",command=getvals).grid()
root.mainloop()