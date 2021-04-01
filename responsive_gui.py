from tkinter import *

root = Tk()
root.geometry("250x200")

def update():
    width_value = width.get()
    height_value = height.get()
    root.geometry(f"{width_value}x{height_value}")

# root.title("Window Resizer")
Label(text="Window Resizer").grid(column=2)

Label(text="Width: ").grid(row=1, column=1)
Label(text="Height: ").grid(row=2, column=1)

width = StringVar()
height = StringVar()

width_entry = Entry(root, textvariable=width).grid(row=1, column=2)
height_entry = Entry(root, textvariable=height).grid(row=2, column=2)

Button(text="Apply", command=update).grid(column=2)

root.mainloop()