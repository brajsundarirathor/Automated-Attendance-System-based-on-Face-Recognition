import tkinter as tk
from tkcalendar import DateEntry
from tkinter import *

class calender:
    def __init__(self,root):
        self.root = root
        self.root.geometry("380x220")
        self.root.title("Calender")
        
        save_btn=Button(self.root,text="Date",command=self.show,font=("times new roman",15,"bold"),bg="blue",fg="white",width=13)
        save_btn.grid(row=0,column=0)
        

    def show(self):
        cal=DateEntry(self.root,SelectMode='day')
        cal.grid(row=1,column=1,padx=15)
    
    
if __name__=="__main__":
    root = Tk()
    obj =calender(root)
    root.mainloop()
