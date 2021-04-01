from tkinter import *
root=Tk()
root.geometry("344x455")

f1=Frame(root,bg="grey",relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

f2=Frame(root,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill="")

l=Label(f1,text="Srimany Group")
l.pack(padx=12)

l=Label(f2,text="Welcome to Code Base of Rik AI")
l.pack(pady=13)
root.mainloop()