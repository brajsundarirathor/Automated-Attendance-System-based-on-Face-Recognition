from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("Face Recoginition System")
        
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        
        # first image
        img = Image.open(r"C:/Users/brajs/Desktop/Attandecnce System/images/college_images/smart-attendance.jpg")
        img = img.resize((800,200),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img,master =root)
        
        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
        # second image
        img1 = Image.open(r"C:/Users/brajs/Desktop/Attandecnce System/images/college_images/bg.jpg")
        img1 = img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1,master =root)
        
        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
        #bg img
        bgimg = Image.open(r"C:/Users/brajs/Desktop/Attandecnce System/images/college_images/bgimg.jpg")
        bgimg = bgimg.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(bgimg,master=root)
        
        bg_lbl = Label(self.root,image = self.photoimg3)
        bg_lbl.place(x=0,y=200,width=1530,height=710)
        
        title_lbl = Label(bg_lbl, text="ATTENDANCE MANAGEMENT SYSTEM ", font=("times new roman",35,"bold"),bg="white",fg = "darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height = 45)
        
        main_frame=Frame(bg_lbl,bd=2)
        main_frame.place(x=20,y=50,width=1500,height=600)
        
        # Left label frame
        
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",15,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)
        
        img_left = Image.open(r"C:/Users/brajs/Desktop/Attandecnce System/images/college_images/2.jpeg")
        img_left = img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_l = ImageTk.PhotoImage(img_left,master=root)
        
        f_lbl = Label(left_frame,image = self.photoimg_l)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=400)
        
        # Lable and Entry
        # Attendance ID
        
        attendance_id_lbl=Label(left_inside_frame,text="Attendance ID",font=("times new roman",12,"bold"))
        attendance_id_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendance_id_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",10,"bold"))
        attendance_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # Roll No.
        
        roll_lbl=Label(left_inside_frame,text="Roll:",bg="white",font=("times new roman",12,"bold"))
        roll_lbl.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",10,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # Name
        
        name_lbl=Label(left_inside_frame,text="Name:",bg="white",font=("times new roman",12,"bold"))
        name_lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",10,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        # Department
        
        dept_lbl=Label(left_inside_frame,text="Department:",bg="white",font=("times new roman",12,"bold"))
        dept_lbl.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",10,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        # Time
        
        time_lbl=Label(left_inside_frame,text="Time:",bg="white",font=("times new roman",12,"bold"))
        time_lbl.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",10,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        # Date
        
        date_lbl=Label(left_inside_frame,text="Date:",bg="white",font=("times new roman",12,"bold"))
        date_lbl.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        date_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",10,"bold"))
        date_time.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        # Attendance
        
        attendance_lbl=Label(left_inside_frame,text="Attendance Status:",bg="white",font=("times new roman",12,"bold"))
        attendance_lbl.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        # Button Frame
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=700,height=70)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,font=("times new roman",15,"bold"),bg="blue",fg="white",width=14)
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,font=("times new roman",15,"bold"),bg="blue",fg="white",width=14)
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",15,"bold"),bg="blue",fg="white",width=14)
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",15,"bold"),bg="blue",fg="white",width=14)
        reset_btn.grid(row=0,column=3)
        
        
        
        # Right label frame
        
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",15,"bold"))
        right_frame.place(x=755,y=10,width=730,height=580)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=700,height=455)
        
        # ========= Scroll Bar Table =========
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll Number")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    # import csv
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    # export csv
    
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" sucessfully.")
                
        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
    
    def update_data(self):
        messagebox.showerror("Error","You can't update data.",parent=self.root)
        
    
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
    
            
                
        
        
        
if __name__=="__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()