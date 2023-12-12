from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import sqlite3
import tkinter.messagebox
import datetime
import time
import math
import os
import tempfile
import random
from employee import employeeclass
from category import categoryClass
from supplier import supplierClass

date = datetime.datetime.now().date()
class homepage:
    def __init__(self,root):
        self.root=root
        # heading
        self.heading = Label(text="SK SALES CORPORATIONS", font="arial 40 bold",anchor="w",fg="black", bg="#e5beec")
        self.heading.place(x=0, y=0, relwidth=1,height=70)

        self.log_out = Button(text='Logout',width=30, height=2, bg='red2',fg="black",
                                font=("arial 18 bold"),command=self.logout,cursor="hand2")
        self.log_out.place(x=1180, y=10,width=150,height=50)
        # clock
        self.lbl_clock = Label(text="Welcome to SK SALES CORPORATIONS\t\t\t\t\t\t\t\t\t\t\t Date: "+ str(date) +"", font=("times new roman",15),fg="white", bg="#917fb3")
        self.lbl_clock.place(x=0, y=70, relwidth=1,height=30)
        #left menu
        self.menulogo = Image.open("image/icon.png")
        self.menulogo = self.menulogo.resize((220,130),Image.LANCZOS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)

        leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="dodgerblue3")
        leftmenu.place(x=1138,y=100,width=220,height=595)

        lbl_menulogo=Label(leftmenu,bg="dodgerblue3",image=self.menulogo)
        lbl_menulogo.pack(side=TOP,fill=BOTH)

        self.lbl_menu = Label(leftmenu,text='Menu',width=30, height=2,fg="white",font=("times new roman",20),bg="maroon").pack(side=TOP,fill=BOTH)
        btn_employee = Button(leftmenu,text='Employee',width=30,command=self.employee,height=1,fg="black",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=BOTH)
        btn_supplier = Button(leftmenu,text='Supplier',width=30,command=self.supplier, height=1,fg="black",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=BOTH)
        btn_category = Button(leftmenu,text='Category',width=30,command=self.category, height=1,fg="black",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=BOTH)
        btn_ad_products = Button(leftmenu,text='Add Products',width=30,command=self.adding, height=1,fg="black",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=BOTH)
        btn_up_products = Button(leftmenu,text='Update Product',width=30,command=self.updating, height=1,fg="black",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=BOTH)
        btn_sales = Button(leftmenu,text='Sales',width=30,command=self.open_bill_page, height=1,fg="black",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=BOTH)
        btn_exit = Button(leftmenu,text='Exit',width=30,command=self.exit, height=1,fg="black",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=BOTH)

        #content
        self.lbl_employee = Label(root,text="Total Employee \n[ 0 ]",bg="slateblue4",fg="white", bd=5, relief=RIDGE,font=("arial",20,"bold"))
        self.lbl_employee.place(x=80,y=150,width=300,height=150)
        self.lbl_supplier = Label(root,text="Total Supplier\n [ 0 ]",bg="slateblue1",fg="black", bd=5, relief=RIDGE,font=("arial",20,"bold"))
        self.lbl_supplier.place(x=430,y=150,width=300,height=150)
        self.lbl_add_pd = Label(root,text="Total Products\n [ 0 ]",bg="slateblue4",fg="white", bd=5, relief=RIDGE,font=("arial",20,"bold"))
        self.lbl_add_pd.place(x=780,y=150,width=300,height=150)
        self.lbl_category = Label(root,text="Total Employee \n[ 0 ]",bg="slateblue1",fg="black", bd=5, relief=RIDGE,font=("arial",20,"bold"))
        self.lbl_category.place(x=80,y=340,width=300,height=150)
       
        self.update_content() 
        
    #=====================================================================================
    def update_content(self):
        conn = sqlite3.connect("C:\store management\Database\store.db")
        cur=conn.cursor()
        try:
            #===Employee====
            cur.execute("Select * from employee")
            employee=cur.fetchall()
            #print(len(employee))
            self.lbl_employee.config(text=f"Total Employee \n[{str(len(employee))}]")
            #===Supplier===
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Supplier \n[{str(len(supplier))}]")
            #===Category===
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f"Total Category \n[{str(len(category))}]")
            #===Products====
            cur.execute("select * from inventory")
            inventory=cur.fetchall()
            self.lbl_add_pd.config(text=f"Total Products \n[{str(len(inventory))}]")
        except Exception as ex:
            tkinter.messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeclass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def adding(self):
        # self.master.destroy()
        os.system("python add_to_db.py")
        
    def updating(self):
        # self.master.destroy()
        os.system("python update.py")

    def open_bill_page(self):
        # self.master.destroy()
        os.system("python main_file.py")

    def exit(self):
        self.root.destroy()
        
    def logout(self):
        root.destroy()
        os.system("python login.py")

if __name__ == "__main__":

    root = tk.Tk()
    b = homepage(root)
    root.geometry("1366x700+0+0")
    root.title("Home Page")
    root.config(bg="#2a2f4f")
    root.mainloop()
