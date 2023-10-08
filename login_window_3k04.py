### Notes on Running
# Python 3.12
# Please install Pillow with the following commands in terminal
# python -m pip install --upgrade pip
# python -m pip install --upgrade Pillow

import tkinter as tk
from PIL import ImageTk, Image

loginPage = tk.Tk()
loginPage.title('Welcome to PaceMaker | Desktop Edition')

# Set Size of Window
widthApp = 600
heightApp = 500

# Do not let user modify size of application
loginPage.resizable(False, False)

# Capture screen width and height
screenW = loginPage.winfo_screenwidth()
screenH = loginPage.winfo_screenheight()

# Calculate center of screen
x_axisCentre = screenW/2 - widthApp/2
y_axisCentre = screenH/2 - heightApp/2

image1 = Image.open(r"C:\Users\joell\OneDrive\Desktop\pacemaker.png") #Fix to make locally stored in same location as patient info
resize_img = image1.resize((100,100))
heartIcon = ImageTk.PhotoImage(resize_img)

# Place window in centre of screen (slightly more up)
loginPage.geometry('%dx%d+%d+%d' % (widthApp, heightApp, x_axisCentre, y_axisCentre-50))
loginPage.grid_rowconfigure(0, weight=1)
loginPage.grid_columnconfigure(0, weight=1)

######## LAYOUT #########

# Main frame | Contains Title, Login prompt, and User/Pass grid
frame1 = tk.Frame(loginPage,width=600, height=100)
frame1.grid(row=0,  column=0) #Needed to show
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(0, weight=1)

# Embedded Frame for User/Pass
frame2 = tk.Frame(frame1,width=600, height=50)
frame2.grid(row=4,  column=0, pady = 5) #Needed to show
frame2.grid_rowconfigure(0, weight=1)
frame2.grid_columnconfigure(0, weight=1)

# Embedded Frame for New User label/button
frame3 = tk.Frame(frame1,width=600, height=50)
frame3.grid(row=7,  column=0, padx= 10, pady = 10) #Needed to show
frame3.grid_rowconfigure(0, weight=1)
frame3.grid_columnconfigure(0, weight=1)

# Welcome Label
welc = tk.Label(frame1, text = "Welcome to PaceMaker Desktop!", font=('Montserrat',24), anchor='center')
welc.grid(row=0,column=0)

# Heart icon
iconLabel = tk.Label(frame1, image = heartIcon)
iconLabel.grid(row=1,column=0)

# Login info prompt
entryMsg = tk.Label(frame1, text = "Please enter login information:", font=('Montserrat',12), anchor='center')
entryMsg.grid(row=2,column=0)

# Username label
userLabel = tk.Label(frame2, text = "Username:", font=('Montserrat',12), anchor='center')
userLabel.grid(row=0,column=0)

# Username Text Field Input from User --> Add Functionality
inputUser = tk.Text(frame2, height = 1, width = 20) 
inputUser.grid(row=0,column=1)

# Password Label 
passLabel = tk.Label(frame2, text = "Password:", font=('Montserrat',12), anchor='center')
passLabel.grid(row=1,column=0)

# Password Text Field Input from User --> Add Functionality
inputPass = tk.Text(frame2, height = 1, width = 20) 
inputPass.grid(row=1,column=1)

# Login Button --> Add Functionality
loginButton = tk.Button(frame1,text = "Login", font=('Montserrat',12), anchor='center')
loginButton.grid(row=5,column=0,pady = 5)

# Line Break
newUser = tk.Label(frame1,text = "____________________________________________", font=('Montserrat',12), anchor='center')
newUser.grid(row=6,column=0)

# New User prompt
newUser = tk.Label(frame3,text = "Need to create a new user?", font=('Montserrat',12), anchor='center')
newUser.grid(row=0,column=0)

# New User button --> Add functionality
newUser = tk.Button(frame3,text = "Create New User", font=('Montserrat',10), anchor='center')
newUser.grid(row=0,column=1, padx = 5)

# New User button --> Add functionality
slotLabel = tk.Label(frame1, text = "New Patient Slots Available: 10", font=('Montserrat',10), anchor='center',fg='#228B22')
slotLabel.grid(row=8,column=0, pady = 10)

loginPage.mainloop()