from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("Face Recoginition System")
        
        title_lbl = Label(self.root, text="Developer", font=("times new roman",35,"bold"),bg="white",fg = "darkgreen")
        title_lbl.place(x=0,y=0,width=1360,height = 45)
        
        img_top = Image.open(r"C:/Users/brajs/Desktop/Attandecnce System/images/college_images/dev.jpg")
        img_top = img_top.resize((1360,710),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top,master=root)
        
        f_lbl = Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1360,height=710)
        
        # frame
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=850,y=0,width=500,height=600)
        
        img_top1 = Image.open(r"C:/Users/brajs/Desktop/Attandecnce System/images/college_images/tony.jpg")
        img_top1 = img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1,master=root)
        
        f_lbl1 = Label(main_frame,image = self.photoimg_top1)
        f_lbl1.place(x=300,y=0,width=200,height=200)
        
        # Developer Information
        
        dev_lbl=Label(main_frame,text="Hello my name is Tony Stark !!!",font=("times new roman",15,"bold"))
        dev_lbl.place(x=0,y=5)
        
        intro_lbl=Label(main_frame,text="I am a Machine Learning Engineer !!!",font=("times new roman",12,"bold"))
        intro_lbl.place(x=0,y=40)
        
        img2 = Image.open(r"C:/Users/brajs/Desktop/Attandecnce System/images/college_images/bg.jpg")
        img2 = img2.resize((500,390),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2,master=root)
        
        f_lbl = Label(main_frame,image = self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=390)
        
        
if __name__=="__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
