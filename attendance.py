from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
# from main import Face_Recognition_System




class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendly- Face Recognition Attendance System")
        
        # face image 1
        img1=Image.open(r"college_images\attendance1.jpg")
        img1=img1.resize((800,250),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=800,height=250)
        
        # face image 2
        img2=Image.open(r"college_images\attendance2.jpg")
        img2=img2.resize((800,250),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=800,height=250)
        
        # background image
        img4=Image.open(r"college_images\attendance_bg.jpg")
        img4=img4.resize((1530,550),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=250,width=1530,height=550)
        
        title_lbl=Button(bg_img,text="Attendance Mangagement System",font=("times new roman",34,"bold"),bg="black",fg="White")
        title_lbl.place(x=0,y=0,width=1530,height=55)
        
        main_frame=Frame(bg_img,bd=2, bg="white")
        main_frame.place(x=10,y=65,width=1500,height=490)
#-------------------------------------------------------------------------------------------------------------------------------------------------------        
#-------------------------------------------------------------------------------------------------------------------------------------------------------
        # left Label frame
        
        Left_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE, text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=30,y=10,width=700,height=470)
        
        img_left1=Image.open(r"college_images\Face_attendance 01.jpg")
        img_left1=img_left1.resize((680,130),Image.Resampling.LANCZOS)
        self.photoimg_left1=ImageTk.PhotoImage(img_left1)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left1)
        f_lbl.place(x=10,y=0,width=680,height=130)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=10,y=135,width=680,height=300)
        
        # Labels and Entry 
        
        # Attendance Id
        attendanceId_label=Label(left_inside_frame,text="Attendance ID: ",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # Roll
        rollLabel=Label(left_inside_frame,text="Roll :",font=("times new roman",12,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        attend_roll=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        attend_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # Name
        nameLabel=Label(left_inside_frame,text="Name : ",font=("times new roman",12,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        attend_name=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        attend_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        # Department 
        depLabel=Label(left_inside_frame,text="Department : ",font=("times new roman",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        attend_dep=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        attend_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        # time 
        timeLabel=Label(left_inside_frame,text="Time : ",font=("times new roman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        attend_time=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        attend_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        # Date 
        dateLabel=Label(left_inside_frame,text="Date : ",font=("times new roman",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        attend_date=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        attend_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        # attendance
        attendanceLable=Label(left_inside_frame,text="Attendance Status: ",font=("times new roman",12,"bold"),bg="white")
        attendanceLable.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        self.attend_status=ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold"),state="read only",width=18)
        self.attend_status["values"]=("Stauts","Present","Absent")
        self.attend_status.grid(row=3,column=1,pady=8)
        self.attend_status.current(0)
        
        # Buttons
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=250,width=650,height=35)
        
        save_btn=Button(btn_frame,text="Import CSV",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export CSV",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------        
         # Right Label frame
        
        Right_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE, text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=700,height=470)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=10,width=680,height=400)
        
        # =============== Scrollbar And  Table ==========================
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        
        # =========================== fetch data ===================
        
        
        
        
        
        
        



if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)  #esme Root bracket ke andar dalna tha lekin kaam nahi kar raha hai root see  no 1 24:21
    root.mainloop()
    # ms.after(0, update, 0)
    # ms.mainloop()