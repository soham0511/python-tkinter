from tkinter import *
def soham(event):
    print(f"You clicked on the button at {event.x} and {event.y}")
    print("Hello ji")
root=Tk()

root.geometry("644x334")
widget=Button(root,text="Click me")
widget.pack()
widget.bind('<Button-1>',soham)
widget.bind("<Double-1>",quit)
root.mainloop()