from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
# import smtplib                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           `                                                                                                               `
import time

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("450x600+500+70")
        self.root.config(bg="#fafafa")

        self.otp=''
       
        #Login Frame

        self.var_emp_id=StringVar()
        self.var_password=StringVar()

        Login_Frame=Frame(self.root,bg="seashell2")
        Login_Frame.place(x=50,y=30,width=350,height=400)

        Frametitle=Label(Login_Frame,text="Login",width=10,font=("arial",30,"bold"),bg="black",fg="white").place(x=50,y=10)

        lbl_emp_id=Label(Login_Frame,text="ID",font=("sanserif",15),fg="black",bg="seashell2").place(x=50,y=100)
        txt_emp_id=Entry(Login_Frame,textvariable=self.var_emp_id,font=("times new roman",15),bg="lightgrey",fg="black").place(x=50,y=140,width=180,height=30)

        lbl_password=Label(Login_Frame,text="Password",font=("sanserif",15),fg="black",bg="seashell2").place(x=50,y=200)
        txt_password=Entry(Login_Frame,textvariable=self.var_password,show="*",font=("times new roman",15),bg="lightgrey",fg="black").place(x=50,y=240,width=180,height=30)

        btn_login=Button(Login_Frame,text=" Log In ",font=("Arial",20),bg="green yellow",activebackground="white",fg="black",cursor="hand2",command=self.login).place(x=50,y=300,width=250,height=40)

        #Register Frame

        Sign_Up_Frame=Frame(self.root,bg="seashell3")
        Sign_Up_Frame.place(x=50,y=500,width=350,height=70)

        lbl_register_info=Label(Sign_Up_Frame,text=" ↓Don't have an Account??↓ ",font=("Candara",15,"bold"),bg="deep sky blue",fg="black").place(x=55,y=5)
        btn_sign_up=Button(Sign_Up_Frame,text=" ..Sign Up.. ",font=("",15,"bold"),bg="seashell3",fg="slate blue",cursor="hand2",bd=0,activebackground="white",activeforeground="lime",command=self.sign_up).place(x=90,y=40,width=150,height=20)


    def login(self):
        conn=sqlite3.connect("C:\store management\Database\store.db")
        cur=conn.cursor()
        try:
            if self.var_emp_id.get()=="" or self.var_password.get()=="":
                messagebox.showerror("Error","All Fields are Required",parent=self.root)
            else:
                cur.execute("select u_type from employee where eid=? AND pass=?",(self.var_emp_id.get(),self.var_password.get()))
                employee=cur.fetchone()
                if employee==None:
                    messagebox.showwarning("Warning","Invalid Employee ID or Password",parent=self.root)
                else:
                    #print(employee)
                    if employee[0]=="Admin":
                        self.root.destroy()
                        os.system("python home.py")
                    else:
                        self.root.destroy()
                        os.system("python main_file.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        '''if self.var_emp_id.get()=="" or self.var_password.get()=="":
            messagebox.showerror("Error","All Fields are Required!!!")
        elif self.var_emp_id.get()!="Ayush" or self.var_password.get()!="19875":
                messagebox.showwarning("Warning","Invalid Username or Password\nTry Again with Correct Credentials")
        else:
            messagebox.showinfo("Information",f"Welcome : {self.var_emp_id.get()}\n Your PAssword is {self.var_password.get()}")'''

    def sign_up(self):
        conn=sqlite3.connect("C:\store management\Database\store.db")
        cur=conn.cursor()
        try:
            self.forget_password_window=Toplevel(self.root)
            self.forget_password_window.title("SIGN UP System")
            self.forget_password_window.geometry("900x500+200+40")
            self.forget_password_window.config(bg="#fafafa")
            self.forget_password_window.focus_force()
            #===Employee Entry=====
            self.var_new_emp_id=StringVar()
            self.var_new_gender=StringVar()
            self.var_new_contact=StringVar()
            self.var_new_name=StringVar()
            self.var_new_dob=StringVar()
            self.var_new_doj=StringVar()
            self.var_new_pass=StringVar()
            self.var_new_utype=StringVar()

            title=Label(self.forget_password_window,text="Enter Details",font=("sanserif",18),bg="Black",fg="white").place(x=10,y=15,width=878,height=40)

            #====content=======

            #===row1====

            lbl_new_empid=Label(self.forget_password_window,text="Emp ID",font=("goudy old style",15),bg="#fafafa").place(x=50,y=100)
            lbl_new_name=Label(self.forget_password_window,text="Name",font=("goudy old style",15),bg="#fafafa").place(x=500,y=100)

            txt_new_empid=Entry(self.forget_password_window,textvariable=self.var_new_emp_id,font=("goudy old style",15),bg="lightgrey").place(x=150,y=100,width=200)
            txt_new_name=Entry(self.forget_password_window,textvariable=self.var_new_name,font=("goudy old style",15),bg="lightgrey").place(x=600,y=100,width=200)
            
            #===row2====

            lbl_new_contact=Label(self.forget_password_window,text="Contact",font=("goudy old style",15),bg="#fafafa").place(x=50,y=150)
            lbl_new_pass=Label(self.forget_password_window,text="Password",font=("goudy old style",15),bg="#fafafa").place(x=500,y=150)
            
            txt_new_contact=Entry(self.forget_password_window,textvariable=self.var_new_contact,font=("goudy old style",15),bg="lightgrey").place(x=150,y=150,width=200)            
            txt_new_pass=Entry(self.forget_password_window,textvariable=self.var_new_pass,font=("goudy old style",15),bg="lightgrey").place(x=600,y=150,width=200)
            #===row3===

            lbl_new_dob=Label(self.forget_password_window,text="D.O.B",font=("goudy old style",15),bg="#fafafa").place(x=50,y=200)
            lbl_new_doj=Label(self.forget_password_window,text="D.O.J",font=("goudy old style",15),bg="#fafafa").place(x=500,y=200)

            txt_new_dob=Entry(self.forget_password_window,textvariable=self.var_new_dob,font=("goudy old style",15),bg="lightgrey").place(x=150,y=200,width=200)
            txt_new_doj=Entry(self.forget_password_window,textvariable=self.var_new_doj,font=("goudy old style",15),bg="lightgrey").place(x=600,y=200,width=200)

            #===row4===

            lbl_new_gender=Label(self.forget_password_window,text="Gender",font=("goudy old style",15),bg="#fafafa").place(x=50,y=250)
            lbl_new_utype=Label(self.forget_password_window,text="User Type",font=("goudy old style",15),bg="#fafafa").place(x=500,y=250)

            cmb_new_gender=ttk.Combobox(self.forget_password_window,textvariable=self.var_new_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("sanserif",15))
            cmb_new_gender.place(x=150,y=250,width=200)
            cmb_new_gender.current(0)
            cmb_new_utype=ttk.Combobox(self.forget_password_window,textvariable=self.var_new_utype,values=("Select","Admin","Employee"),state='readonly',justify=CENTER,font=("sanserif",15))
            cmb_new_utype.place(x=600,y=250,width=200)
            cmb_new_utype.current(0)
            


            #===buttons====

            btn_new_add=Button(self.forget_password_window,text="Add User",command=self.new_add,font=("sanserif",15),bg="Black",fg="white",cursor="hand2").place(x=350,y=320,width=200,height=38)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def new_add(self):
                conn=sqlite3.connect("C:\store management\Database\store.db")
                cur=conn.cursor()
                try:
                    if self.var_new_emp_id.get()=="": #or self.var_name.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="":
                        messagebox.showerror("Error","All Fields must be required",parent=self.forget_password_window)
                    else:
                        cur.execute("Select * from employee where eid=?",(self.var_new_emp_id.get(),))
                        row=cur.fetchone()
                        if row!=None:
                            messagebox.showerror("Error","This Employee ID is Alreary Assigned, try different",parent=self.root)
                        else:
                            cur.execute("Insert into employee (eid,name,gender,contact,dob,doj,u_type,pass) values(?,?,?,?,?,?,?,?)",(
                                                self.var_new_emp_id.get(),
                                                self.var_new_name.get(),
                                                self.var_new_gender.get(),
                                                self.var_new_contact.get(), 
                                                self.var_new_dob.get(),
                                                self.var_new_doj.get(),                          
                                                self.var_new_utype.get(),
                                                self.var_new_pass.get(),
                            ))
                            conn.commit()
                            messagebox.showinfo("Succes","Employee Added Successfully",parent=self.forget_password_window)
                        messagebox.showinfo("Success","Sign Up Successful")
                        self.forget_password_window.destroy()
                except Exception as ex:
                    messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.forget_password_window)


root=Tk()
obj=Login_System(root)
root.mainloop()