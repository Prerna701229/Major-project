from tkinter import*
root = Tk()
def getvals():
    print("Accepected")
root.geometry("500x500")
root.title("Pakistani College Form")
Label(root,text="Pakstani College From",font="arial 15 bold").grid(row=0,column=3)
name=Label(root,text="Name")
Phone=Label(root,text="Phone no.")
Gender=Label(root,text="gender")
name.grid(row=1,column=2)
Phone.grid(row=2,column=2)
Gender.grid(row=3,column=2)
namevalue=StringVar
Phonevalue=StringVar
Gendervalue=StringVar
checkvalue=IntVar
nameentry=Entry(root,textvariable=namevalue ,bg="blue")
Phoneentry=Entry(root,textvariable=Phonevalue ,bg="green")
Genderentry=Entry(root,textvariable=Gendervalue ,bg="red")
nameentry.grid(row=1,column=4)
Phoneentry.grid(row=2,column=4)
Genderentry.grid(row=3,column=4)
checkbtn= Checkbutton(text="Remember Me?", variable= checkvalue).grid(row=5,column=3)
button=Button(root,text="submit now").grid(row=6,column=4)
Button(text="submit",command=getvals).grid(row=8,column=4)




root.mainloop()
