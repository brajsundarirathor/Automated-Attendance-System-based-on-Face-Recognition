from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("Face Recoginition System")
        
        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman",35,"bold"),bg="white",fg = "darkgreen")
        title_lbl.place(x=0,y=0,width=1360,height = 45)
        
        img_top = Image.open(r"C:/Users/brajs/Desktop/Attandecnce System/images/college_images/face.jpg")
        img_top = img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top,master=root)
        
        f_lbl = Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
        
        img_bottom = Image.open(r"C:/Users/brajs/Desktop/Attandecnce System/images/college_images/bottom.jpg")
        img_bottom = img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom,master=root)
        
        f_lbl = Label(self.root,image = self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="red",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)
    # ======= Attendance ==========
    
    def mark_attendance(self,d,b,a,c):
        with open("MyAttendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split(",")
                name_list.append(entry[0])
            if((a not in name_list) and (b not in name_list) and (c not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%m/%d/%Y")
                dtString=now.strftime("%X")
                f.writelines(f"\n{d},{b},{a},{c},{dtString},{d1},Present")
                    
                
            
        
        
    # Face Recognition function
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)
            cord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                Id,predict=clf.predict(gray_img[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn=mysql.connector.connect(host="localhost",username="root",password="braj",database="face_recognizer")
                mycursor=conn.cursor()
                mycursor.execute("select Name from student where Student_ID="+str(Id))
                a=mycursor.fetchone()
                a="+".join(a)
                mycursor.execute("select RollNo from student where Student_ID="+str(Id))
                b=mycursor.fetchone()
                b="+".join(b)
                mycursor.execute("select Department from student where Student_ID="+str(Id))
                c=mycursor.fetchone()
                c="+".join(c)
                mycursor.execute("select Student_ID from student where Student_ID="+str(Id))
                d=mycursor.fetchone()
                d="+".join(d)
                
                if confidence>77:
                    cv2.putText(img,f"ID:{d}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"RollNo:{b}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{a}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{c}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(d,b,a,c)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face:",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                cord=[x,y,w,y]
                
            return cord
        
        def recognize(img,clf,faceCascade):
            cord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read('Classifier.xml')
        
        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
            
            
                    
                
                


        
        
if __name__=="__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()