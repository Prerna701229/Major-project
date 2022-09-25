from tkinter import *

class lbs:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800")

        lbltitle=Label(self.root,text="Library Management System",
                       bg="powder blue" , fg="green",bd=20,padx=2,pady=6,
                       relief=RIDGE,font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root , bd=12 , relief=RIDGE , bg="powder blue")
        frame.place(x=0 , y=130 , width=1530 , height=400)

        #Left Frame
        dataframeleft=LabelFrame(frame , text="Library Management Information" ,
                                 bg="powder blue" , fg="green" , bd=20 , relief=RIDGE ,
                                 font=("times new roman",12,"bold"))
        dataframeleft.place(x=0 , y=5 , width=900 , height=350)

        lblmember=Label(dataframeleft , text="Member Type" , bg="powder blue" ,
                        fg="green" , bd=15 , relief=RIDGE ,
                                 font=("times new roman",12,"bold") , padx=2 , pady=6)
        #lblmember.grid(row=0 , column=0 , sticky=W)

        #prn no
        labelprn_no=Label(dataframeleft , text="prn no" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        labelprn_no.grid(row=1 , column=0)

        txtprn_no=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtprn_no.grid(row=1 , column=1)

        #title
        lbltitle=Label(dataframeleft , text="Title" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lbltitle.grid(row=2 , column=0)

        txttitle=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txttitle.grid(row=2 , column=1)

        #First Name
        lblfirstname=Label(dataframeleft , text="First Name" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lblfirstname.grid(row=3 , column=0)

        txtfirstname=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtfirstname.grid(row=3 , column=1)

        #Last Name
        lbllastname=Label(dataframeleft , text="Last Name" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lbllastname.grid(row=4 , column=0)

        txtlastname=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtlastname.grid(row=4 , column=1)

        #Address 1
        lbladdress1=Label(dataframeleft , text="Address 1" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lbladdress1.grid(row=5 , column=0)

        txtaddress1=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtaddress1.grid(row=5 , column=1)

        #Address 2
        lbladdress2=Label(dataframeleft , text="Address 2" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lbladdress2.grid(row=6 , column=0)

        txtaddress2=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtaddress2.grid(row=6 , column=1)

        #Postal Code
        lblpostcode=Label(dataframeleft , text="Post Code" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lblpostcode.grid(row=7 , column=0)

        txtpostcode=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtpostcode.grid(row=7 , column=1)

        #Mobile number
        lblmobile=Label(dataframeleft , text="Mobile No" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lblmobile.grid(row=8 , column=0)

        txtmobile=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtmobile.grid(row=8 , column=1)

        #Book Id
        lblbookid=Label(dataframeleft , text="Book ID" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lblbookid.grid(row=1 , column=2)

        txtbookid=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtbookid.grid(row=1 , column=3)

        #Book Title
        lblbooktitle=Label(dataframeleft , text="Book Title" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lblbooktitle.grid(row=2 , column=2)

        txtbooktitle=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtbooktitle.grid(row=2 , column=3)

        #Author
        lblauthor=Label(dataframeleft , text="Author" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lblauthor.grid(row=3 , column=2)

        txtauthor=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtauthor.grid(row=3 , column=3)

        #Data Borrowed
        lbldateborrow=Label(dataframeleft , text="Date Borrowed" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lbldateborrow.grid(row=4 , column=2)

        txtdateborrow=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtdateborrow.grid(row=4 , column=3)

        #Date Due
        lbldatedue=Label(dataframeleft , text="Date Due" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lbldatedue.grid(row=5 , column=2)

        txtdatedue=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtdatedue.grid(row=5 , column=3)

        #Days on Book
        lbldayonbook=Label(dataframeleft , text="Day on Book" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lbldayonbook.grid(row=6 , column=2)

        txtdayonbook=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtdayonbook.grid(row=6 , column=3)

        #Late Return Fine
        lblfine=Label(dataframeleft , text="Late Return Fine" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lblfine.grid(row=7 , column=2)

        txtfine=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtfine.grid(row=7 , column=3)

        #Date over Date
        lbldateover=Label(dataframeleft , text="Date over" , bg="powder blue" ,
                          padx=2 , pady=6 , font=("times new roman",12,"bold"))
        lbldateover.grid(row=8 , column=2)

        txtdateover=Entry(dataframeleft , font=("times new roman" , 15 , "bold") ,
                        width=29)
        txtdateover.grid(row=8 , column=3)
        
        #Right Frame
        dataframeright=LabelFrame(frame , text="Books Details" ,
                                 bg="powder blue" , fg="green" , bd=12 , relief=RIDGE ,
                                 font=("times new roman",12,"bold"))
        dataframeright.place(x=910 , y=5 , width=540 , height=350)

        #self.textbook=Text(dataframeright , font=("arial",12,"bold") ,
         #                  width=32 , height=16 , padx=2 , pady=6)
        #self.textbox.grid(row=0 , column=2)

        #Scroll bar
        listscrollbar=Scrollbar(dataframeright)
        listscrollbar.grid(row=0 , column=1 , sticky="ns")

        booklist=["Python","Java","C++","DSA",
                  "DBMS","MicroProcessor","C Language","JavaScript",
                  "HTML","Web Development","Machine Learning",
                  "Data Science","Artificial Intelligence","Flutter","Linux",
                  "Operating System","Computer Organization","Java","C++","DSA"]
        booklistbox=Listbox(dataframeright , font=("arial",12,"bold") ,
                            width=20 , height=16)
        booklistbox.grid(row=0 , column=0 , padx=4)
        listscrollbar.config(command=booklistbox.yview)

        for item in booklist:
            booklistbox.insert(END , item)

        #Buttons
        framebutton=Frame(self.root , bd=12 , relief=RIDGE , padx=20 ,
                          bg="powder blue")
        framebutton.place(x=0 , y=530 , height=70 , width=1530)

        btnadddata=Button(framebutton , text="Add Data" , font=("arial",12,"bold"),
                          width=23 , bg="blue")
        btnadddata.grid(row=0 , column=0)

        btnshowdata=Button(framebutton , text="Show Data" , font=("arial",12,"bold"),
                          width=23 , bg="blue")
        btnshowdata.grid(row=0 , column=1)

        btndeletedata=Button(framebutton , text="Delete Data" , font=("arial",12,"bold"),
                          width=23 , bg="blue")
        btndeletedata.grid(row=0 , column=2)

        btnupdatedata=Button(framebutton , text="Update Data" , font=("arial",12,"bold"),
                          width=23 , bg="blue")
        btnupdatedata.grid(row=0 , column=3)

        btnresetdata=Button(framebutton , text="Reset Data" , font=("arial",12,"bold"),
                          width=23 , bg="blue")
        btnresetdata.grid(row=0 , column=4)

        btnexit=Button(framebutton , text="Exit" , font=("arial",12,"bold"),
                          width=23 , bg="blue")
        btnexit.grid(row=0 , column=5)

        #Information
        framedetails=Frame(self.root , bd=12 , relief=RIDGE , padx=20 ,
                           bg="powder blue")
        framedetails.place(x=0 , y=600 , height=195 , width=1530)

        Table_frame=Frame(framedetails , bd=6 , relief=RIDGE ,
                          bg="powder blue")
        Table_frame.place(x=0 , y=2 , width=1460 , height=190)

        self.library_table=ttk.Treeview(Table_frame ,
                                        column={"membertypr","prnno","title","firstname",
                                                "lastname","address1"})
        xscroll.pack(side=BOTTOM , fill=x)
        yscroll.pack(side=RIGHT , fill=y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype" , text="member type")
        self.library_table.heading("prnno" , text="reference no.")
        self.library_table.heading("title" , text="title")
        self.library_table.heading("firstname" , text="first name")
        self.library_table.heading("last name" , text="last name")
        self.library_table.heading("address1" , text="address1")
        self.library_table.heading("address2" , text="address2")
        self.library_table.heading("postid" , text="post id")
        self.library_table.heading("mobile" , text="mobile number")
        self.library_table.heading("bookid" , text="book id")
        self.library_table.heading("booktitle" , text="book title")
        self.library_table.heading("author" , text="author")
        self.library_table.heading("dateborrowed" , text="date of borrow")
        self.library_table.heading("datedue" , text="date of due")
        self.library_table.heading("days" , text="daysonbook")
        self.library_table.heading("latereturnfine" , text="latereturnfine")
        self.library_table.heading("dateoverdue" , text="dateoverdue")
        self.library_table.heading("finalprice" , text="final price")

        xscroll=ttk.Scrollbar(Table_frame , orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame , orient=VERTICAL)

        self.library_table["show"]="heading"
        self.library_table.pack(fill=BOTH , expand=1)

        self.library_table.column("membertype" , width=100)
        self.library_table.column("prnno" , width=100)
        self.library_table.column("title" , width=100)
        self.library_table.column("firstname" , width=100)
        self.library_table.column("lastname" , width=100)
        self.library_table.column("address1" , width=100)
        self.library_table.column("address2" , width=100)
        self.library_table.column("postid" , width=100)
        self.library_table.column("mobile" , width=100)
        self.library_table.column("bookid" , width=100)
        self.library_table.column("booktitle" , width=100)
        self.library_table.column("author" , width=100)
        self.library_table.column("dateborrowed" , width=100)
        self.library_table.column("datedue" , width=100)
        self.library_table.column("days" , width=100)
        self.library_table.column("latereturnfine" , width=100)
        self.library_table.column("dateoverdue" , width=100)
        self.library_table.column("finalprice" , width=100)
        
                
if __name__=="__main__":
    root=Tk()          # Tk() :- Method of Tkinter module which creates widget
    obj=lbs(root)
    root.mainloop()
