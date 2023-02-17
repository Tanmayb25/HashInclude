from tkinter import *
import pandas as pd
import time
from tkinter import messagebox
import re
from datetime import date
from plyer import notification
import random

import matplotlib.pyplot as plt





def showNotif(message) :
    notification.notify(
            title = "Alert!",
            message=message ,
           
            # displaying time
            timeout=7
)


def plotGraph():
    global graphData
    graphData.plot(x="Time", y=["MentalIndex", "PhysicalIndex"], kind="line")
    print(graphData)
    plt.show()


graphData = pd.DataFrame({
    'Time': [],
    'PhysicalIndex': [],
    'MentalIndex':[]
})


exerData={'Physical': ['Take a walk for 5 minutes','Cobra stretch for your back','Stretch your neck towards left and then right','blinking quickly 20 times, and then close your eyes for three deep breaths'],
      'Mental':['Place your palms on your eyes and meditate for 2 mins','Meditate for 2 minutes','Try equal breathing for 5 minutes','Listen to calm music']}

exerDf=pd.DataFrame(exerData)


'''meetings1 = {'Title': ['Meeting1', 'Meeting2', 'Meeting3'],
             'sTime': ['1830', '1940','0800'],
             'eTime': ['1900', '2000','0830'],
             'Date':['17-02-23', '18-02-23', '19-02-23']}


df1 = pd.DataFrame(meetings1)'''

curr_time = time.strftime("%H:%M:%S", time.localtime())
curr_date = date.today()

phyIndex = 99
menIndex = 99



list_of_events = [{'kind': 'calendar#event',
  'etag': '"3353215715256000"',
  'id': '6ks34c1gc4qm6b9gcgpjcb9k6spm6bb2ckom8b9mc9i3ae1mcgpjapj468',
  'status': 'confirmed',
  'htmlLink': 'https://www.google.com/calendar/event?eid=NmtzMzRjMWdjNHFtNmI5Z2NncGpjYjlrNnNwbTZiYjJja29tOGI5bWM5aTNhZTFtY2dwamFwajQ2OCBzdW1pdG11bGUyMjJAbQ',
  'created': '2023-02-17T03:51:29.000Z',
  'updated': '2023-02-17T04:24:17.628Z',
  'summary': 'meeting 1',
  'creator': {'email': 'sumitmule222@gmail.com', 'self': True},
  'organizer': {'email': 'sumitmule222@gmail.com', 'self': True},
  'start': {'dateTime': '2023-02-17T15:30:00+05:30',
   'timeZone': 'Asia/Kolkata'},
  'end': {'dateTime': '2023-02-17T12:26:00+05:30', 'timeZone': 'Asia/Kolkata'},
  'iCalUID': '6ks34c1gc4qm6b9gcgpjcb9k6spm6bb2ckom8b9mc9i3ae1mcgpjapj468@google.com',
  'sequence': 0,
  'reminders': {'useDefault': True},
  'eventType': 'default'},
 {'kind': 'calendar#event',
  'etag': '"3353215716612000"',
  'id': 'c5j34d31ccojabb1clj6cb9k71i3gb9o74q68b9hcli30c1gc8r32cb464',
  'status': 'confirmed',
  'htmlLink': 'https://www.google.com/calendar/event?eid=YzVqMzRkMzFjY29qYWJiMWNsajZjYjlrNzFpM2diOW83NHE2OGI5aGNsaTMwYzFnYzhyMzJjYjQ2NCBzdW1pdG11bGUyMjJAbQ',
  'created': '2023-02-17T04:24:18.000Z',
  'updated': '2023-02-17T04:24:18.306Z',
  'summary': 'meeting on 18',
  'creator': {'email': 'sumitmule222@gmail.com', 'self': True},
  'organizer': {'email': 'sumitmule222@gmail.com', 'self': True},
  'start': {'dateTime': '2023-02-18T16:30:00+05:30',
   'timeZone': 'Asia/Kolkata'},
  'end': {'dateTime': '2023-02-18T17:30:00+05:30', 'timeZone': 'Asia/Kolkata'},
  'iCalUID': 'c5j34d31ccojabb1clj6cb9k71i3gb9o74q68b9hcli30c1gc8r32cb464@google.com',
  'sequence': 0,
  'reminders': {'useDefault': True},
  'eventType': 'default'}]

