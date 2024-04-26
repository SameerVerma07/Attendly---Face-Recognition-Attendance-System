from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
# from main import Face_Recognition_System




class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendly- Face Recognition Attendance System")
        
        
        # ======variables=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        # face image 1
        img1=Image.open(r"college_images\student.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        # face image 2
        img2=Image.open(r"college_images\Attendly2.0.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=520,height=130)
        
        # face image 3
        img3=Image.open(r"college_images\Face_attendance 01.jpg")
        img3=img3.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1025,y=0,width=520,height=130)
        
        # background image
        img4=Image.open(r"college_images\bg1.jpg")
        img4=img4.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Button(bg_img,text="Student Mangagement System",font=("times new roman",35,"bold"),bg="black",fg="White")
        title_lbl.place(x=0,y=0,width=1530,height=55)
        
        main_frame=Frame(bg_img,bd=2, bg="white")
        main_frame.place(x=10,y=65,width=1500,height=600)
        
 # --*-*-*-**-*-*-*-*-*-*-**--*-**-**-**-*-**-----------------------------------------------------------------------------
 # --*-*-*-**-*-*-*-*-*-*-**--*-**-**-**-*-**-----------------------------------------------------------------------------
 # --*-*-*-**-*-*-*-*-*-*-**--*-**-**-**-*-**-----------------------------------------------------------------------------

        # left Label frame
        
        Left_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE, text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=30,y=10,width=700,height=580)
        
        img_left1=Image.open(r"college_images\Face_attendance 01.jpg")
        img_left1=img_left1.resize((680,130),Image.Resampling.LANCZOS)
        self.photoimg_left1=ImageTk.PhotoImage(img_left1)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left1)
        f_lbl.place(x=5,y=0,width=680,height=130)
        
