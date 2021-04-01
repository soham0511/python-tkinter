from tkinter import *
root=Tk()

def hello():
    Label(root,text="Submitted Successfully !",font="comicsnsms 13 bold").grid(row=10,column=3)

    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), emailvalue.get(), aadharvalue.get(), addressvalue.get(), foodservices.get()}\n ")
root.geometry("644x344")
Label(root,text="Welcome to Srimany Inc.",font="comicsnsms 13 bold").grid(row=0,column=3)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
email=Label(root,text="Email Id")
aadhar=Label(root,text="Aadhar No.")
address=Label(root,text="Address")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
email.grid(row=3,column=2)
aadhar.grid(row=4,column=2)
address.grid(row=5,column=2)

namevalue=StringVar()
phonevalue=StringVar()
emailvalue=StringVar()
aadharvalue=StringVar()
addressvalue=StringVar()
foodservicesvalue=IntVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
emailentry=Entry(root,textvariable=emailvalue)
aadharentry=Entry(root,textvariable=aadharvalue)
addressentry=Entry(root,textvariable=addressvalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
emailentry.grid(row=3,column=3)
aadharentry.grid(row=4,column=3)
addressentry.grid(row=5,column=3)
foodservices=Checkbutton(text="Download seat confirmation letter",variable=foodservicesvalue)
foodservices.grid(row=6,column=3)
Button(text="Submit",command=hello).grid(row=7, column=3)
root.mainloop()