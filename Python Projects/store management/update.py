#import all modules
from tkinter import *
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
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_id=StringVar()
        self.var_category=StringVar()
        self.var_sr_no=StringVar()
        self.var_stock=StringVar()
        self.var_cp=StringVar()
        self.var_sp=StringVar()
        self.var_totalcp=StringVar()
        self.var_totalsp=StringVar()
        self.var_assumed_profit=StringVar()
        self.var_vendor=StringVar()
        self.var_vendor_phone=StringVar()
        self.var_status=StringVar()

        self.master = master
        self.heading = Label(master,text="Update Products", font=('goudy old style',20),fg='white',bg="#2a2f4f")
        self.heading.place(x=0,y=0,width=1370,height=40)
    
    #label and Entry for id
        self.id_le = Label(master,text="Enter id", font=("arial 18 bold"))
        self.id_le.place(x=0,y=70)

        self.id_leb = Entry(master, font=("arial 18 bold"), width=25)
        self.id_leb.place(x=380, y=70)

        # self.btn_search = Button(master, text="Search", width=15, height=2, bg="orange", command=self.search)
        # self.btn_search.place(x=550,y=68)
    #label and entries for the window
        # self.name_l = Label(master, text="Enter the Product Name", font=("arial 18 bold"))
        # self.name_l.place(x=0, y=120)
        self.category=Label(master,text="Enter Category",font=("arial 18 bold")).place(x=0, y=120) 

        self.sr_no_l = Label(master, text="Enter the Serial Number", font=("arial 18 bold"))
        self.sr_no_l.place(x=0, y=170)

        self.stock_l = Label(master, text="Enter Stock In Meter", font=("arial 18 bold"))
        self.stock_l.place(x=0, y=220)

        self.cp_l = Label(master, text="Enter Cost price", font=("arial 18 bold"))
        self.cp_l.place(x=0, y=270)

        self.sp_l = Label(master, text="Enter Selling price", font=("arial 18 bold"))
        self.sp_l.place(x=0, y=320)

        self.totalcp_l = Label(master, text="Enter Total cost price", font=("arial 18 bold"))
        self.totalcp_l.place(x=0, y=370)

        self.totalsp_l = Label(master, text="Enter Total Selling price", font=("arial 18 bold"))
        self.totalsp_l.place(x=0, y=420)

        self.vendor_l = Label(master, text="Enter the Vendor Name", font=("arial 18 bold"))
        self.vendor_l.place(x=0, y=470)

        self.vendor_phone_l = Label(master, text="Enter the Vendor Number", font=("arial 18 bold"))
        self.vendor_phone_l.place(x=0, y=520)

        self.status=Label(master,text="Status",font=("arial 18 bold"))
        self.status.place(x=0,y=570) 


        #entries for the labels
        # self.name_e = Entry(master,width=25,font=("arial 18 bold"))
        # self.name_e.place(x=380,y=120)
        self.category_e=ttk.Combobox(master, width=24,values=("Select","Rexine","Velvet","Carpet"),state='readonly',justify=CENTER,font=("arial 18"))
        self.category_e.place(x=380,y=120)
        self.category_e.current(0)

        self.sr_no_e = Entry(master,width=25,font=("arial 18 bold"))
        self.sr_no_e.place(x=380,y=170)

        self.stock_e = Entry(master,width=25,font=("arial 18 bold"))
        self.stock_e.place(x=380,y=220)

        self.cp_e = Entry(master,width=25,font=("arial 18 bold"))
        self.cp_e.place(x=380,y=270)

        self.sp_e = Entry(master,width=25,font=("arial 18 bold"))
        self.sp_e.place(x=380,y=320)

        self.totalcp_e = Entry(master,width=25,font=("arial 18 bold"))
        self.totalcp_e.place(x=380,y=370)

        self.totalsp_e = Entry(master,width=25,font=("arial 18 bold"))
        self.totalsp_e.place(x=380,y=420)

        self.vendor_e = Entry(master,width=25,font=("arial 18 bold"))
        self.vendor_e.place(x=380,y=470)

        self.vendor_phone_e = Entry(master,width=25,font=("arial 18 bold"))
        self.vendor_phone_e.place(x=380,y=520)

        self.status_e=ttk.Combobox(master,width=24,values=("Select","Active","Inactive"),state='readonly',justify=CENTER,font=("arial 18"))
        self.status_e.place(x=380,y=570)
        self.status_e.current(0)

        #button to add to the database
        self.btn_add = Button(master, text="Update",width=20,height=2,bg='#2a2f4f',fg="white", command=self.update)
        self.btn_add.place(x=550,y=620)
        self.btn_add = Button(master, text="Delete",width=20,height=2,bg="red",fg="white", command=self.delete)
        self.btn_add.place(x=380,y=620)

        #text box for logs
        # self.tBox = Text(master,width=60,height=21,font=("goudy old style", 12))
        # self.tBox.place(x=750,y=70)
        # self.tBox.insert(END,"\n  FOR REXINE SEARCH ID FROM 0-100."+"\n\n  FOR VELVET SEARCH ID FROM 101-200."+"\n\n  FOR CARPET SEARCH ID FROM 201-250.")
        #Search
        SearchFrame=LabelFrame(root,text="Search Product",font=("goudy old style",12))
        SearchFrame.place(x=750,y=60,width=600,height=80)

        #===options===
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","vendor","sr_no"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search1,font=("goudy old style",15),bg="steelblue",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #product detail
        product_frame=Frame(root,bd=3,relief=RIDGE)
        product_frame.place(x=750,y=170,width=600,height=390)

        scrolly=Scrollbar(product_frame,orient=VERTICAL)
        scrollx=Scrollbar(product_frame,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(product_frame,columns=("id","category", "sr_no", "stock", "cp", "sp", "totalcp", "totalsp", "vendor", "vendor_phone","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=TOP,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading("id",text="Id")
        self.ProductTable.heading("category",text="Category")
        self.ProductTable.heading("sr_no",text="srno")
        self.ProductTable.heading("stock",text="Stock")
        self.ProductTable.heading("cp",text="cp")
        self.ProductTable.heading("sp",text="sp")
        self.ProductTable.heading("totalcp",text="totalcp")
        self.ProductTable.heading("totalsp",text="totalsp")
        # self.ProductTable.heading("assumed_profit",text="assumed_profit")
        self.ProductTable.heading("vendor",text="vendor")       
        self.ProductTable.heading("vendor_phone",text="vendor_phone")
        self.ProductTable.heading("status",text="Status")
        self.ProductTable["show"]="headings"

        self.ProductTable.column("id",width=100)
        self.ProductTable.column("category",width=100)
        self.ProductTable.column("sr_no",width=100)
        self.ProductTable.column("stock",width=100)
        self.ProductTable.column("cp",width=100)
        self.ProductTable.column("sp",width=100)
        self.ProductTable.column("totalcp",width=100)
        self.ProductTable.column("totalsp",width=100)
        # self.ProductTable.column("assumed_profit",width=100)
        self.ProductTable.column("vendor",width=100)
        self.ProductTable.column("vendor_phone",width=100)  
        self.ProductTable.column("status",width=100)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
    # def get_data(self,ev):
    #     f=self.ProductTable.focus()
    #     content=(self.ProductTable.item(f))
    #     row=content['values']
    #     #print(row)
    #     self.var_id.set(row[0])
    #     self.var_category.set(row[1])
    #     self.var_sr_no.set(row[2])
    #     self.var_stock.set(row[3])
    #     self.var_cp.set(row[4])
    #     self.var_sp.set(row[5])
    #     self.var_totalcp.set(row[6])
    #     self.var_totalsp.set(row[7])
    #     # self.var_assumed_profit.set(row[8])
    #     self.var_vendor.set(row[8])
    #     self.var_vendor_phone.set(row[9])
    #     self.var_status.set(row[10])
    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        # #print(row)
        self.var_id.set(row[0])
        self.var_category.set(row[1])
        self.var_sr_no.set(row[2])
        self.var_stock.set(row[3])
        self.var_cp.set(row[4])
        self.var_sp.set(row[5])
        self.var_totalcp.set(row[6])
        self.var_totalsp.set(row[7])
        # self.var_assumed_profit.set(row[8])
        self.var_vendor.set(row[8])
        self.var_vendor_phone.set(row[9])
        self.var_status.set(row[10])

    # def search(self, *args, **kwargs):
    #     sql = "SELECT * FROM inventory WHERE id=?"
    #     result = c.execute(sql,(self.id_leb.get(), ))
    #     for r in result:
    #         self.n1 = r[1] #category
    #         self.n2 = r[2] #sr_no
    #         self.n3 = r[3] #stock
    #         self.n4 = r[4] #cp
    #         self.n5 = r[5] #sp
    #         self.n6 = r[6] #totalcp
    #         self.n7 = r[7] #totalsp
    #         self.n8 = r[8] #assumed_profit
    #         self.n9 = r[9] #vendor
    #         self.n10 = r[10] #vendor_phone
    #         self.n11 = r=[11] #status
    #     conn.commit()

    #     #insert into the entries to update
    #     self.category_e.delete(0, END)
    #     self.category_e.insert(0, str(self.n1))

    #     self.sr_no_e.delete(0, END)
    #     self.sr_no_e.insert(0, str(self.n2))

    #     self.stock_e.delete(0, END)
    #     self.stock_e.insert(0, str(self.n3))

    #     self.cp_e.delete(0, END)
    #     self.cp_e.insert(0, str(self.n4))

    #     self.sp_e.delete(0, END)
    #     self.sp_e.insert(0, str(self.n5))

    #     self.vendor_e.delete(0, END)
    #     self.vendor_e.insert(0, str(self.n9))

    #     self.vendor_phone_e.delete(0, END)
    #     self.vendor_phone_e.insert(0, str(self.n10))

    #     self.totalcp_e.delete(0, END)
    #     self.totalcp_e.insert(0, str(self.n6))

    #     self.totalsp_e.delete(0, END)
    #     self.totalsp_e.insert(0, str(self.n7))
        
    #     self.status_e.delete(0, END)
    #     self.status_e.insert(0, str(self.n11))
    
    def update(self, *args, **kwargs):
        #get all the update values
        self.u0 = self.id_le.get()
        self.u1 = self.category_e.get()
        self.u2 = self.sr_no_e.get()
        self.u3 = self.stock_e.get()
        self.u4 = self.cp_e.get()
        self.u5 = self.sp_e.get()
        self.u6 = self.totalcp_e.get()
        self.u7 = self.totalsp_e.get()
        self.u8 = self.vendor_e.get()
        self.u9 = self.vendor_phone_e.get()
        self.u10 = self.status_e.get()

        query = "UPDATE inventory SET category=?, sr_no=?, stock=?, cp=?, sp=?, totalcp=?, totalsp=?, vendor=?, vendor_phone=?, status=? WHERE id=?"
        c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.u8, self.u9,self.u10, self.id_leb.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Updated Database Successfully")
    def show(self):
        conn = sqlite3.connect("C:\store management\Database\store.db")
        cur=conn.cursor()
        try:
            cur.execute("Select * from inventory")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=root)
    def delete(self):
        conn = sqlite3.connect("C:\store management\Database\store.db")
        cur=conn.cursor()
        try:
            if self.id_leb.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_desc.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","please select Product for deleting",parent=root)
            else:
                cur.execute("Select * from inventory where id=?",(self.id_leb.get(),))    
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error, please try again",parent=root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.id_leb.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete","product Deleted Successfully",parent=root)
                        self.show()
                        self.id_leb.set("")
                        # self.category_e.set("")
                        #self.var_sub_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=root)
        
    def search1(self):
        conn = sqlite3.connect("C:\store management\Database\store.db")
        cur=conn.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search Input is Required",parent=root)
            else:
                cur.execute("Select * from inventory where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=root)


root=Tk()
b = Database(root)

root.geometry("1366x768+0+30")
root.title("Update the database")


root.mainloop()