#import all modules
from tkinter import *
import tkinter as tk
import sqlite3
import tkinter.messagebox
from tkinter import ttk,messagebox

conn = sqlite3.connect("C:\store management\Database\store.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) from inventory")
for r in result:
    id = r[0]
class Database:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.heading = Label(master,text="Add Products", font=('goudy old style',20),fg='white',bg="#2a2f4f")
        self.heading.place(width=1370,height=40,x=0,y=0)

        # self.btn_clear = Button(master, text="return", width=18, height=2, bg='red',fg='white',command=self.clear_all)
        # self.btn_clear.place(x=0, y=10)

    #label and entries for the window
        self.category=Label(master,text="Enter Category",font=("arial 18 bold")).place(x=0,y=50) 
        
        # self.name_l = Label(master, text="Enter the Product Name", font=("arial 18 bold"))
        # self.name_l.place(x=0, y=100)

        self.sr_no_l = Label(master, text="Enter the Serial Number", font=("arial 18 bold"))
        self.sr_no_l.place(x=0, y=100)

        self.stock_l = Label(master, text="Enter Stock In Meter", font=("arial 18 bold"))
        self.stock_l.place(x=0, y=150)

        self.cp_l = Label(master, text="Enter Cost price", font=("arial 18 bold"))
        self.cp_l.place(x=0, y=200)

        self.sp_l = Label(master, text="Enter Selling price", font=("arial 18 bold"))
        self.sp_l.place(x=0, y=250)

        self.vendor_l = Label(master, text="Enter the Vendor Name", font=("arial 18 bold"))
        self.vendor_l.place(x=0, y=300)

        self.vendor_phone_l = Label(master, text="Enter the Vendor Number", font=("arial 18 bold"))
        self.vendor_phone_l.place(x=0, y=350)

        self.id_l = Label(master, text="Enter ID", font=("arial 18 bold"))
        self.id_l.place(x=0, y=400)
        
        self.status=Label(master,text="Status",font=("arial 18 bold"))
        self.status.place(x=0,y=450) 

        #entries for the labels
        self.category_e=ttk.Combobox(master, width=24,values=("Select","Rexine","Velvet","Carpet"),state='readonly',justify=CENTER,font=("arial 18"))
        self.category_e.place(x=380,y=55)
        self.category_e.current(0)

        # self.name_e = Entry(master,width=25,font=("arial 18 bold"))
        # self.name_e.place(x=380,y=100)

        self.sr_no_e = Entry(master,width=25,font=("arial 18 bold"))
        self.sr_no_e.place(x=380,y=100)

        self.stock_e = Entry(master,width=25,font=("arial 18 bold"))
        self.stock_e.place(x=380,y=150)

        self.cp_e = Entry(master,width=25,font=("arial 18 bold"))
        self.cp_e.place(x=380,y=200)

        self.sp_e = Entry(master,width=25,font=("arial 18 bold"))
        self.sp_e.place(x=380,y=250)

        self.vendor_e = Entry(master,width=25,font=("arial 18 bold"))
        self.vendor_e.place(x=380,y=300)

        self.vendor_phone_e = Entry(master,width=25,font=("arial 18 bold"))
        self.vendor_phone_e.place(x=380,y=350)

        self.id_e = Entry(master,width=25,font=("arial 18 bold"))
        self.id_e.place(x=380,y=400)

        self.status_e=ttk.Combobox(master,width=24,values=("Select","Active","Inactive"),state='readonly',justify=CENTER,font=("arial 18"))
        self.status_e.place(x=380,y=450)
        self.status_e.current(0)

        #button to add to the database
        self.btn_add = Button(master,text="Add to Database",width=25,height=2,bg="black",fg="white",command=self.get_items)
        self.btn_add.place(x=550,y=520)

        self.btn_clear = Button(master, text="Clear All Fields", width=18, height=2, bg='red',fg='white',command=self.clear_all)
        self.btn_clear.place(x=380, y=520)

        #text box for logs
        self.tBox = Text(master,width=60,height=21)
        self.tBox.place(x=750,y=100)
        self.tBox.insert(END, "ID has reached upto: " + str(id))

    def get_items(self,*args,**kwargs):
        #get from Entries
        self.category = self.category_e.get()
        # self.name = self.name_e.get()
        self.sr_no = self.sr_no_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()
        self.status = self.status_e.get()

        #dynamic entries
        self.totalcp = float(self.cp) * float(self.stock) if self.cp and self.stock else 0.0
        try:
             self.totalsp = float(self.sp) * float(self.stock)
        except ValueError:
            self.totalsp = 0.0 

        self.assumed_profit = float(self.totalsp) - float(self.totalcp)

        if self.category == ''or self.sr_no == '' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo("Error","please fill all the entries")
        else:
            sql = "INSERT INTO inventory (category, sr_no, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phone,status) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.category,self.sr_no,self.stock,self.cp,self.sp,self.totalcp,self.totalsp,self.assumed_profit,self.vendor,self.vendor_phone,self.status))
            conn.commit()
            # textBox insert
            self.tBox.insert(END,"\n \nInserted " + str(self.category) + " Into the database with code " + str(self.id_e.get()))
            tkinter.messagebox.showinfo("Success","Sucessfully added to the database")
    def clear_all(self,*args,**kwargs):
        self.category_e.delete(0, END)
        # self.name_e.delete(0, END)
        self.sr_no_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phone_e.delete(0, END)
        self.id_e.delete(0, END)
        self.status_e.delete(0,END)

    
root=Tk()
b = Database(root)

root.geometry("1366x768+0+100")
root.title("Add to the database")


root.mainloop()
