from tkinter import *

root=Tk()

canvas_width=800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()
#the line goes from the point x1,y1 to x2,y2
can_widget.create_line(0,0,800,400,fill="red")
#top-left coordinate and bottom right coordinate
can_widget.create_rectangle(3,5,700,300,fill="blue")
can_widget.create_text(200,200,text="Srimany")#coordinates of the center of the text
can_widget.create_oval(344,167,123,255)#coordinates of end point of major axis and minor axis
root.mainloop()