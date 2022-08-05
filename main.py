from tkinter import *
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime

from student import Student
from train import Train
from FaceRecognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recogition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("Face Recoginition System")
        
        # first image
        img = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\Stanford.jpg")
        img = img.resize((454,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img,master =root)
        
        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=454,height=130)
        
        # second image
        img1 = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\facialrecognition.png")
        img1 = img1.resize((454,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1,master =root)
        
        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=454,y=0,width=454,height=130)
        
        # third image
        img2 = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\u.jpg")
        img2 = img2.resize((454,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2,master=root)
        
        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=908,y=0,width=454,height=130)
        
        # background image
        bgimg = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\bgimg.jpg")
        bgimg = bgimg.resize((1360,768),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(bgimg,master=root)
        
        bg_lbl = Label(self.root,image = self.photoimg3)
        bg_lbl.place(x=0,y=130,width=1360,height=710)
        
        title_lbl = Label(bg_lbl, text="FACE RECOGNITION SYSTEM ", font=("times new roman",35,"bold"),bg="white",fg = "red")
        title_lbl.place(x=0,y=0,width=1366,height = 40)
        
        # student button
        img4 = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\student.jpg")
        img4 = img4.resize((200,150),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4,master=root)
        b1 = Button(bg_lbl,image=self.photoimg4,cursor="hand2",command=self.student_details)
        b1.place(x=150,y=100,width=200,height=150)
        b1_lbl = Button(bg_lbl, text="Student Details",cursor="hand2", command = self.student_details, font=("times new roman",15,"bold"),bg="darkblue",fg = "white")
        b1_lbl.place(x=150,y=250,width=200,height =30)
        
        #detect face button
        img5 = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\face.jpg")
        img5 = img5.resize((200,150),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5,master=root)
        b2 = Button(bg_lbl,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=450,y=100,width=200,height=150)
        b2_lbl = Button(bg_lbl, text="Face Detector",cursor="hand2", command=self.face_data, font=("times new roman",15,"bold"),bg="darkblue",fg = "white")
        b2_lbl.place(x=450,y=250,width=200,height =30)
        
        # Attandence face button
        img6 = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\attandence.jpg")
        img6 = img6.resize((200,150),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6,master=root)
        b3 = Button(bg_lbl,image=self.photoimg6,cursor="hand2", command=self.attendance_data)
        b3.place(x=750,y=100,width=200,height=150)
        b3_lbl = Button(bg_lbl, text="Attendance",cursor="hand2", command=self.attendance_data, font=("times new roman",15,"bold"),bg="darkblue",fg = "white")
        b3_lbl.place(x=750,y=250,width=200,height =30)
        
        # Help button
        img7 = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\help.jpg")
        img7 = img7.resize((200,150),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7,master=root)
        b4 = Button(bg_lbl,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b4.place(x=1050,y=100,width=200,height=150)
        b4_lbl = Button(bg_lbl, text="Help Desk",cursor="hand2", command=self.help_data, font=("times new roman",15,"bold"),bg="darkblue",fg = "white")
        b4_lbl.place(x=1050,y=250,width=200,height =30)
        
        # train face button
        img8 = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\Train.jpg")
        img8 = img8.resize((200,150),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8,master=root)
        b5 = Button(bg_lbl,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=150,y=320,width=200,height=150)
        b5_lbl = Button(bg_lbl, text="Train Data",cursor="hand2", command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg = "white")
        b5_lbl.place(x=150,y=470,width=200,height =30)
        
        # photos
        img9 = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\photos.jpg")
        img9 = img9.resize((200,150),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9,master=root)
        b5 = Button(bg_lbl,image=self.photoimg9,cursor="hand2")
        b5.place(x=450,y=320,width=200,height=150)
        b5_lbl = Button(bg_lbl, text="Photos",cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue",fg = "white")
        b5_lbl.place(x=450,y=470,width=200,height =30)
        
        # developer
        img10 = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\developer.jpg")
        img10 = img10.resize((200,150),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10,master=root)
        b5 = Button(bg_lbl,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b5.place(x=750,y=330,width=200,height=150)
        b5_lbl = Button(bg_lbl, text="Developer",cursor="hand2", command=self.developer_data, font=("times new roman",15,"bold"),bg="darkblue",fg = "white")
        b5_lbl.place(x=750,y=470,width=200,height =30)
        
        # exit
        img11 = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\exit.jpg")
        img11 = img11.resize((200,150),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11,master=root)
        b5 = Button(bg_lbl,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b5.place(x=1050,y=320,width=200,height=150)
        b5_lbl = Button(bg_lbl, text="Exit",cursor="hand2", command=self.iExit, font=("times new roman",15,"bold"),bg="darkblue",fg = "white")
        b5_lbl.place(x=1050,y=470,width=200,height =30)
        
   
        
    def open_img(self):
        os.startfile("C:/Users/brajs/Desktop/Attandecnce System/Data")
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit ?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return 
        
    #function button
    
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
        

        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recogition_System(root)
    root.mainloop()
    
