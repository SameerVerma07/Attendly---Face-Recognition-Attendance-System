from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendly- Face Recognition Attendance System")
        
        # face image 1
        img1=Image.open(r"college_images\Face_attendance 01.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        # face image 2
        img2=Image.open(r"college_images\Attendly2.0.jpg")
        # img2=Image.open(r"E:\FaceAttendance System\college_images\sachin.png")
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
        
        title_lbl=Label(bg_img,text="Attendly- Face Recognition Attendance System",font=("times new roman",35,"bold"),bg="white",fg="black")
        # title_lbl=Label(bg_img,text="AttendFace - Automatic Face recogniation Based Attendance",font=("times new roman",35,"bold"),bg="white",fg="black")

        title_lbl.place(x=0,y=0,width=1530,height=55)

#-------------------------------------------------------------------------------------------------------------    
        
# -----------------------------------------------------------------------------------------------------------
        
    # Students Details
        img10=Image.open(r"college_images\details.gif")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
    
        
        b1=Button(bg_img,image=self.photoimg10, cursor="hand2",command = self.student_details)
        b1.place(x=250,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details", command=self.student_details,cursor="hand2",font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=250,y=320,width=220,height=30)
# -----------------------------------------------------------------------------------------------    
    # 
    # Face Detector
        img11=Image.open(r"college_images\FaceDEtector.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
    
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.face_data)
        b1.place(x=550,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=550,y=320,width=220,height=30)
        
        
# ----------------------------------------------------------------------------------------
# Attendance 
        img12=Image.open(r"college_images\attend.jpg")
        img12=img12.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)
    
        
        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.attendance_data)
        b1.place(x=850,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=850,y=320,width=220,height=30)
        
# ----------------------------------------------------------------------------------------
# Help Desk 
        img13=Image.open(r"college_images\Help.jpg")
        img13=img13.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg13=ImageTk.PhotoImage(img13)
    
        b1=Button(bg_img,image=self.photoimg13,cursor="hand2")
        b1.place(x=1150,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1150,y=320,width=220,height=30)        


# ----------------------------------------------------------------------------------------
        
    # Train Data
        img14=Image.open(r"college_images\traindata.jpg")
        img14=img14.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg14=ImageTk.PhotoImage(img14)
    
        
        b1=Button(bg_img,image=self.photoimg14,cursor="hand2",command=self.training_data)
        b1.place(x=250,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.training_data,font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=250,y=580,width=220,height=30)
        
# ----------------------------------------------------------------------------------------
        
    # Photos
        img15=Image.open(r"college_images\photos.jpg")
        img15=img15.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg15=ImageTk.PhotoImage(img15)
    
        
        b1=Button(bg_img,image=self.photoimg15,cursor="hand2",command=self.open_img)
        b1.place(x=550,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=550,y=580,width=220,height=30)
        
# ----------------------------------------------------------------------------------------
        
    # Developer
        img16=Image.open(r"college_images\Developer.jpg")
        img16=img16.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg16=ImageTk.PhotoImage(img16)
    
        
        b1=Button(bg_img,image=self.photoimg16,cursor="hand2")
        b1.place(x=850,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=850,y=580,width=220,height=30)
        
# ----------------------------------------------------------------------------------------
        
    # Exitṇ
        img17=Image.open(r"college_images\exit.jpg")
        img17=img17.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg17=ImageTk.PhotoImage(img17)
    
        
        b1=Button(bg_img,image=self.photoimg17,cursor="hand2")
        b1.place(x=1150,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1150,y=580,width=220,height=30)
        
    def open_img(self):
        os.startfile("data")
        
        
        
        
# ================== Function Buttons ========================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
        
    def training_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
        
         
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)  #esme Root bracket ke andar dalna tha lekin kaam nahi kar raha hai root see  no 1 24:21
    root.mainloop()
    # ms.after(0, update, 0)
    # ms.mainloop()
    