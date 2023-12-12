from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
# from cat_apmc import cat_apmcClass


class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x550+220+130")
        self.root.title("Category Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        #=============================
        #####Variables=====
        self.var_cat_id=StringVar()
        self.var_main_name=StringVar()
        self.var_sub_name=StringVar()
        #======Title======
        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#2a2f4f",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=0)
        #======Entry Frame=====
        
        entry_frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        entry_frame.place(x=30,y=80,width=510,height=450)

        lbl_cid=Label(entry_frame,text="   Category ID",font=("goudy old style",20),bg="white").place(x=10,y=10)
        lbl_m_name=Label(entry_frame,text="Category Name",font=("goudy old style",20),bg="white").place(x=10,y=60)
        # lbl_s_name=Label(entry_frame,text="Sub Category Name",font=("goudy old style",20),bg="white").place(x=10,y=100)

        lbl_cid=Entry(entry_frame,textvariable=self.var_cat_id,font=("goudy old style",20),bg="lightyellow").place(x=250,y=10,width=150)
        #cmb_m_name=ttk.Combobox(entry_frame,textvariable=self.var_main_name,values=("Select","Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",20))
        #cmb_m_name.place(x=250,y=50,width=200)
        #cmb_m_name.current(0)
        #cmb_s_name=ttk.Combobox(entry_frame,textvariable=self.var_sub_name,values=("Select","Admin",input()),state='readonly',justify=CENTER,font=("goudy old style",20))
        #cmb_s_name.place(x=250,y=100,width=200)
        #cmb_s_name.current(0)
        lbl_m_name=Entry(entry_frame,textvariable=self.var_main_name,font=("goudy old style",20),bg="lightyellow").place(x=250,y=60,width=150)
        # lbl_s_name=Entry(entry_frame,textvariable=self.var_sub_name,font=("goudy old style",20),bg="lightyellow").place(x=250,y=100,width=150)

        btn_add=Button(entry_frame,text="Add",command=self.add,font=("goudy old style",15),bg="#2a2f4f",fg="white",cursor="hand2").place(x=250,y=150,width=250,height=50)
        btn_delete=Button(entry_frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#ff0000",fg="white",cursor="hand2").place(x=250,y=220,width=250,height=50)
        # btn_cat_apmc=Button(entry_frame,text="APMC Category",command=self.cat_apmc,font=("goudy old style",15,"bold"),bg="white",cursor="hand2").place(x=10,y=150,width=200,height=40)
        
        #====Category Details===
        
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=570,y=80,width=490,height=450)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.CategoryTable=ttk.Treeview(cat_frame,columns=("cid","m_name"))
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)

        self.CategoryTable.heading("cid",text="Category ID")
        self.CategoryTable.heading("m_name",text="Main Category")
        # self.CategoryTable.heading("s_name",text="Sub Category")
        self.CategoryTable["show"]="headings"

        self.CategoryTable.column("cid",width=80)
        self.CategoryTable.column("m_name",width=100)
        # self.CategoryTable.column("s_name",width=100)
        self.CategoryTable.pack(fill=BOTH,expand=1)

        self.CategoryTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

        #===images======
        #self.im1=Image.open("images/cat.jpg")
        #self.im1=self.im1.resize((500,220),Image.ANTIALIAS)
        #self.im1=ImageTk.PhotoImage(self.im1)

        #self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        #self.lbl_im1.place(x=40,y=270)

        #self.im2=Image.open("images/category.jpg")
        #self.im2=self.im2.resize((500,220),Image.ANTIALIAS)
        #self.im2=ImageTk.PhotoImage(self.im2)

        #self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        #self.lbl_im2.place(x=580,y=270)

        #=======Functions===========

    def cat_apmc(self):
        self.new_win=Toplevel(self.root)
        # self.new_obj=cat_apmcClass(self.new_win)

    def add(self):
        conn = sqlite3.connect("C:\store management\Database\store.db")
        cur=conn.cursor()
        try:
            if self.var_cat_id.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_desc.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields must be required",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Category ID is Alreary Assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into category(cid,m_name) values(?,?)",(
                                        self.var_cat_id.get(),
                                        self.var_main_name.get()
                                        #self.var_sub_name.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Succes","Category Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        conn = sqlite3.connect("C:\store management\Database\store.db")        
        cur=conn.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.CategoryTable.focus()
        content=(self.CategoryTable.item(f))
        row=content['values']
        # #print(row)
        self.var_cat_id.set(row[0])
        self.var_main_name.set(row[1])
        
    def delete(self):
        conn = sqlite3.connect("C:\store management\Database\store.db")
        cur=conn.cursor()
        try:
            if self.var_cat_id.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_desc.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","please select category from the list",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error, please try again",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_main_name.set("")
                        #self.var_sub_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    
    #root.resizable(False,False)
    obj=categoryClass(root)
    root.mainloop()
