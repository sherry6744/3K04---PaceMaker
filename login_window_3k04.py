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

def get_pass():
    print(inputPass.get())

######## LAYOUT #########

# Main frame | Contains Title, Login prompt, and User/Pass grid
frame_welcome = tk.Frame(loginPage,width=600, height=100)
frame_welcome.grid(row=0,  column=0) #Needed to show
frame_welcome.grid_rowconfigure(0, weight=1)
frame_welcome.grid_columnconfigure(0, weight=1)
frame_welcome.grid_rowconfigure(1, weight=1)
frame_welcome.grid_columnconfigure(1, weight=1)

# Welcome Label
welc = tk.Label(frame_welcome, text = "Welcome to PaceMaker Desktop!", font=('Montserrat',24), anchor='center')
welc.grid(row=0,column=0, columnspan=2)

# Heart icon
iconLabel = tk.Label(frame_welcome, image = heartIcon)
iconLabel.grid(row=1,column=0, columnspan=2)

# Login info prompt
entryMsg = tk.Label(frame_welcome, text = "Please enter login information:", font=('Montserrat',12), anchor='center')
entryMsg.grid(row=2,column=0,pady = 2, columnspan=2)

# Username label
userLabel = tk.Label(frame_welcome, text = "Username:", font=('Montserrat',12), anchor='center')
userLabel.grid(row=3,column=0, sticky= tk.E, padx = 12)

# Username Text Field Input from User --> Add Functionality
inputUser = tk.Text(frame_welcome, height = 1, width = 15) 
inputUser.grid(row=3,column=1, sticky= tk.W)

# Password Label 
passLabel = tk.Label(frame_welcome, text = "Password:", font=('Montserrat',12))
passLabel.grid(row=4,column=0, sticky= tk.E, padx = 12)

# Password Text Field Input from User --> Add Functionality
inputPass = tk.Entry(frame_welcome, width = 20, show='*') 
inputPass.grid(row=4,column=1, sticky= tk.W)

# Login Button --> Add Functionality
loginButton = tk.Button(frame_welcome,text = "Login", font=('Montserrat',12),command= get_pass, anchor='center')
loginButton.grid(row=5,column=0,pady = 10, columnspan=2)

# Line Break
newUser = tk.Label(frame_welcome,text = "___________________________________________________", font=('Montserrat',12), anchor='center')
newUser.grid(row=6,column=0, columnspan=2)

# New User prompt
newUser = tk.Label(frame_welcome,text = "Need to create a new user?", font=('Montserrat',12), anchor='center')
newUser.grid(row=8,column=0, pady = 10, columnspan=2)

# New User button --> Add functionality
newUser = tk.Button(frame_welcome,text = "Create New User", font=('Montserrat',10), anchor='center')
newUser.grid(row=9,column=0, columnspan=2)

# Update when new user is made (decrease count please!)
slotLabel = tk.Label(frame_welcome, text = "New Patient Slots Available: 10", font=('Montserrat',10), anchor='center',fg='#228B22')
slotLabel.grid(row=10,column=0, pady = 10, columnspan=2)

loginPage.mainloop()
