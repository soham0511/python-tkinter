from tkinter import *

def name():
    print("Printing")
def order():
    print("Order your favourite meal")
def hire():
    print("You will be notified when we get some talent")
def contact():
    print("Our contact Number is 43222151")
root=Tk()
root.geometry("655x333")

frame=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")
b1=Button(frame,fg="red",text="Print Now",command=name)
b1.pack(side=LEFT)
b2=Button(frame,fg="red",text="Order Now",command=order)
b2.pack(side=LEFT)
b3=Button(frame,fg="red",text="Hire With Us",command=hire)
b3.pack(side=LEFT)
b4=Button(frame,fg="red",text="Contact Now",command=contact)
b4.pack(side=LEFT)
root.mainloop()