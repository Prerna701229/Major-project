from tkinter import *
root=Tk()

def getvals():
    print("Accepted")

root.geometry("500x500")
root.title("Pakistani College Form")
Label(root, text="Pakistani College Form" , font="arial 15 bold").grid(row=0,column=3)

name=Label(root,text="Name")
phone=Label(root,text="phone")
gender=Label(root,text="gender")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)

namevalue=Stringvar
phonevalue=Stringvar
gendervalue=Stringvar

checkvalue=Intvar

entry=Entry(root,textvariable=namevalue)
entry=Entry(root,textvariable=phonevalue)
entry=Entry(root,textvariable=gendervalue)

nameentry.grid(row=1,column=4)
phoneentry.grid(row=2,column=4)
genderentry.grid(row=3,column=4)

checkbtn=Checkbutton(text="Remember me ?",variable=checkvalue).grid(row-5,column=3)

button=Button(root,text="Submit Now").grid(row=6,column=4)
Button(text="Submit",command=getvals).grid(row=8,column=4)

root.mainloop()
