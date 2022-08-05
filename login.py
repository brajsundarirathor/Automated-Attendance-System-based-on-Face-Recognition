from tkinter import *
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
from time import strftime
from datetime import datetime
import mysql.connector
import os
from main import Face_Recogition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
    
class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file="C:/Users/brajs/Desktop/Attandecnce System/images/college_images/un.jpg",master=root)
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1 =Image.open("C:/Users/brajs/Desktop/Attandecnce System/images/college_images/LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1,master=root)
        
        f_lbl=Label(image=self.photoimg1,bg="black",borderwidth=0)
        f_lbl.place(x=730,y=175,width=100,height=100)
        
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),bg="black",fg="white")
        get_str.place(x=95,y=100)
        
        # Username
        
        user=Label(frame,text="User Name",font=("times new roman",15,"bold"),bg="black",fg="white")
        user.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        # Password
        
        passw=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        passw.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,show='*',font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        # Icon images
        
        img2 =Image.open("C:/Users/brajs/Desktop/Attandecnce System/images/college_images/LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2,master=root)
        
        f_lbl=Label(image=self.photoimg2,bg="black",borderwidth=0)
        f_lbl.place(x=650,y=323,width=25,height=25)
        
        img3 =Image.open("C:/Users/brajs/Desktop/Attandecnce System/images/college_images/lock-512.png")
        img3=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3,master=root)
        
        f_lbl=Label(image=self.photoimg3,bg="black",borderwidth=0)
        f_lbl.place(x=650,y=393,width=25,height=25)
        
        #Login button
        
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bg="black",fg="white",bd=3,relief=RIDGE)
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required !!")
            
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="password":
            messagebox.showinfo("Success","Welcome to Attendance System")
            self.Main()
            
        else:
            messagebox.showerror("Error","Invalid Username or Password !!")
            
            
    def Main(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recogition_System(self.new_window)
        
       
        
if __name__=="__main__":
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()
        
    


