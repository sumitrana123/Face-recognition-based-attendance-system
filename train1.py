# -*- coding: utf-8 -*-
"""
Created on Monday (03-March-2019)

@author: Gaurav Rajpoot
"""


import tkinter as tk
from tkinter import messagebox
from tkinter import Message ,Text,Label,Entry,Button
import cv2
import os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
from tkinter import Frame, Canvas
import tkinter.ttk as ttk
import tkinter.font as font
from tkcalendar import Calendar, DateEntry
import datetime
import mysql.connector
from mysql.connector import Error

		

window1= tk.Tk()
window1.geometry("500x300") #You want the size of the app to be 500x500
window1.resizable(0, 0)

photoimage3 = ImageTk.PhotoImage(file="Wet.jpg")
photoimage4 = ImageTk.PhotoImage(file="Home.png")
def callback(event):
	window1.destroy()
	from new2 import SignUp_Page

mydb1=mysql.connector.connect(host='localhost',database='Face_R',port=3306,user='root',password='sumit47494')
print(mydb1)	

	
		
class Face:
	
		
	def open_Face(self,master):
		#self.master=master
		#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
		#answer = messagebox.askquestion(dialog_title, dialog_text)
		#self.photoimage = photoimage
		#self.photoimage1 = photoimage1
		#self.photoimage2 = photoimage2
		


		self.img = ImageTk.PhotoImage(file="wave-flow.png")
		self.img1 = ImageTk.PhotoImage(file="asdd.jpg")
		self.img2 = ImageTk.PhotoImage(file="a7.jpg")
	
		self.frames = Frame(master)
		self.frames.pack()
		self.canvass = Canvas(self.frames, width=1920, height=1080)
		self.canvass.pack()

		self.canvass.create_image(620, 300 ,image=self.img)
		self.canvass.create_text(432,245,fill="purple",font="Boton 20  bold ",text="Enter ID")
		self.canvass.create_text(450,322,fill="purple",font="Boton 20  bold ",text="Enter Name")
		self.canvass.create_text(450,425,fill="purple",font="Boton 20  bold ",text="Notification")
		self.canvass.create_text(450,575,fill="purple",font="Boton 20  bold ",text="Attendance")

		master.grid_rowconfigure(0, weight=0)
		master.grid_columnconfigure(0, weight=0)

		self.messages = Label(master,bg='white' ,fg="white"  ,width=100 ) 
		self.messages.place(x=-300, y=10)

		self.frames1 = Frame(self.messages,highlightthickness=-1,bd=0)
		self.frames1.pack()

		self.canvass1 = Canvas(self.frames1, width=2000, height=80,highlightthickness=-1,bd=-1)
		self.canvass1.pack()
		self.canvass1.create_image(980, 250,image=self.img1)
		self.canvass1.create_text(1000,45,fill="#01CBB5",font="Boton 32  bold ",text="REALTIME FACE ATTENDANCE")

		self.txts = Entry(master,width=20,bg='white' ,fg="purple",font=('times', 15, ' bold ')  )
		self.txts.place(x=550, y=230)

		self.txts2 = Entry(master,width=20,bg='white' ,fg="purple",font=('times', 15, ' bold ')  )
		self.txts2.place(x=550 , y=310)

		self.messagess = Label(master, text=" " ,width=40,bg="#01CBB5" ,fg="white", activebackground = "#01CBB5" ,font=('Cordia New', 26, ' bold ')) 
		self.messagess.place(x=550,y=400)

		self.messagess2 = Label(master, text="" ,width=45,bg="#01CBB5" ,fg="white",activeforeground = "#01CBB5"  ,font=('Cordia New', 26, ' bold ')) 
		self.messagess2.place(x=550, y=550)
		
		self.boxs = Label(master, fg="white"  ,width=500  ,height=33) 
		self.boxs.place(x=20, y=180)
		self.framess2 = Frame(self.boxs, width=250, height=430,highlightthickness=0,bd=0)
		self.framess2.pack(side = 'left', fill='both')

		self.canvasss2 = Canvas(self.framess2, width=250, height=500,highlightthickness=0,bd=0)
		self.canvasss2.pack()
		self.canvasss2.create_image(500, 270,image=self.img2)
		
		def clear():
			self.txts.delete(0, 'end')    
			res = ""
			self.messagess.configure(text= res)
		
		def clear1():
			self.txts2.delete(0, 'end')    
			res = ""
			self.messagess.configure(text= res)
		self.clearButton = Button(self.framess2, text="Clear ID", command=clear  ,fg="white"  ,bg="#01CBB5"  ,width=18  ,height=1 ,activebackground = "powder blue" ,font=('Browallia New', 18, ' italic bold '))
		self.clearButton.place(x=30, y=270)
		self.clearButton = Button(self.framess2, text="Clear Name", command=clear1  ,fg="white"  ,bg="#01CBB5"  ,width=18  ,height=1 ,activebackground = "powder blue" ,font=('Browallia New', 18, ' italic bold '))
		self.clearButton.place(x=30, y=350)
		def is_number(s):
			try:
				float(s)
				return True
			except ValueError:
				pass
 
			try:
				import unicodedata
				unicodedata.numeric(s)
				return True
			except (TypeError, ValueError):
				pass
	
			return False
	
    
		def TakeImages():        
			Id=(self.txts.get())
			name=(self.txts2.get())
			if(is_number(Id) and name.isalpha()):
				cam = cv2.VideoCapture(0)
				harcascadePath = 'haarcascade_frontalface_default.xml'
				detector=cv2.CascadeClassifier(harcascadePath)
				sampleNum=0
				while 1:
					ret, img = cam.read()
					gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
					faces = detector.detectMultiScale(gray, 1.3, 5)
					for (x,y,w,h) in faces:
						cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
						#incrementing sample number 
						sampleNum=sampleNum+1
						#saving the captured face in the dataset folder TrainingImage
						cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w] )
					
						#display the frame
						cv2.imshow('img',img)
					#wait for 100 miliseconds 
					if cv2.waitKey(100) & 0xFF == ord('q'):
						break
					# break if the sample number is morethan 100
					elif sampleNum>60:
						break
				cam.release()
				cv2.destroyAllWindows() 
				res = "Images Saved for ID : " + Id +" Name : "+ name
				row = [Id , name]
				with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
					writer = csv.writer(csvFile)
					writer.writerow(row)
				csvFile.close()
				self.messagess.configure(text= res)
			else:
				if(is_number(Id)):
					res = "Enter Alphabetical Name"
					self.messagess.configure(text= res)
				if(name.isalpha()):
					res = "Enter Numeric Id"
					self.messagess.configure(text= res)
		
		self.takeImg = Button(self.framess2, text="Take Images", command=TakeImages  ,fg="white"  ,bg="#01CBB5"  ,width=18  ,height=1, activebackground = "powder blue" ,font=('Browallia New', 18, ' italic bold '))
		self.takeImg.place(x=30, y=30)


		def getImagesAndLabels(path):
			#get the path of all the files in the folder
			imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
			#print(imagePaths)
		
			#create empty face list
			faces=[]
			#create empty ID list
			Ids=[]
			#now looping through all the image paths and loading the Ids and the images
			for imagePath in imagePaths:
				#loading the image and converting it to gray scale
				pilImage=Image.open(imagePath).convert('L')
				#Now we are converting the PIL image into numpy array
				imageNp=np.array(pilImage,'uint8')
				#getting the Id from the image
				Id=int(os.path.split(imagePath)[-1].split(".")[1])
				# extract the face from the training image sample
				faces.append(imageNp)
				Ids.append(Id)        
			return faces,Ids
	
		def TrainImages():
			recognizer = cv2.face.LBPHFaceRecognizer_create()  #recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
			harcascadePath = "haarcascade_frontalface_default.xml"
			detector =cv2.CascadeClassifier(harcascadePath)
			faces,Id = getImagesAndLabels("TrainingImage")
			recognizer.train(faces, np.array(Id))
			recognizer.save("TrainingImageLabel\Trainner.yml")
			res = "Image Trained"#+",".join(str(f) for f in Id)
			self.messagess.configure(text= res)
	
		self.trainImg = Button(self.framess2, text="Train Images", command=TrainImages  ,fg="white"  ,bg="#01CBB5"  ,width=18  ,height=1, activebackground = "powder blue" ,font=('Browallia New', 18, ' italic bold '))
		self.trainImg.place(x=30, y=110)
		def TrackImages():
			recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
			recognizer.read("TrainingImageLabel\Trainner.yml")
			harcascadePath = "haarcascade_frontalface_default.xml"
			faceCascade = cv2.CascadeClassifier(harcascadePath);    
			df=pd.read_csv("StudentDetails\StudentDetails.csv")
			cam = cv2.VideoCapture(0)
			font = cv2.FONT_HERSHEY_SIMPLEX        
			col_names =  ['Id','Name','Date','Time']
			attendance = pd.DataFrame(columns = col_names)    
			while True:
				ret, im =cam.read()
				gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
				faces=faceCascade.detectMultiScale(gray, 1.2,5)    
				for(x,y,w,h) in faces:
					cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
					Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
					if(conf < 50):
						ts = time.time()      
						date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
						timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
						aa=df.loc[df['Id'] == Id]['Name'].values
						tt=str(Id)+"-"+aa
						attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
					else:
						Id='Unknown'                
						tt=str(Id)  
					if(conf > 75):
						noOfFile=len(os.listdir("ImagesUnknown"))+1
						cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
					cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
				attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
				cv2.imshow('im',im) 
				if (cv2.waitKey(1)==ord('q')):
					break
			ts = time.time()      
			date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
			timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
			Hour,Minute,Second=timeStamp.split(":")
			fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
			attendance.to_csv(fileName,index=False)
			cam.release()
			cv2.destroyAllWindows()
			#print(attendance)
			res=attendance
			self.messagess2.configure(text= res)
	
		self.trackImg = Button(self.framess2, text="Track Images", command=TrackImages  ,fg="white"  ,bg="#01CBB5"  ,width=18  ,height=1, activebackground = "powder blue" ,font=('Browallia New', 18, ' italic bold '))
		self.trackImg.place(x=30, y=190)
		self.quitWindow = Button(self.framess2, text="Quit", command=master.destroy  ,fg="white"  ,bg="#01CBB5"  ,width=18  ,height=1, activebackground = "powder blue" ,font=('Browallia New', 18, ' italic bold '))
		self.quitWindow.place(x=30, y=430)
		self.copyWrite = Text(master, background=master.cget("background"), borderwidth=1,font=('Browallia New', 22, ' italic bold '))
		self.copyWrite.tag_configure("superscript", offset=10)
		self.copyWrite.insert("insert", "Developed by Gaurav","", "TEAM", "superscript")
		self.copyWrite.configure(state="disabled",fg="red"  )
		self.copyWrite.pack(side="left")
		self.copyWrite.place(x=800, y=750)



	
	