event_details = {'Title' :[],'sTime' :[],'eTime' :[],'Date' :[]}
for items in list_of_events:
  #front
  event_details['Title'].append(items['summary'])

  date = re.split('T',items['start']['dateTime'])
  event_details['Date'].append(date[0])

  arr1 = re.split('T',items['start']['dateTime'])
  sTime = arr1[1].split('+')[0]
  event_details['sTime'].append(sTime)

  arr2 = re.split('T',items['end']['dateTime'])
  eTime = arr2[1].split('+')[0]
  event_details['eTime'].append(eTime)


df2 = pd.DataFrame(event_details)
df1 = df2.sort_values(by=['sTime'],ascending=True)
print(df1)


'''from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from google_auth_oauthlib.flow import Flow
import re
from datetime import date
import pandas as pd
import re

flow = Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=["https://www.googleapis.com/auth/calendar"],
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')

# Tell the user to go to the authorization URL.
auth_url, _ = flow.authorization_url(prompt='consent')

print('Please go to this URL: {}'.format(auth_url))

# The user will get an authorization code. This code is used to get the
# access token.
code = input('Enter the authorization code: ')
credentials = flow.fetch_token(code=code)

pickle.dump(credentials, open('token.pkl','wb'))
credentials = pickle.load(open('token.pkl','rb'))
service = build('calendar','v3',credentials=flow.credentials)
result = service.calendarList().list().execute()
calendar_id = result['items'][3]['id']

today = date.today()
timeCondmin = str(today) + 'T00:00:00+05:30'
timeCondmax = str(today) + 'T23:00:00+05:30'
events = service.events().list(calendarId=calendar_id,timeMin=timeCondmin,timeMax=timeCondmax).execute()

list_of_events = events['items']
#print(result)

event_details = {'Title' :[],'sTime' :[],'eTime' :[],'Date' :[]}
for items in list_of_events:
  #front
  event_details['Title'].append(items['summary'])

  date = re.split('T',items['start']['dateTime'])
  event_details['Date'].append(date[0])

  arr1 = re.split('T',items['start']['dateTime'])
  sTime = arr1[1].split('+')[0]
  event_details['sTime'].append(sTime)

  arr2 = re.split('T',items['end']['dateTime'])
  eTime = arr2[1].split('+')[0]
  event_details['eTime'].append(eTime)


df2 = pd.DataFrame(event_details)


df1 = df2.sort_values(by=['sTime'],ascending=True)
print(df1)'''


window = Tk()
window.geometry("420x520")
window.title("HealthApp")
window.config(background="#000000")

titleText = Label (window, text = "Health App" , font=('Arial', 40, 'bold'), fg='#FFFFFF', bg='#000000')
titleText.place(x=70, y=45)

meetingsText = Label (window, text="Meetings", font=('Arial', 20, 'bold'), fg='#FFFFFF', bg='#000000')
meetingsText.place(x=60, y=135)

tempY=180
for ind in df1.index:
    #print(df1['Title'][ind], df['Time'][ind], df['Date'][ind])
    tempTitle=Label(window, text = df1['Title'][ind],font=('Arial', 10, 'bold'), fg='#FFFFFF', bg='#000000')
    tempTitle.place(x=60, y=tempY)
                    
    tempDate=Label(window, text = df1['Date'][ind],font=('Arial', 10, 'bold'), fg='#FFFFFF', bg='#000000')
    tempDate.place(x=130, y=tempY)
                   
    tempsTime=Label(window, text = df1['sTime'][ind],font=('Arial', 10, 'bold'), fg='#FFFFFF', bg='#000000')
    tempsTime.place(x=200, y=tempY)
    
    tempY=tempY+30

waterTitle = Label(window, text = "Water Intake" , font=('Arial', 16, 'bold'), fg='#FFFFFF', bg='#000000')
waterTitle.place(x=30, y=tempY+70)

waterInLabel=Label (window, text = "6L" , font=('Arial', 20, 'bold'), fg='#FFFFFF', bg='#000000')
waterInLabel.place(x=30, y=tempY+100)

