from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")

def order():

    tmsg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")

# var = IntVar()
var = StringVar()
var.set("Radio")
# var.set(1)
Label(root, text = "What would you like to have sir?",font="lucida 19 bold",
      justify=LEFT, padx=14).pack()
radio = Radiobutton(root,text="Chicken Biriyani",padx=14,variable=var, value="Chicken Biriyani").pack()
radio = Radiobutton(root, text="Mixed Chowmin", padx=14, variable=var, value="Mixed Chowmin").pack()
radio = Radiobutton(root, text="Veg Chowmin", padx=14, variable=var, value="Veg Chowmin").pack()
radio = Radiobutton(root, text="Mutton Chowmin", padx=14, variable=var, value="Mutton Chowmin").pack()

Button(text="Order Now", command=order).pack()
root.mainloop()
