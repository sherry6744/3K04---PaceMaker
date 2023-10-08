import tkinter as tk

newUserPage = tk.Tk()
newUserPage.title('New User Registration')

# Set Size of Window
widthApp = 600
heightApp = 500

# Do not let user modify size of application
newUserPage.resizable(False, False)

# Capture screen width and height
screenW = newUserPage.winfo_screenwidth()
screenH = newUserPage.winfo_screenheight()

# Calculate center of screen
x_axisCentre = screenW/2 - widthApp/2
y_axisCentre = screenH/2 - heightApp/2

# Place window in centre of screen (slightly more up)
newUserPage.geometry('%dx%d+%d+%d' % (widthApp, heightApp, x_axisCentre, y_axisCentre-50))
newUserPage.grid_rowconfigure(0, weight=1)
newUserPage.grid_columnconfigure(0, weight=1)

######## LAYOUT #########

# New Patient Registration frame
frame_newUser = tk.Frame(newUserPage,width=600, height=600)
frame_newUser.grid(row=0,  column=0) #Needed to show
frame_newUser.grid_rowconfigure(0, weight=1)
frame_newUser.grid_columnconfigure(0, weight=1)

# Please Input New Patient Details:
detailLabel = tk.Label(frame_newUser, text = "Please Input New Patient Details:", font=('Montserrat',18), anchor='center')
detailLabel.grid(row=0,column=0,columnspan=2)

# Username label
userLabelnew = tk.Label(frame_newUser, text = "Username:", font=('Montserrat',12), anchor='center')
userLabelnew.grid(row=1,column=0)

# Username Text Field Input from User --> Add Functionality
inputUsernew = tk.Text(frame_newUser, height = 1, width = 20) 
inputUsernew.grid(row=1,column=1, pady = 20)

# Password Label
userLabelnew = tk.Label(frame_newUser, text = "Password:", font=('Montserrat',12), anchor='center')
userLabelnew.grid(row=2,column=0)

# Password Text Field Input from User --> Add Functionality
inputUsernew = tk.Text(frame_newUser, height = 1, width = 20) 
inputUsernew.grid(row=2,column=1)

# Verify Password Label
userLabelnew = tk.Label(frame_newUser, text = "Verify Password:", font=('Montserrat',12), anchor="center")
userLabelnew.grid(row=3,column=0, padx=20)

# Verify Password Text Field Input from User --> Add Functionality
inputUsernew = tk.Text(frame_newUser, height = 1, width = 20) 
inputUsernew.grid(row=3,column=1)

# New User button --> Add functionality to create user once correct data is entered
newUser = tk.Button(frame_newUser,text = "Create New User", font=('Montserrat',10), anchor='center')
newUser.grid(row=4,column=1, pady = 20)

# Return to home screen --> Add functionality
newUser = tk.Button(frame_newUser,text = "Cancel", font=('Montserrat',10), anchor='center')
newUser.grid(row=4,column=0, pady = 20)

newUserPage.mainloop()