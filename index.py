from cProfile import label
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import clear
from matplotlib.backend_bases import cursors
import mysql.connector
from mysqlx import DatabaseError


from requests import get
win=Tk()
win.state('zoomed')
win.config(bg="black")


#=========================button function================
def pd():
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("Error","All fields are Required")
    else:
        con=mysql.connector.connect(host="localhost",username="root",password="Shu@2003",database="mydata")
        my_cursor=con.cursor()
        my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            nameoftablets.get(),
            ref.get(),
            dose.get(),
            nooftablets.get(),
            issuedate.get(),
            expdate.get(),
            dailydose.get(),
            sideeffect.get(),
            nameofpatient.get(),
            dob.get(),
            patientaddress.get()

        ))
        con.commit()
        fetch_data()
        
        con.close()
        messagebox.showinfo("Success","Record has been inserted")


def fetch_data():
        con=mysql.connector.connect(host="localhost",username="root",password="Shu@2003",database="mydata")
        my_cursor=con.cursor()
        my_cursor.execute("select *from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
             table.delete(* table.get_children())
             for items in rows:
                    table.insert("",END,values=items)
             con.commit()

        con.close()
                    

# def get_data(event=""):
#      cursor_row=table.focus()
#      data=table.item(cursor_row)
#      row=data['values']
#      nameoftablets.set(row[0])
#      ref.set(row[1])
#      dose.set(row[2])
#      nooftablets.set(row[3])
#      issuedate.set(row[4])
#      expdate.set(row[5])
#      dailydose.set(row[6])
#      sideeffect.set(row[7])
#      nameofpatient.set(row[8])
#      dob.set(row[9])
#      patientaddress.set(row[10])


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`prescription~Data~~~~~~~~~~
def pre():
     txt_frme.insert(END,"Name of tablets:\t\t\t"+nameoftablets.get()+'\n')
     txt_frme.insert(END,"Reference No.:\t\t\t"+ref.get()+'\n')
     txt_frme.insert(END,"Dose:\t\t\t"+dose.get()+'\n')
     txt_frme.insert(END,"No. of tablets:\t\t\t"+nooftablets.get()+'\n')
     txt_frme.insert(END,"Issue date:\t\t\t"+issuedate.get()+'\n')
     txt_frme.insert(END,"Exp. Date:\t\t\t"+expdate.get()+'\n')
     txt_frme.insert(END,"Daily Dose:\t\t\t"+dailydose.get()+'\n')
     txt_frme.insert(END,"Side Effect:\t\t\t"+sideeffect.get()+'\n')
     txt_frme.insert(END,"Blood Pressure:\t\t\t"+bloodpressure.get()+'\n')
     txt_frme.insert(END,"Storage Device:\t\t\t"+storage.get()+'\n')
     txt_frme.insert(END,"Medication:\t\t\t"+medication.get()+'\n')
     txt_frme.insert(END,"Patient Id:\t\t\t"+patientid.get()+'\n')
     txt_frme.insert(END,"Name of Patient:\t\t\t"+nameofpatient.get()+'\n')
     txt_frme.insert(END,"DOB:\t\t\t"+dob.get()+'\n')
     txt_frme.insert(END,"Patient Address:\t\t\t"+patientaddress.get()+'\n')


     


#=================delete button=====================
def delete():
    con=mysql.connector.connect(host="localhost",username="root",password="Shu@2003",database="mydata")
    my_cursor=con.cursor()
    querry=('delete from hospital where Reference No.=%s')
    value=(ref.get(),)
    my_cursor.execute(querry,value)   
    con.commit()
    con.close()
    fetch_data()
    messagebox.showinfo("Deleted","Patient Data has been deleted")
    

#======================clear button=======================
def clear():
     nameoftablets.set("")
     ref.set("")
     dose.set("")
     nooftablets.set("")
     issuedate.set("")
     expdate.set("")
     dailydose.set("")
     sideeffect.set("")
     bloodpressure.set("")
     storage.set("")
     medication.set("")
     patientid.set("")
     nameofpatient.set("")
     dob.set("")
     patientaddress.set("")
     txt_frme.delete(1.0,END)
     

#==================================exit button===================
def exit():
     confirm=messagebox.askyesno("confirmation","ARE YOU SURE YOU WANT TO EXIT")
     if confirm>0:
            win.destroy()
            return

#=========================================heading============
Label(win,text="Hospital Management System",font="impact 31 bold ",bg="blue",fg="white").pack(fill=X)

#==========================================frame1=============

frame1=Frame(win,bd=15,relief=RIDGE)
frame1.place(x=0,y=54,width=1366,height=310)

# ====================label frame1 patient info================
lf1=LabelFrame(frame1,text="Patient Information",font="arial 10 bold",bd=10,bg="pink")
lf1.place(x=0,y=0,width=750,height=280)


#========================label for patient information====================================

Label(lf1,text="Name of tablet",bg="pink").place(x=5,y=10)
Label(lf1,text="Reference No.",bg="pink").place(x=5,y=40)
Label(lf1,text="Dose",bg="pink").place(x=5,y=70)
Label(lf1,text="No. of Tablets",bg="pink").place(x=5,y=100)
Label(lf1,text="Issue Date",bg="pink").place(x=5,y=130)
Label(lf1,text="Exp. Date",bg="pink").place(x=5,y=160)
Label(lf1,text="Daily Dose",bg="pink").place(x=5,y=190)
Label(lf1,text="Side Effect",bg="pink").place(x=5,y=220)
Label(lf1,text="Blood Pressure",bg="pink").place(x=370,y=10)
Label(lf1,text="Storage Device",bg="pink").place(x=370,y=40)
Label(lf1,text="Medication",bg="pink").place(x=370,y=70)
Label(lf1,text="Patient Id",bg="pink").place(x=370,y=100)
Label(lf1,text="Patient name",bg="pink").place(x=370,y=130)
Label(lf1,text="DOB",bg="pink").place(x=370,y=160)
Label(lf1,text="Patient Address",bg="pink").place(x=370,y=190)



#============================text variable for every entry field

nameoftablets=StringVar()
ref=StringVar()
dose=StringVar()
nooftablets=StringVar()
issuedate=StringVar()
expdate=StringVar()
dailydose=StringVar()
sideeffect=StringVar()
bloodpressure=StringVar()
storage=StringVar()
medication=StringVar()
patientid=StringVar()
nameofpatient=StringVar()
dob=StringVar()
patientaddress=StringVar()


#======================entry field for all labes================

e1=Entry(lf1,bd=4,textvariable=nameoftablets)
e1.place(x=130,y=10,width=200)
e2=Entry(lf1,bd=4,textvariable=ref)
e2.place(x=130,y=40,width=200)
e3=Entry(lf1,bd=4,textvariable=dose)
e3.place(x=130,y=70,width=200)
e4=Entry(lf1,bd=4,textvariable=nooftablets)
e4.place(x=130,y=100,width=200)
e5=Entry(lf1,bd=4,textvariable=issuedate)
e5.place(x=130,y=130,width=200)
e6=Entry(lf1,bd=4,textvariable=expdate)
e6.place(x=130,y=160,width=200)
e7=Entry(lf1,bd=4,textvariable=dailydose)
e7.place(x=130,y=190,width=200)
e8=Entry(lf1,bd=4,textvariable=sideeffect)
e8.place(x=130,y=220,width=200)



e9=Entry(lf1,bd=4,textvariable=bloodpressure)
e9.place(x=500,y=10,width=200)
e10=Entry(lf1,bd=4,textvariable=storage)
e10.place(x=500,y=40,width=200)
e11=Entry(lf1,bd=4,textvariable=medication)
e11.place(x=500,y=70,width=200)
e12=Entry(lf1,bd=4,textvariable=patientid)
e12.place(x=500,y=100,width=200)
e13=Entry(lf1,bd=4,textvariable=nameofpatient)
e13.place(x=500,y=130,width=200)
e14=Entry(lf1,bd=4,textvariable=dob)
e14.place(x=500,y=160,width=200)
e15=Entry(lf1,bd=4,textvariable=patientaddress)
e15.place(x=500,y=190,width=200)







# ====================label frame for Precription================
lf2=LabelFrame(frame1,text="Prescription",font="arial 10 bold",bd=10)
lf2.place(x=760,y=0,width=590,height=280)

#=========================textbox for precription===============

txt_frme=Text(lf2,font="arial 10 bold",width=40,height=30,bg="light green")
txt_frme.pack(fill=BOTH)






#=========================================fram2===============

frame2=Frame(win,bd=15,relief=RIDGE)
frame2.place(x=0,y=360,width=1366,height=290)


#==========================================button==============
d_btn=Button(win,text="Delete",font="arial 15 bold",bg="brown",fg="white",bd=6,cursor="hand2",command=delete)
d_btn.place(x=0,y=655,width=270)


p_btn=Button(win,text="Prescription",font="arial 15 bold",bg="brown",fg="white",bd=6,cursor="hand2",command=pre)
p_btn.place(x=270,y=655,width=330)

pd_btn=Button(win,text="Save prescription data",font="arial 15 bold",bg="green",fg="white",bd=6,cursor="hand2",command=pd)
pd_btn.place(x=600,y=655,width=340)

c_btn=Button(win,text="Clear",font="arial 15 bold",bg="blue",fg="white",bd=6,cursor="hand2",command=clear)
c_btn.place(x=940,y=655,width=170)


e_btn=Button(win,text="Exit",font="arial 15 bold",bg="brown",fg="white",bd=6,cursor="hand2",command=exit)
e_btn.place(x=1110,y=655,width=257)


#=================================SCROLL BAR for precription======================
scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side="bottom",fill=X)
scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side="right",fill=Y)


table=ttk.Treeview(frame2,columns=("Name of tablets","ref","dose","nots","issue date","exp date","Daily dose","side effect","pn","DOB","pa"),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x=ttk.Scrollbar(command=table.xview)
scroll_y=ttk.Scrollbar(command=table.yview)

#=================heading for prescription data=====================================
table.heading("Name of tablets",text="Name of tablet")
table["show"]="headings"
table.heading("ref",text="reference No.")
table["show"]="headings"
table.heading("dose",text="Dose")
table["show"]="headings"
table.heading("nots",text="Number of tablet")
table["show"]="headings"

#issue date","exp date","Daily dose","side effect","DOB"
table.heading("issue date",text="Issue Date")
table["show"]="headings"
table.heading("exp date",text="Exp.Date")
table["show"]="headings"
table.heading("Daily dose",text="Daily Dose")
table["show"]="headings"
table.heading("side effect",text="Side Effect")
table["show"]="headings"

table.heading("pn",text="Patient Name")
table["show"]="headings"
table.heading("DOB",text="DOB")
table["show"]="headings"
table.heading("pa",text="Patient Address")
table["show"]="headings"
table.pack(fill=BOTH,expand=1)


#322222222222222222222222222222222222222222222222
#Name of tablets","ref","dose","nots","issue date","exp date","Daily dose","side effect","DOB","pa
table.column("Name of tablets",width=100)
table.column("ref",width=100)
table.column("dose",width=100)
table.column("nots",width=100)
table.column("issue date",width=100)
table.column("exp date",width=100)
table.column("Daily dose",width=100)
table.column("side effect",width=100)
table.column("DOB",width=100)
table.column("pa",width=100)

# table.bind("<ButtonRelease-1>",get_data())


fetch_data()

mainloop()