waterRemLabel=Label (window, text = "Remaining: 1L" , font=('Arial', 10, 'bold'), fg='#FFFFFF', bg='#000000')
waterRemLabel.place(x=30, y=tempY+130)

statsButton = Button(window, text="show stats", command=plotGraph)
statsButton.place(x=30, y=tempY+150)


'''walkTitle = Label(window, text = "Steps" , font=('Arial', 16, 'bold'), fg='#FFFFFF', bg='#000000')
walkTitle.place(x=30, y=tempY+170)

walkInLabel=Label (window, text = "4098" , font=('Arial', 20, 'bold'), fg='#FFFFFF', bg='#000000')
walkInLabel.place(x=30, y=tempY+200)

walkRemLabel=Label (window, text = "3456" , font=('Arial', 10, 'bold'), fg='#FFFFFF', bg='#000000')
walkRemLabel.place(x=30, y=tempY+230)'''



phyTitle=Label (window, text = "Physical Index" , font=('Arial', 15, 'bold'), fg='#FFFFFF', bg='#000000')
phyTitle.place(x=250, y=tempY+40)

'''phyInLabel=Label (window, text = i , font=('Arial', 20, 'bold'), fg='#FFFFFF', bg='#000000')
phyInLabel.place(x=300, y=tempY+70)'''

menTitle=Label (window, text = "Mental Index" , font=('Arial', 15, 'bold'), fg='#FFFFFF', bg='#000000')
menTitle.place(x=250, y=tempY+110)

'''menInLabel=Label (window, text = "45" , font=('Arial', 20, 'bold'), fg='#FFFFFF', bg='#000000')
menInLabel.place(x=300, y=tempY+140)'''



'''t=10;
while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1
      
messagebox.showinfo("reminder", "WHY ARE YOU GAY")'''






import cv2
import time

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

work = 0
startTime = time.time()
currTime = startTime
flag = 0







def updateInfo() :
    #updating the indexes
    global phyIndex
    global menIndex
    
    global curr_time
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    #print(curr_time)


    global df1
    for index in range(len(df1)):
        if curr_time == df1.eTime[index]:
              phyIndex=phyIndex-10
              menIndex=menIndex-20
              messagebox.showinfo("reminder", "Hope you had a great meeting! Time for a 10 mins break")


    
    phyInLabel=Label (window, text = phyIndex , font=('Arial', 20, 'bold'), fg='#FFFFFF', bg='#000000')
    phyInLabel.place(x=300, y=tempY+70)

    menInLabel=Label (window, text = menIndex , font=('Arial', 20, 'bold'), fg='#FFFFFF', bg='#000000')
    menInLabel.place(x=300, y=tempY+140)

    
    # Camera
    global face_cascade
    global cap
    global work
    global startTime
    global currTime
    global flag
    global graphData


    #print(work)
    
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)

    

    # Draw the rectangle around each face
    if len(faces) == 0:
        pass
        '''if(flag == 1):
            work += currTime - startTime
            flag = 0
        
        startTime = time.time()
        currTime = time.time()'''

        

        

    else:
        '''flag = 1
        currTime = time.time()'''
        work+=1
        if (work>=30):
            #messagebox.showinfo("reminder", "take a break")
            work=0
            phyIndex-=5
            menIndex-=10
            showNotif("Take a break")
            
            curr_time = time.strftime("%H:%M:%S", time.localtime())
            tempDf=pd.DataFrame({
                'Time': [str(curr_time)],
                'PhysicalIndex': [phyIndex],
                'MentalIndex':[menIndex]
            })

            #graphData = graphData.append(tempDf,ignore_index=True)
            

            graphData = pd.concat([graphData, tempDf])
            
            
        


        for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    


    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    
    
    if k==27 :
        print(work)

    if (phyIndex<=50):
        r=random.randint(0,len(exerDf)-1)
        showNotif(str(exerDf['Physical'][r]))
        phyIndex=phyIndex+10
        
    if (menIndex<=50):
        r=random.randint(0, len(exerDf)-1)
        showNotif(str(exerDf['Mental'][r]))
        menIndex=menIndex+15
        
    
    
    
        
    window.after(1, updateInfo)


window.after(1, updateInfo)
window.mainloop()



