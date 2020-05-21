from tkinter import *
from tkinter.ttk import *
base = Tk()


base.geometry("300x370")
base.title("Chatbot")
lb1=Label(base,text="Enter First Name")
lb1.place(x=1,y=30)
en1=Entry(base)
en1.place(x=110,y=30)

lb2=Label(base,text="Enter last Name")
lb2.place(x=1,y=60)
en2=Entry(base)
en2.place(x=110,y=60)

lb3=Label(base,text="Enter E-mail")
lb3.place(x=1,y=90)
en3=Entry(base)
en3.place(x=110,y=90)

lb4=Label(base,text="Contact No.")
lb4.place(x=1,y=120)
en4=Entry(base)
en4.place(x=110,y=120)

lb5=Label(base,text="Enter Gender")
lb5.place(x=1,y=150)
rb1=Radiobutton(base,text="Male",value=1)
rb1.place(x=100,y=150)
rb2=Radiobutton(base,text="Female",value=2)
rb2.place(x=170,y=150)

lb6=Label(base,text="Select Country")
lb6.place(x=1,y=180)
list_con=["India","Italy","China","America","France"]
cb1=Combobox(base,value=list_con)
cb1.place(x=110,y=180)

bt1=Button(base,text="Submit")
bt1.place(x=5,y=220)
bt2=Button(base,text="Clear")
bt2.place(x=100,y=220)
bt3=Button(base,text="Cancel")
bt3.place(x=195,y=220)




base.mainloop()
