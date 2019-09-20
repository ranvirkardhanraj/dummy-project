from tkinter import*
from tkinter import ttk
class Student:
    def __init__ (self,root):
        self.root=root
        self.root.title("Student ManagementSystem")
        self.root.geometry("1350x700+0+0")
        
        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="white",fg="blue")
        title.pack(side=TOP,fill=X)
        #-----------ManageFrame----------------------------------
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="green")
        Manage_Frame.place(x=20,y=100,width=450,height=600)

        m_title=Label(Manage_Frame,text="Manage Student",bg="green",fg="white",font=("times new roman",40,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        
        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="green",fg="white",font=("times new roman",15,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bg="green",fg="white",font=("times new roman",15,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_Name=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_Email=Label(Manage_Frame,text="Email",bg="green",fg="white",font=("times new roman",15,"bold"))
        lbl_Email.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_Email=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_gender=Label(Manage_Frame,text="Gender",bg="green",fg="white",font=("times new roman",15,"bold"))
        lbl_gender.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,font=("times new roman",13,"bold"),state="readonly")
        combo_gender["values"]=("Male","Female","Other")
        combo_gender.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_Contact=Label(Manage_Frame,text="Contact",bg="green",fg="white",font=("times new roman",15,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_Contact=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="D.O.B",bg="green",fg="white",font=("times new roman",15,"bold"))
        lbl_name.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_Name=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        

        lbl_gender=Label(Manage_Frame,text="Address",bg="green",fg="white",font=("times new roman",15,"bold"))
        lbl_gender.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        a=Text(Manage_Frame,width=26,height=6)
        a.grid(row=7,column=1,pady=10,padx=20,sticky="w")
     #-----------Button---------------------------------------------   

        but_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="green")
        but_Frame.place(x=15,y=550,width=420)

        add=Button(but_Frame,text="Add",width=10).grid(row=0,column=1,padx=10,pady=8)
        add=Button(but_Frame,text="Update",width=10).grid(row=0,column=2,padx=10,pady=8)
        add=Button(but_Frame,text="Delete",width=10).grid(row=0,column=3,padx=10,pady=8)
        add=Button(but_Frame,text="Clear",width=10).grid(row=0,column=4,padx=10,pady=8)


        

        

        

        

        








        
        #-----------DetailFrame----------------------------------
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="green")
        Detail_Frame.place(x=500,y=100,width=800,height=600)

        lbl_roll=Label(Detail_Frame,text="Search By",bg="green",fg="white",font=("times new roman",15,"bold"))
        lbl_roll.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Detail_Frame,font=("times new roman",13,"bold"),state="readonly")
        combo_gender["values"]=("Roll No.","Name","Contact")
        combo_gender.grid(row=0,column=1,pady=10,padx=20,sticky="w")

        txt_Email=Entry(Detail_Frame,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        add=Button(Detail_Frame,text="Search",width=10).grid(row=0,column=3,padx=10,pady=8)
        add=Button(Detail_Frame,text="Show all",width=10).grid(row=0,column=4,padx=10,pady=8)

        
#--------------------------Table Frame-------------------------------------------------------

        table=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="green")
        table.place(x=10,y=70,width=760,height=500)
        
        scroll_x=Scrollbar(table,orient=HORIZONTAL)
        scroll_y=Scrollbar(table,orient=VERTICAL)
        
        Student_table=ttk.Treeview(table,columns=("Roll No.","Name","Email","Gender","Contact","D.O.B","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("Roll No.",text="Roll No.")
        Student_table.heading("Name",text="Name")
        Student_table.heading("Contact",text="Contact")
        Student_table.heading("Address",text="Address")
        Student_table.heading("Gender",text="Gender")
        Student_table.heading("Email",text="Email")
        Student_table.heading("D.O.B",text="D.O.B")
        Student_table["show"]="headings"
        Student_table.column("Name",width=100)
        Student_table.column("Roll No.",width=100)
        Student_table.column("Contact",width=100)
        Student_table.column("Address",width=150)
        Student_table.column("Gender",width=100)
        Student_table.column("Email",width=100)
        Student_table.column("D.O.B",width=100)


        Student_table.pack(fill=BOTH,expand=1)
        
        
    
    


root=Tk()
ob=Student(root)
root.mainloop()
 