class Login_Page(Face):
	
		
	def __init__(self,master1):
		self.val_12=""
		self.val_13=""
		self.val_14=""
		
		self.frame = Frame(master1)
		self.frame.pack()
		self.canvas = Canvas(master1,width=650,height=300,highlightthickness=-1,bd=-1)
		self.canvas.pack()
		self.canvas.create_image(50, 50, image=photoimage4)
		# ******HyperLink** #
		self.canvas.create_text(103,118,fill="purple",font="Boton 12 bold  ",text="User ID")
		self.canvas.create_text(110,160,fill="purple",font="Boton 12 bold  ",text="Username")
		self.canvas.create_text(110,205,fill="purple",font="Boton 12 bold  ",text="Password")
		self.message = tk.Label(master1,bg='white' ,fg="white"  ,width=50) 
		self.message.place(x=-300, y=10)
		#lbl = tk.Label(master1, text="ID",width=12,height=1,bg='white' ,fg="purple"  ,font=('Cordia New', 16, ' bold ') ) 
		#lbl.place(x=80,y=105)
		self.txt = Entry(master1,width=25,bg='white' ,fg="purple",font=('times', 16, ' bold ')  )
		self.txt.place(x=185, y=106)
		def callback3(event):
			self.val_12=(self.txt.get())
			print(self.val_12)	
			return self.val_12
		self.txt.bind("<FocusOut>", callback3)
		
		  
		lbl = tk.Label(master1, text="Not Registered...?",width=20,height=1,bg='white' ,fg="blue"  ,font=('Cordia New', 12, ' bold italic underline ') ) 
		lbl.place(x=235,y=243)
		lbl.bind("<Button-1>", callback)
		self.txtp = Entry(master1,width=25,bg='white' ,fg="purple",font=('times', 16, ' bold ')  )
		self.txtp.place(x=185, y=148)
		def callback4(event):
			self.val_13=(self.txtp.get())
			print(self.val_13)	
			return self.val_13
		self.txtp.bind("<FocusOut>", callback4)
		
		self.txtpp = Entry(master1,width=25,bg='white',show='*',fg="purple",font=('times', 16, ' bold ')  )
		self.txtpp.place(x=185, y=191)
		self.comp=""
		def callback5(event):
			self.val_14=(self.txtpp.get())
			print(self.val_14)	
			return self.val_14
		self.txtpp.bind("<FocusOut>", callback5)
		
        
		
		#lbl = tk.Label(master1, text="Password",width=12,height=1,bg='white' ,fg="purple"  ,font=('Cordia New', 16, ' bold ') ) 
		#lbl.place(x=80,y=190)
		loginButton = tk.Button(master1, text="Login", fg="white"   ,bg="#FA0122"  ,width=12  ,height=1 ,activebackground = "powder blue" ,font=('Browallia New', 12, ' italic bold '))
		loginButton.place(x=370, y=240)
		
		def buttonClick(ev):
			if self.txt!=None and self.txtp!=None and self.txtpp!=None : 
				window1.destroy()
				win=tk.Tk()
				win.title("Face Enabled Attendace System")
				dialog_title = 'QUIT'
				dialog_text = 'Are you sure?'
				ob2=Face()
				ob2.open_Face(win)
				win.mainloop()	
			else:
				messagebox.showinfo("Warning", "Empty Fields ...")
		
		
		def check_data(event):
			try:
				start = "('"
				end = "',)"
				
				query1 = "SELECT text1 FROM SignUp WHERE id = %s" 
				print('Done')
				
				cursor= mydb1.cursor()
				args1 = (self.val_12,)
				cursor.execute(query1, args1)
				myresult=cursor.fetchall()
				for x in myresult:
					self.comp=x[0]
		
				
				print('Perfect')
				print(self.comp)
				
							
			except Error as err:
				print(err)
										
		loginButton.bind('<ButtonPress>',check_data)
		loginButton.bind('<ButtonRelease>',buttonClick)
			
		self.frame1 = Frame(self.message,highlightthickness=-1,bd=0)
		self.frame1.pack()
		self.canvas1 = Canvas(self.frame1, width=2000, height=50,highlightthickness=-1,bd=-1)
		self.canvas1.pack()
		self.canvas1.create_image(600, 100, image=photoimage3)
		self.canvas1.create_text(550,25,fill="white",font="Boton 22 bold ",text="LOGIN")
		
ob=Login_Page(window1)
window1.mainloop()
vall=ob.val_12
tex1=ob.val_14


