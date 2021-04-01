from tkinter import *
from PIL import Image, ImageTk
soham_root=Tk()

#GUI logic
soham_root.geometry("434x345")#widthxheigth
# soham_root.minsize(200,100)#width,height
# soham_root.maxsize(500,900)
# rik=Label(text="Rik is a good GUI")
# rik.pack()
photo=PhotoImage(file="download.png")
rik_label=Label(image=photo)
rik_label.pack()
soham_root.title("Rik AI")
# for jpg or any other extensions images
# image=Image.open("download.png")
# photo=ImageTk.PhotoImage(image)
# rik_label=Label(image=photo)
# rik_label.pack()

soham_root.mainloop()