# Notes on Running...
# Python 3.12
# Please install Pillow with the following commands in terminal
# python -m pip install --upgrade pip
# python -m pip install --upgrade Pillow

import tkinter as tk
#from tkinter import tkk
from PIL import ImageTk, Image

### MAIN WINDOW CLASS ###
class mainWindow(tk.Tk):
    # Initialize class with __init__ function
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('PaceMaker | Desktop Edition')
        
        # Set Size of Window
        widthApp = 600
        heightApp = 500

        # Do not let user modify size of application
        self.resizable(False, False)

        # Capture screen width and height
        screenW = self.winfo_screenwidth()
        screenH = self.winfo_screenheight()

        # Calculate center of screen
        x_axisCentre = screenW/2 - widthApp/2
        y_axisCentre = screenH/2 - heightApp/2
        
        # Place window in centre of screen (slightly more up)
        self.geometry('%dx%d+%d+%d' % (widthApp, heightApp, x_axisCentre, y_axisCentre-50))
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_columnconfigure(0, weight=1)
        
        # Base frame is used to act as a base for switching frames
        base = tk.Frame(self)
        base.pack(side = "top", fill="both",expand=True, pady=20, padx=24)
        
        # Page Dictionary (UPDATE: Change to array if possible)
        self.pages = {}
        # Must initialize all the pages first
        #for pageNum in (welcome_page,user_page,main_page):
        
        for pageNum in (welcome_page,user_page,main_page):
            page = pageNum(base,self)
            self.pages[pageNum] = page
            page.grid(row = 0, column = 0, stick="nsew")
        
        #displays welcome page first
        self.display_page(welcome_page) #displays welcome page first
        
    # Displays the desired page    
    def display_page(self,display):
        page = self.pages[display] #Set page to chosen value of display
        page.tkraise() #Raise the frame to the top of the window
    
#### WELCOME PAGE ####
class welcome_page(tk.Frame):
    # parent is needed for all widgets that are not the root tkinter window
    # controller allows for low coupling, frames can be accessed 
    # with accessing controller instead of frame directly
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        # Main frame | Contains Title, Login prompt, and User/Pass grid
        
        # Import Media
        image1 = Image.open(r"C:\Users\joell\OneDrive\Desktop\pacemaker.png") #Fix to make locally stored in same location as patient info
        resize_img = image1.resize((100,100))
        self.photo = ImageTk.PhotoImage(resize_img)

        # Welcome Label
        welc = tk.Label(self, text = "Welcome to PaceMaker Desktop!", font=('Montserrat',24), anchor='center')
        welc.grid(row=0,column=0, columnspan=2)

        # Heart icon
        iconLabel = tk.Label(self, image = self.photo)
        iconLabel.grid(row=1,column=0, columnspan=2)

        # Login info prompt
        entryMsg = tk.Label(self, text = "Please enter login information:", font=('Montserrat',12), anchor='center')
        entryMsg.grid(row=2,column=0,pady = 2, columnspan=2)

        # Username label
        userLabel = tk.Label(self, text = "Username:", font=('Montserrat',12), anchor='center')
        userLabel.grid(row=3,column=0, sticky= tk.E, padx = 12)

        # Username Text Field Input from User --> Add Functionality
        inputUser = tk.Text(self, height = 1, width = 15) 
        inputUser.grid(row=3,column=1, sticky= tk.W)

        # Password Label 
        passLabel = tk.Label(self, text = "Password:", font=('Montserrat',12))
        passLabel.grid(row=4,column=0, sticky= tk.E, padx = 12)

        # Password Text Field Input from User --> Add Functionality
        inputPass = tk.Entry(self, width = 20, show='*') 
        inputPass.grid(row=4,column=1, sticky= tk.W)

        # Login Button --> Add Functionality
        loginButton = tk.Button(self,text = "Login", font=('Montserrat',12), anchor='center',command=lambda : controller.display_page(main_page))
        loginButton.grid(row=5,column=0,pady = 10, columnspan=2)

        # Line Break
        newUser = tk.Label(self,text = "___________________________________________________", font=('Montserrat',12), anchor='center')
        newUser.grid(row=6,column=0, columnspan=2)

        # New User prompt
        newUser = tk.Label(self,text = "Need to create a new user?", font=('Montserrat',12), anchor='center')
        newUser.grid(row=8,column=0, pady = 10, columnspan=2)

        # New User button --> Add functionality
        newUser = tk.Button(self,text = "Create New User", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(user_page))
        newUser.grid(row=9,column=0, columnspan=2)

        # Update when new user is made (decrease count please!)
        slotLabel = tk.Label(self, text = "New Patient Slots Available: 10", font=('Montserrat',10), anchor='center',fg='#228B22')
        slotLabel.grid(row=10,column=0, pady = 10, columnspan=2)

#### USER PAGE ####
class user_page(tk.Frame):
    # parent is needed for all widgets that are not the root tkinter window
    # controller allows for low coupling, frames can be accessed 
    # with accessing controller instead of frame directly
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        ######## LAYOUT #########
        # New Patient Registration frame

        # Please Input New Patient Details:
        detailLabel = tk.Label(self, text = "Please Input New Patient Details:", font=('Montserrat',18), anchor='center')
        detailLabel.grid(row=0,column=0,columnspan=2)

        # Username label
        userLabelnew = tk.Label(self, text = "Username:", font=('Montserrat',12), anchor='center')
        userLabelnew.grid(row=1,column=0)

        # Username Text Field Input from User --> Add Functionality
        inputUsernew = tk.Text(self, height = 1, width = 20) 
        inputUsernew.grid(row=1,column=1, pady = 20)

        # Password Label
        userLabelnew = tk.Label(self, text = "Password:", font=('Montserrat',12), anchor='center')
        userLabelnew.grid(row=2,column=0)

        # Password Text Field Input from User --> Add Functionality
        inputUsernew = tk.Text(self, height = 1, width = 20) 
        inputUsernew.grid(row=2,column=1)

        # Verify Password Label
        userLabelnew = tk.Label(self, text = "Verify Password:", font=('Montserrat',12), anchor="center")
        userLabelnew.grid(row=3,column=0, padx=20)

        # Verify Password Text Field Input from User --> Add Functionality
        inputUsernew = tk.Text(self, height = 1, width = 20) 
        inputUsernew.grid(row=3,column=1)

        # New User button --> Add functionality to create user once correct data is entered
        newUser = tk.Button(self,text = "Create New User", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(welcome_page))
        newUser.grid(row=4,column=1, pady = 20)

        # Return to home screen --> Add functionality
        newUser = tk.Button(self,text = "Cancel", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(welcome_page))
        newUser.grid(row=4,column=0, pady = 20)
        
#### USER PAGE ####
class main_page(tk.Frame):
    # parent is needed for all widgets that are not the root tkinter window
    # controller allows for low coupling, frames can be accessed 
    # with accessing controller instead of frame directly
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        detailLabel = tk.Label(self, text = "<Main Page>", font=('Montserrat',18), anchor='center')
        detailLabel.grid(row=0,column=0,columnspan=2)
        
pacemakerApp = mainWindow()
pacemakerApp.mainloop()