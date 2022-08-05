from multiprocessing import parent_process
import re
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("Face Recoginition System")
        
        # variables
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_student_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_phone=StringVar()
        self.var_teacher=StringVar()
        
       
        
         # background image
        bgimg = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\bgimg.jpg")
        bgimg = bgimg.resize((1360,768),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(bgimg,master=root)
        
        bg_lbl = Label(self.root,image = self.photoimg3)
        bg_lbl.place(x=0,y=0,width=1360,height=710)
        
        title_lbl = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM ", font=("times new roman",35,"bold"),bg="white",fg = "darkgreen")
        title_lbl.place(x=0,y=0,width=1366,height = 40)
        
        main_frame=Frame(bg_lbl,bd=2)
        main_frame.place(x=5,y=45,width=1345,height=660)
        
        # Left label frame
        
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        left_frame.place(x=10,y=10,width=655,height=630)
        
         # third image
        img_left = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\2.jpeg")
        img_left = img_left.resize((454,130),Image.ANTIALIAS)
        self.photoimg_l = ImageTk.PhotoImage(img_left,master=root)
        
        f_lbl = Label(left_frame,image = self.photoimg_l)
        f_lbl.place(x=5,y=0,width=645,height=130)
        
        
        # Current Course frame
        
        course=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course",font=("times new roman",15,"bold"))
        course.place(x=5,y=135,width=640,height=117)
        
        # Department
        
        dept_lbl=Label(course,text="Department",font=("times new roman",12,"bold"))
        dept_lbl.grid(row=0,column=0,padx=10,sticky=W)
        
        dept_combo=ttk.Combobox(course,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="readonly")
        dept_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical","Electrical","Electronics")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=20,pady=10,sticky=W)
        
         # Course frame
        
        course_lbl=Label(course,text="Course",font=("times new roman",12,"bold"))
        course_lbl.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(course,textvariable=self.var_course,font=("times new roman",10,"bold"),state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=20,pady=10,sticky=W)
        
        # Year frame
        
        year_lbl=Label(course,text="Year",font=("times new roman",12,"bold"))
        year_lbl.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(course,textvariable=self.var_year,font=("times new roman",10,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=20,pady=10,sticky=W)
        
        # Semester frame
        
        sem_lbl=Label(course,text="Semester",font=("times new roman",12,"bold"))
        sem_lbl.grid(row=1,column=2,padx=10,sticky=W)
        
        sem_combo=ttk.Combobox(course,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="readonly")
        sem_combo["values"]=("Select Semester","First Semester","Second Semester")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=20,pady=10,sticky=W)
        
         # Class Student frame
        
        class_student=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",15,"bold"))
        class_student.place(x=5,y=250,width=640,height=350)
        
        # Student ID
        
        student_id_lbl=Label(class_student,text="Student ID",font=("times new roman",12,"bold"))
        student_id_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        student_id_entry=ttk.Entry(class_student,textvariable=self.var_student_id,width=20,font=("times new roman",10,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # Student Name
        
        student_name_lbl=Label(class_student,text="Student Name",font=("times new roman",12,"bold"))
        student_name_lbl.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        student_name_entry=ttk.Entry(class_student,textvariable=self.var_name,width=20,font=("times new roman",10,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # Class Division
        
        student_class_lbl=Label(class_student,text="Student Class",font=("times new roman",12,"bold"))
        student_class_lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        #student_class_entry=ttk.Entry(class_student,textvariable=self.var_div,width=20,font=("times new roman",10,"bold"))
        #student_class_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(class_student,textvariable=self.var_div,width=18,font=("times new roman",10,"bold"),state="readonly")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        # Gender
        
        student_gender_lbl=Label(class_student,text="Student Gender",font=("times new roman",12,"bold"))
        student_gender_lbl.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        #student_gender_entry=ttk.Entry(class_student,textvariable=self.var_gender,width=20,font=("times new roman",10,"bold"))
        #student_gender_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student,textvariable=self.var_gender,width=18,font=("times new roman",10,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        
        # Roll Number
        
        student_roll_lbl=Label(class_student,text="Student Roll No.",font=("times new roman",12,"bold"))
        student_roll_lbl.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        student_roll_entry=ttk.Entry(class_student,textvariable=self.var_roll_no,width=20,font=("times new roman",10,"bold"))
        student_roll_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        # Email
        
        student_email_lbl=Label(class_student,text="Student Email",font=("times new roman",12,"bold"))
        student_email_lbl.grid(row=2,column=2,padx=10,sticky=W)
        
        student_email_entry=ttk.Entry(class_student,textvariable=self.var_email,width=20,font=("times new roman",10,"bold"))
        student_email_entry.grid(row=2,column=3,padx=10,sticky=W)
        
        # Phone number
        
        student_phone_lbl=Label(class_student,text="Student Phone",font=("times new roman",12,"bold"))
        student_phone_lbl.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        student_phone_entry=ttk.Entry(class_student,textvariable=self.var_phone,width=20,font=("times new roman",10,"bold"))
        student_phone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        # Address
        
        student_add_lbl=Label(class_student,text="Student Address",font=("times new roman",12,"bold"))
        student_add_lbl.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        student_add_entry=ttk.Entry(class_student,textvariable=self.var_address,width=20,font=("times new roman",10,"bold"))
        student_add_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        # Teacher Name
        
        student_teacher_lbl=Label(class_student,text="Teacher Name",font=("times new roman",12,"bold"))
        student_teacher_lbl.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        student_teacher_entry=ttk.Entry(class_student,textvariable=self.var_teacher,width=20,font=("times new roman",10,"bold"))
        student_teacher_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        
         # DOB
            
        student_dob_lbl=Label(class_student,text="Student DOB",font=("times new roman",12,"bold"))
        student_dob_lbl.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        #student_dob_entry=ttk.Entry(class_student,textvariable=self.var_dob,width=20,font=("times new roman",10,"bold"))
        #student_dob_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        student_dob_entry=DateEntry(class_student,textvariable=self.var_dob,SelectMode='day',width=20,date_pattern='dd-mm-yyyy')
        student_dob_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        # Radio Button
        
        self.var_radio1=StringVar()
        
        radio1=ttk.Radiobutton(class_student,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio1.grid(row=5,column=0)
        
        radio2=ttk.Radiobutton(class_student,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio2.grid(row=5,column=1)
        
        # Button Frame
        
        btn_frame=Frame(class_student,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=210,width=655,height=100)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",15,"bold"),bg="blue",fg="white",width=13)
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",15,"bold"),bg="blue",fg="white",width=12)
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",15,"bold"),bg="blue",fg="white",width=12)
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",15,"bold"),bg="blue",fg="white",width=13)
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=260,width=775,height=45)
        
        take_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",font=("times new roman",15,"bold"),bg="blue",fg="white",width=27)
        take_btn.grid(row=1,column=0)
        
        up_photo_btn=Button(btn_frame1,text="Update Photo Sample",font=("times new roman",15,"bold"),bg="blue",fg="white",width=27)
        up_photo_btn.grid(row=1,column=1)
        
        # Right label frame
        
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        right_frame.place(x=675,y=10,width=655,height=630)
        
        img_right = Image.open(r"C:\Users\brajs\Desktop\Attandecnce System\images\college_images\u.jpg")
        img_right = img_left.resize((454,130),Image.ANTIALIAS)
        self.photoimg_r = ImageTk.PhotoImage(img_right,master=root)
        
        f_lbl = Label(right_frame,image = self.photoimg_r)
        f_lbl.place(x=5,y=0,width=645,height=130)
        
        # Search System
        
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
        search_frame.place(x=5,y=135,width=640,height=70)
        
        student_search_lbl=Label(search_frame,text="Search By: ",font=("times new roman",12,"bold"))
        student_search_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",10,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll No.","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=20,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(search_frame,text="Search",font=("times new roman",12,"bold"),bg="blue",fg="white",width=8)
        search_btn.grid(row=0,column=3,padx=10)
        
        show_all_btn=Button(search_frame,text="Show All",font=("times new roman",12,"bold"),bg="blue",fg="white",width=8)
        show_all_btn.grid(row=0,column=4,padx=10)
       
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=640,height=390)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
    # function declaration
    
    def add_data(self):
        pattern='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w+[.]\w{2,3}$'
        z=re.search(pattern,str(self.var_email.get()))
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif (z is None):
            messagebox.showerror("Error","Invalid mail id",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="braj",database="face_recognizer")
                mycursor=conn.cursor()
                mycursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",   (self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_student_id.get(),self.var_name.get(),     self.var_div.get(),self.var_roll_no.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),
                                                                                                          self.var_teacher.get(),self.var_radio1.get()))
        
            
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                
                
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="braj",database="face_recognizer")
        mycursor=conn.cursor()
        mycursor.execute("select * from student")
        data=mycursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]) 
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_student_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll_no.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

       
    def update_data(self):
        pattern='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w+[.]\w{2,3}$'
        z=re.search(pattern,str(self.var_email.get()))
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif (z is None):
            messagebox.showerror("Error","Invalid mail id",parent=self.root)
        
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student's details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="braj",database="face_recognizer")
                    mycursor=conn.cursor()
                    mycursor.execute("update student set Department=%s, Course=%s, Year=%s, Semester=%s, Student_ID=%s, Name=%s, Division=%s, RollNo=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher_Name=%s, PhotoSampleStatus=%s where Student_ID=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_student_id.get(),self.var_name.get(),     self.var_div.get(),self.var_roll_no.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),
                                                                                                          self.var_teacher.get(),self.var_radio1.get(), self.var_student_id.get()))
                 
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success","Student's details successfully updated",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                
    def delete_data(self):
        if self.var_student_id.get()=="":
            messagebox.showerror("Error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this student's details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="braj",database="face_recognizer")
                    mycursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_student_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student's details successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                

    def reset_data(self):
        self.var_dep.set("Select Department") 
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_student_id.set("")
        self.var_name.set("")
        self.var_div.set("A")
        self.var_roll_no.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
    #======================== Generate dataset and Take photo samples ===============================
    
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="braj",database="face_recognizer")
                mycursor=conn.cursor()
                mycursor.execute("select * from student")
                myresult=mycursor.fetchall()
                Id=0
                for x in myresult:
                    Id+=1
                mycursor.execute("update student set Department=%s, Course=%s, Year=%s, Semester=%s, Student_ID=%s, Name=%s, Division=%s, RollNo=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher_Name=%s, PhotoSampleStatus=%s where Student_ID=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_student_id.get(),self.var_name.get(),     self.var_div.get(),self.var_roll_no.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),
                                                                                                          self.var_teacher.get(),self.var_radio1.get(), self.var_student_id.get()==Id+1))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray, 1.3 ,5)
                    #scaling=1.3
                    #neighbours=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path="C:/Users/brajs/Desktop/Attandecnce System/Data/"
                        my_photo="User."+str(Id)+"."+str(img_id)+".png"
                        cv2.imwrite(os.path.join(file_name_path,my_photo),face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                        
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                
                
                
                
                
                        
                    
                        

                    
                    


       
           

                    
       
        
        
       
       
        

if __name__=="__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
