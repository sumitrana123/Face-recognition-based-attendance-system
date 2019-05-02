import tkinter as tk
from tkinter import messagebox
from tkinter import Frame, Canvas, Entry, Label
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
import datetime
import mysql.connector
from mysql.connector import Error



mydb=mysql.connector.connect(host='localhost',database='Face_R',port=3306,user='root',password='sumit47494')
print(mydb)	


window2 = tk.Tk()
window2.geometry("458x610") #You want the size of the app to be 500x500
window2.resizable(0, 0)

					
str1=""
str2=""
str3=""
ids=()
ids1=()
users=()
tex=()
tu=()
x=()

strs=""	

class SignUp_Page:
	def create_Login(self,master):
		
		self.siz=0
		self.id1=()
		self.lis=[]
		self.noti='Maximum character required 8...'
		self.noti_0='User Id Already Exists...'
		self.noti_1='Username Already Exists...'
		self.noti_2='Password Does not Match...'
		self.str=""
		self.res=[]
		self.strr=""
		self.imge1 = ImageTk.PhotoImage(file="Wet.jpg")
		self.imgs = ImageTk.PhotoImage(file="a7.jpg")
		self.val=""
		self.val_0=""
		self.val_1=""
		self.val_2=""
		self.gen=""
		self.framed = Frame(master)
		self.framed.pack()
		self.canves = Canvas(master,width=650,height=700,highlightthickness=-1,bd=-1)
		self.canves.pack()
		self.canves.create_image(50, 50, image=self.imgs)
		self.canves.create_text(65,150,fill="purple",font="Boton 12 bold ",text="User Id")
		self.canves.create_text(72,215,fill="purple",font="Boton 12 bold ",text="Username")
		self.canves.create_text(69,275,fill="purple",font="Boton 12 bold ",text="Password")
		self.canves.create_text(100,332,fill="purple",font="Boton 12 bold ",text="Confirm Password")
		self.canves.create_text(99,392,fill="purple",font="Boton 12 bold ",text="Registration Date")
		self.canves.create_text(56,450,fill="purple",font="Boton 12 bold ",text="D.O.B")
		self.canves.create_text(59,515,fill="purple",font="Boton 12 bold ",text="Gender")
		
		self.cal = DateEntry(window2,fg="purple",bg="powder blue",highlightcolor="white",width=10,cursor="hand1")
		self.cal.place(x=190,y=385)
		self.cal1 = DateEntry(window2,fg="purple",bg="powder blue",highlightcolor="white",width=10,cursor="hand1")
		self.cal1.place(x=190,y=447)
		def check_data():
			try:
				start = "('"
				end = "',)"
				
				query1 = "SELECT id,username,text1 FROM SignUp" 
				print('Done')
			
				cursor= mydb.cursor()
				cursor.execute(query1)
				myresult=cursor.fetchall()
				for self.id1 in myresult:
					self.id1[0]
					
				#ids=tuple(myresult)
				#itu=(ids1,users,tex)
				#for y in ids:
				#	tu=y
				self.lis=myresult	
				
	
				print('Perfect')
		
							
			except Error as err:
				print(err)
		
		check_data()			
	
		def create_data(e):
			self.str=self.cal.get_date()
			str1=self.str
			llb = tk.Label(window2,width=20,height=1,text=str1,bg='white' ,fg="purple"  ,font=('Cordia New', 16, ' bold ') ) 
			llb.place(x=280,y=385)
			return str1

		self.cal.bind("<<DateEntrySelected>>",create_data)
		
		def create_data1(e):
			
			self.strr=self.cal1.get_date()
			str2=self.strr
			self.llb1 = Label(window2,width=20,height=1,text=str2,bg='white' ,fg="purple"  ,font=('Cordia New', 16, ' bold ') ) 
			self.llb1.place(x=280,y=447)
			return str2

		self.cal1.bind("<<DateEntrySelected>>",create_data1)
		
		self.messege = Label(master,bg='white' ,fg="white"  ,width=50) 
		self.messege.place(x=-300, y=10)
	#	passButton = tk.Button(master, fg="white"  ,command=showPass,bg="#FA0122"  ,width=12  ,height=1 ,activebackground = "powder blue" ,font=('Browallia New', 12, ' italic bold '))
	#	passButton.place(x=370, y=500)
		
		#llb = tk.Label(master, text="ID",width=12,height=1,bg='white' ,fg="purple"  ,font=('Cordia New', 16, ' bold ') ) 
		#llb.place(x=80,y=105)
		self.content=tk.StringVar()
		self.tct0 = Entry(master,width=20,bg='white',fg="purple",font=('times', 16, ' bold ')  )
		self.tct0.place(x=190, y=140)
		self.llbp1 = Label(window2,width=30,bg='white' ,fg="red"  ,font=('Cordia New', 12, ' bold ') ) 
		self.llbp1.place(x=193,y=110)
		def callback0(event):
			self.val_0=(self.tct0.get())
			self.rs=[self.rses[0] for self.rses in self.lis]
			
			self.rss=int(self.val_0)
			if self.rss in self.rs:
					
				self.llbp1 = Label(window2,width=30,text=self.noti_0,bg='white' ,fg="red"  ,font=('Cordia New', 12, ' bold ') ) 
				self.llbp1.place(x=193,y=110)
			else:
				self.llbp1.destroy()
			return self.val_0
			
		self.tct0.bind("<FocusOut>", callback0)
		
		self.tct = Entry(master,width=20,bg='white',fg="purple",font=('times', 16, ' bold ')  )
		self.tct.place(x=190, y=200)
		self.llbp3 = Label(window2,width=30,bg='white' ,fg="red"  ,font=('Cordia New', 12, ' bold ') ) 
		self.llbp3.place(x=193,y=171)
		def callback(event):
			self.val=(self.tct.get())
			self.rs1=[self.rses1[1] for self.rses1 in self.lis]
			if self.val in self.rs1:
				self.llbp3 = Label(window2,width=30,text=self.noti_1,bg='white' ,fg="red"  ,font=('Cordia New', 12, ' bold ') ) 
				self.llbp3.place(x=193,y=171)
			else:
				self.llbp3.destroy()
			
			return self.val
		self.tct.bind("<FocusOut>", callback)
		
		
		self.tct1 = Entry(master,width=20,bg='white' ,show='*',fg="purple",font=('times', 16, ' bold ')  )
		self.tct1.place(x=190, y=260)
		self.llbp4 = Label(window2,width=30,bg='white' ,fg="red"  ,font=('Cordia New', 12, ' bold ') ) 
		self.llbp4.place(x=193,y=230)
		
		def callback1(event):
			self.val_1=(self.tct1.get())
			if (len(self.val_1)<8):
				self.llbp4 = Label(window2,width=30,text=self.noti,bg='white' ,fg="red"  ,font=('Cordia New', 12, ' bold ') ) 
				self.llbp4.place(x=193,y=230)
			else:
			    self.llbp4.destroy()
			
			return self.val_1
		self.tct1.bind("<FocusOut>", callback1)

		self.tct2 = Entry(master,width=20,bg='white' ,show='*',fg="purple",font=('times', 16, ' bold ')  )
		self.tct2.place(x=190, y=320)
		self.llbp5 = Label(window2,width=30,bg='white' ,fg="red"  ,font=('Cordia New', 12, ' bold ') ) 
		self.llbp5.place(x=193,y=290)
		def callback2(event):
			self.val_2=(self.tct2.get())
			self.val_1=(self.tct1.get())
			if (self.val_1!=self.val_2):
				self.llbp5 = Label(window2,width=30,text=self.noti_2,bg='white' ,fg="red"  ,font=('Cordia New', 12, ' bold ') ) 
				self.llbp5.place(x=193,y=290)
			else:
			    self.llbp5.destroy()
			
			return self.val_2
		self.tct2.bind("<FocusOut>", callback2)
		self.v1=(self.tct0.get())
		self.v2=(self.tct1.get())
		self.v3=(self.tct2.get())
		self.v4=(self.tct.get())
		def User_Signed(event):
			if self.val!="" and self.val_0!="" and self.val_1!="" and self.val_2!="": 
				window2.destroy()
				import train1
			else:
				messagebox.showinfo("Warning", "Empty Fields ...")
			
		loginButton = tk.Button(master, text="SignIn", fg="white",bg="#FA0122" ,width=12  ,height=1 ,activebackground = "powder blue" ,font=('Browallia New', 12, ' italic bold '))
		loginButton.place(x=360, y=560)
		def insert_data(eve):
	
			try:
	
				query = "INSERT INTO SignUp(id,username,text1,text2,regd,dob,gen) VALUES(%s,%s,%s,%s,%s,%s,%s)"
				print('Done')
				print(self.val_0)
				
				cursor = mydb.cursor()
				args = (self.val_0,self.val,self.val_1,self.val_2,self.str,self.strr,self.gen)
				cursor.execute(query, args)
				mydb.commit()
		
			except Error as err:
				print(err)
		
			finally:
				cursor.close()
				mydb.close()
		
		loginButton.bind("<ButtonPress>", insert_data)
		loginButton.bind("<ButtonRelease>", User_Signed)
		gender = tk.Checkbutton(master, fg="purple",bg="powder blue" ,text='Male',activebackground = "white" ,selectcolor='white',font=('Browallia New', 12, ' italic bold '))
		gender.place(x=190, y=507)
		def changeg(event):
			self.gen="Male"
			print(self.gen)	
			return self.gen
		
		gender.bind("<Button-1>", changeg)
		gender1 = tk.Checkbutton(master, fg="purple",bg="powder blue" ,text='Female',activebackground = "white" ,selectcolor='white',font=('Browallia New', 12, ' italic bold '))
		gender1.place(x=265, y=507)
		def changeg1(event):
			self.gen="Female"
			print(self.gen)	
			return self.gen
		
		gender1.bind("<Button-1>", changeg1)
		self.framed1 = Frame(self.messege,highlightthickness=-1,bd=0)
		self.framed1.pack()
		self.canves1 = Canvas(self.framed1, width=2000, height=50,highlightthickness=-1,bd=-1)
		self.canves1.pack()
		self.canves1.create_image(600, 100, image=self.imge1)
		self.canves1.create_text(525,25,fill="white",font="Boton 22 bold ",text="SignUp Page")
    
ob=SignUp_Page()
ob.create_Login(window2)
window2.mainloop()
val0=ob.val_0
print(val0)
val1=ob.val
print(val1)
val2=ob.val_1
print(val2)
val3=ob.val_2
print(val3)
reg_date=ob.str
print(reg_date)
dob_date=ob.strr
print(dob_date)
gend=ob.gen
print(gend)

