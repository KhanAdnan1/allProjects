from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
# from sup_apmc import sup_apmcClass

class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Supplier Management System")
        self.root.config(bg="#fafafa")
        self.root.focus_force()
        #==============================
        # All Variables======

        self.var_searchtxt=StringVar()

        # self.var_date=StringVar()
        self.var_supid=StringVar()
        self.var_company=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        # self.var_cat=StringVar()
        # self.cat_list=[]
        # self.fetch_cat()
        # self.var_desc=StringVar()

        #===searchFrame=====
        SearchFrame=LabelFrame(self.root,text="Search Supplier",font=("goudy old style",12),bd=2,relief=RIDGE,bg="#fafafa")
        SearchFrame.place(x=470,y=40,width=600,height=90)

        #===options===
        lbl_search=Label(SearchFrame,text="Search By Supplier ID",font=("goudy old style",15),bg="#fafafa")
        lbl_search.place(x=10,y=10,width=180)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightgrey").place(x=200,y=10,width=210)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="steelblue",fg="white",cursor="hand2").place(x=430,y=10,width=150,height=30)

        #===title====
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20),bg="#2a2f4f",fg="white").place(x=0,y=0,width=1100,height=40)


        #====content=======

        #===row1====

        # lbl_date=Label(self.root,text="Date",font=("goudy old style bold",18),bg="#fafafa").place(x=50,y=100)
    
        # txt_date=Entry(self.root,textvariable=self.var_date,font=("goudy old style bold",18),bg="lightgrey").place(x=220,y=100,width=210)
    
        #===row2====

        lbl_supid=Label(self.root,text="Supplier ID",font=("goudy old style bold",18),bg="#fafafa").place(x=50,y=150)
        
        txt_supid=Entry(self.root,textvariable=self.var_supid,font=("goudy old style bold",18),bg="lightgrey").place(x=220,y=150,width=210)
        
        #===row3====

        lbl_company=Label(self.root,text="Company",font=("goudy old style bold",18),bg="#fafafa").place(x=50,y=200)
        
        txt_company=Entry(self.root,textvariable=self.var_company,font=("goudy old style bold",18),bg="lightgrey").place(x=220,y=200,width=210)
        
        #===row4====

        lbl_name=Label(self.root,text="Supplier Name",font=("goudy old style bold",18),bg="#fafafa").place(x=50,y=250)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style bold",18),bg="lightgrey").place(x=220,y=250,width=210)
        
        #===row5====

        lbl_contact=Label(self.root,text="Contact",font=("goudy old style bold",18),bg="#fafafa").place(x=50,y=300)
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style bold",18),bg="lightgrey").place(x=220,y=300,width=210)
        
       
        #===buttons====

        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="violet",fg="white",cursor="hand2").place(x=20,y=450,width=130,height=40)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="teal",fg="white",cursor="hand2").place(x=160,y=450,width=130,height=40)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="coral",fg="white",cursor="hand2").place(x=300,y=450,width=130,height=40)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=440,y=450,width=130,height=40)
        # btn_sup_apmc=Button(self.root,text="APMC Supplier",command=self.sup_apmc,font=("goudy old style",15,"bold"),bg="white",cursor="hand2").place(x=10,y=450,width=300,height=30) #image=self.icon_side


        #====Supplier Details===

        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=470,y=150,width=600,height=290)

        scrolly=Scrollbar(sup_frame,orient=VERTICAL)
        scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)

        self.SupplierTable=ttk.Treeview(sup_frame,columns=("supid","company","name","contact"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        # self.var_date.set("")
        # self.SupplierTable.heading("date",text="Date")
        self.SupplierTable.heading("supid",text="Supplier ID")
        self.SupplierTable.heading("company",text="Company")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable["show"]="headings"

        self.SupplierTable.pack(fill=BOTH,expand=1)

        # self.SupplierTable.column("date",width=80)
        self.SupplierTable.column("supid",width=90)
        self.SupplierTable.column("company",width=100)
        self.SupplierTable.column("name",width=200)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#===============================================================================

    def sup_apmc(self):
        self.new_win=Toplevel(self.root)
        # self.new_obj=sup_apmcClass(self.new_win)

    def add(self):
        conn=sqlite3.connect("C:\store management\Database\store.db")
        cur=conn.cursor()
        try:
            if self.var_supid.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_desc.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where supid=?",(self.var_supid.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Supplier ID is Alreary Assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (supid,company,name,contact) values(?,?,?,?)",(
                                        # self.var_date.get(),
                                        self.var_supid.get(),
                                        self.var_company.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                    ))
                    conn.commit()
                    messagebox.showinfo("Succes","Supplier Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        conn=sqlite3.connect("C:\store management\Database\store.db")
        cur=conn.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        #print(row)
        # self.var_date.set(row[0])
        self.var_supid.set(row[0])
        self.var_company.set(row[1])
        self.var_name.set(row[2])
        self.var_contact.set(row[3])

    def update(self):
        conn=sqlite3.connect("C:\store management\Database\store.db")
        cur=conn.cursor()
        try:
            if self.var_supid.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_desc.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where supid=?",(self.var_supid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier ID",parent=self.root)
                else:
                    cur.execute("Update supplier set  company=?,name=?,contact=? where supid=?",(
                                        # self.var_date.get(),
                                        self.var_company.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.var_supid.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Succes","Supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        conn=sqlite3.connect("C:\store management\Database\store.db")
        cur=conn.cursor()
        try:
            if self.var_supid.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_desc.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where supid=?",(self.var_supid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where supid=?",(self.var_supid.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        # self.var_date.set("")
        self.var_supid.set("")
        self.var_company.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        conn=sqlite3.connect("C:\store management\Database\store.db")
        cur=conn.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Supplier ID is Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where supid=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
 

if __name__=="__main__":
    root=Tk()
    #root.resizable(False,False)
    obj=supplierClass(root)
    root.mainloop()