# -------Current Course-------------------------------------------------------------------- 
        CC_frame=LabelFrame(Left_frame,bd=2, bg="white",relief=RIDGE, text="Current Course Details",font=("times new roman",12,"bold"))
        CC_frame.place(x=5,y=135,width=680,height=120)
        
        # Department
        dep_label=Label(CC_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(CC_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","Computer Science","IT","BBA","LLB","Agriculture","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        
        # Course
        
        course_label=Label(CC_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(CC_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only",width=20)
        course_combo["values"]=("Select Course","BE","TE","FE","SE","Agriculture","Civil")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        
        # Year
        
        year_label=Label(CC_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(CC_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only",width=20)
        year_combo["values"]=("Select Year","2023-2024","2022-2023","2021-2022","2020-2021","2019-2020","2018-2019")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)
        
        # semester
        
        semester_label=Label(CC_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(CC_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="read only",width=20)
        semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W)
        
# ------Class Student Information (CS)----------------------------------------------------------------------------------
        
        CS_frame=LabelFrame(Left_frame,bd=2, bg="white",relief=RIDGE, text="Class Student Information",font=("times new roman",12,"bold"))
        CS_frame.place(x=5,y=255,width=680,height=300)
        
        # Student Id
        studentid_label=Label(CS_frame,text="Student ID: ",font=("times new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentid_entry=ttk.Entry(CS_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # Student Name
        
        studentName_label=Label(CS_frame,text="Student Name: ",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(CS_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # Class Division
        
        division_label=Label(CS_frame,text="Class Division: ",font=("times new roman",12,"bold"),bg="white")
        division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        # division_entry=ttk.Entry(CS_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        # division_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(CS_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=18)
        div_combo["values"]=("Select Divsion","A","B","C","D","E","F")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        # Roll No or Enrollment no
        
        roll_label=Label(CS_frame,text="Roll No: ",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_entry=ttk.Entry(CS_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        # Gender
        
        gender_label=Label(CS_frame,text="Gender: ",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        # gender_entry=ttk.Entry(CS_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(CS_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=18)
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        # DOB 
        
        DOB_label=Label(CS_frame,text="DOB: ",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        DOB_entry=ttk.Entry(CS_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #  Email
        
        email_label=Label(CS_frame,text="Email ID: ",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(CS_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        # Phone Numbers /contact details
        
        phone_label=Label(CS_frame,text="Phone No: ",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(CS_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        
        # adress Details
        
        adress_label=Label(CS_frame,text="Address : ",font=("times new roman",12,"bold"),bg="white")
        adress_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        adress_entry=ttk.Entry(CS_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        adress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        # Teacher Name
        
        teacher_label=Label(CS_frame,text="Teacher Name: ",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(CS_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        # radio buttons
        self.var_radio1=StringVar()
        radioBt1=ttk.Radiobutton(CS_frame,variable=self.var_radio1,text="Take A Photos Sample",value="Yes")
        radioBt1.grid(row=6,column=0)
        
       
        radioBt2=ttk.Radiobutton(CS_frame,variable=self.var_radio1,text="No Photos Sample",value="NO")
        radioBt2.grid(row=6,column=1)
        
# ------- Buttons Frame -----------------------------------------------------------------        
        btn_frame=Frame(CS_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=200,width=650,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
    
# -------update and take photos buttoms    
        
        btn_frame1=Frame(CS_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=240,width=650,height=35)
        
        TakePhotos_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",12,"bold"),bg="magenta",fg="black")
        TakePhotos_btn.grid(row=0,column=0)
        
        UpadtePhotos_btn=Button(btn_frame1,text="Upadte Photo Sample",width=35,font=("times new roman",12,"bold"),bg="magenta",fg="black")
        UpadtePhotos_btn.grid(row=0,column=1)
        

        
        
# --*-*-*-**-*-*-*-*-*-*-**--*-**-**-**-*-**-----------------------------------------------------------------------------
# --*-*-*-**-*-*-*-*-*-*-**--*-**-**-**-*-**-----------------------------------------------------------------------------
 # --*-*-*-**-*-*-*-*-*-*-**--*-**-**-**-*-**-----------------------------------------------------------------------------
       
        # Right Label frame
        
        Right_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE, text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=700,height=580)
        
        img_Right1=Image.open(r"college_images\Right.jpg")
        img_Right1=img_Right1.resize((680,130),Image.Resampling.LANCZOS)
        self.photoimg_Right1=ImageTk.PhotoImage(img_Right1)
        
        f_lbl=Label(Right_frame,image=self.photoimg_Right1)
        f_lbl.place(x=5,y=0,width=680,height=130)
        
        # =========== Search system =========================================================================
        
        search_frame=LabelFrame(Right_frame,bd=2, bg="white",relief=RIDGE, text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=680,height=70)
        
        search_label=Label(search_frame,text="Search By",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="read only",width=15)
        search_combo["values"]=("Select ","Roll No","Admission no","Phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        
        phone_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        phone_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showall_btn=Button(search_frame,text="Showall",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)
        
# ======== table frame =========================
        table_frame=Frame(Right_frame,bd=2, bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=680,height=250)
        
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
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.pack(fill=BOTH,expand=1)
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
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        # =======function declaration======================
    def add_data(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields Are Required",parent=self.root)
            else:
                try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Sameerverma@121",database="face_recognition")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        
                
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        # self.var_year.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get()
                                                                                                                        
                                                                                                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","Student Details Has Been Added Successfully",parent=self.root)
                except Exception as es:
                        messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
#     ======fetch data =============================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sameerverma@121",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                        self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()
        
#     ========get Cursor============
    def get_cursor(self,event=""):
            cursor_focus=self.student_table.focus()
            content=self.student_table.item(cursor_focus)
            data=content["values"]
            
            self.var_dep.set(data[0]),
            self.var_course.set(data[1]),
            self.var_year.set(data[2]),
            self.var_semester.set(data[3]),
            self.var_std_id.set(data[4]),
            self.var_std_name.set(data[5]),
            self.var_div.set(data[6]),
            self.var_roll.set(data[7]),
            self.var_gender.set(data[8]),
            self.var_dob.set(data[9]),
            self.var_email.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_address.set(data[12]),
            self.var_teacher.set(data[13]),
            self.var_radio1.set(data[14])
                    
#   ==================update data ===========================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you Want to Update the Student Details ?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sameerverma@121",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s,Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s ",(

                                                                                                                                                                                                                       self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        # self.var_year.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get(),
                                                                                                        self.var_std_id.get(),     
                    ))
                
                else:
                    if not Update:
                            return
                messagebox.showinfo("Success","Student Details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()    
            except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                    
    # ======== Delete Function=========================
    
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do You Want to Delete the Student Data?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Sameerverma@121", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                messagebox.showinfo("Delete", "Successfully Deleted student details", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)


# ===================reset data===========
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
    # ====== Generate data set or take photo sample===============                            
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sameerverma@121",
                                            database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1

                my_cursor.execute(
                    "update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s,Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s ",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() == id + 1  # Corrected this line
                    ))
                conn.commit()  # Corrected this line
                
                self.fetch_data()
                # k=self.var_std_id
                self.reset_data()
                conn.close()

                # =====loading predefine data from frontals form open cv=========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Crooped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set Completed",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)
                
            
            
        
        
# # ================================ going Back to the main Window============================   
#     def Main_Window(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Face_Recognition_System(self.new_window)

                  
                
        
                            

        
        
        
        





if __name__ == "__main__":
    root=Tk()
    obj=student(root)  #esme Root bracket ke andar dalna tha lekin kaam nahi kar raha hai root see  no 1 24:21
    root.mainloop()
    # ms.after(0, update, 0)
    # ms.mainloop()