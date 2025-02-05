import cv2
import os
import shutil
import csv
import numpy as np
import pandas as pd
import datetime
import time
from org.jython.book.interfaces import BuildingType

class Building(BuildingType):

	def TakeImages():        #login
		Id=(txt.get())
		name=(txt2.get())
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
			message.configure(text= res)
		else:
			if(is_number(Id)):
				res = "Enter Alphabetical Name"
				message.configure(text= res)
			if(name.isalpha()):
				res = "Enter Numeric Id"
				message.configure(text= res)
		
	def TrainImages():	#after login on database save confirm
		recognizer = cv2.face.LBPHFaceRecognizer_create()  #recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
		harcascadePath = "haarcascade_frontalface_default.xml"
		detector =cv2.CascadeClassifier(harcascadePath)
		faces,Id = getImagesAndLabels("TrainingImage")
		recognizer.train(faces, np.array(Id))
		recognizer.save("TrainingImageLabel\Trainner.yml")
		res = "Image Trained"#+",".join(str(f) for f in Id)
		message.configure(text= res)
	
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

	def TrackImages():	#confirm pic identity
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
		message2.configure(text= res)
	print('ok')