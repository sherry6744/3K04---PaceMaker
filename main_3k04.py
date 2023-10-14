# Notes on Running...
# Python 3.12
# Please install Pillow with the following commands in terminal
# python -m pip install --upgrade pip
# python -m pip install --upgrade Pillow
# pip install tkcalendar
# Download pacemaker.jpg from github and change directory in line 72 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry
from PIL import ImageTk, Image
from patient import Patient
import patient
import csv

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
        
        for pageNum in (welcome_page,user_page,main_page,AOO_page,AAI_page,VOO_page,VVI_page,set_date_time):
            page = pageNum(base,self)
            self.pages[pageNum] = page
            page.grid(row = 0, column = 0, sticky="nsew")
        
        #displays welcome page first
        self.display_page(welcome_page) #displays welcome page first
        
    # Displays the desired page    
    def display_page(self,display):
        self.update()
        self.update_idletasks()
        page = self.pages[display] #Set page to chosen value of display
        page.tkraise() #Raise the frame to the top of the window
    
    def on_login(self,state_status):
        if (state_status == 0):
            messagebox.showinfo(title="Invalid Login", message="Username is incorrect.")
        elif (state_status == 1):
            messagebox.showinfo(title="Invalid Login", message="Password is incorrect.")
        elif (state_status == 2):       
            self.display_page(main_page)
            
    def on_create(self,max_val):
        print(max_val)
        if (max_val == 0):
            messagebox.showinfo(title="Error", message="Max patients reached. Limit of 10 patients.")
        else:
            self.display_page(user_page)
        
    def logTime(self):
        timeSave = datetime.now()
        messagebox.showinfo(title="Updated Time.", message="Time logged: " + str(timeSave))
        print(timeSave)
        # Can be logged with future patient reports.
    
#### WELCOME PAGE ####
class welcome_page(tk.Frame):
    # parent is needed for all widgets that are not the root tkinter window
    # controller allows for low coupling, frames can be accessed 
    # with accessing controller instead of frame directly
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        # Main frame | Contains Title, Login prompt, and User/Pass grid
        
        # Import Media
        image1 = Image.open(r"C:\Users\aggar\OneDrive\Desktop\Mcmaster\Sem 5\3K04\3K04---PaceMaker\pacemaker.png") #Fix to make locally stored in same location as patient info
        #image1 = Image.open(r"C:\Users\joell\OneDrive\Desktop\pacemaker.png") #Fix to make locally stored in same location as patient info
        
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
        #print(inputPass.get())

        # Login Button --> Add Functionality
        #loginButton = tk.Button(self,text = "Login", font=('Montserrat',12), anchor='center',command=lambda : self.loginState(patient.loginUser(inputUser.get("1.0","end-1c"),inputPass.get())))
        #loginButton = tk.Button(self,text = "Login", font=('Montserrat',12), anchor='center',command=lambda : print(type(inputPass.get())))
        loginButton = tk.Button(self,text = "Login", font=('Montserrat',12), anchor='center',command= lambda : controller.on_login(patient.loginUser(inputUser.get("1.0","end-1c"),inputPass.get())))
        loginButton.grid(row=5,column=0,pady = 10, columnspan=2)

        # Line Break
        newUser = tk.Label(self,text = "___________________________________________________", font=('Montserrat',12), anchor='center')
        newUser.grid(row=6,column=0, columnspan=2)

        # New User prompt
        newUser = tk.Label(self,text = "Need to create a new user?", font=('Montserrat',12), anchor='center')
        newUser.grid(row=8,column=0, pady = 10, columnspan=2)

        # New User button --> Add functionality
        newUser = tk.Button(self,text = "Create New User", font=('Montserrat',10), anchor='center',command=lambda : controller.on_create(patient.availUsers()))
        newUser.grid(row=9,column=0, columnspan=2)

        # Update when new user is made (decrease count please!)
        slotLabel = tk.Button(self, text = "New Patient Slots Available", font=('Montserrat',10), anchor='center',fg='#228B22',command=lambda : self.checkAvail())
        slotLabel.grid(row=10,column=0, pady = 10, columnspan=2)
        
    def checkAvail(self):
        messagebox.showinfo(title="Available Patient Slots", message="There are currently " + str(patient.availUsers()) + " patient slots.")
     
    
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
        inputPassnew = tk.Text(self, height = 1, width = 20) 
        inputPassnew.grid(row=2,column=1)

        # Verify Password Label
        userLabelnew = tk.Label(self, text = "Verify Password:", font=('Montserrat',12), anchor="center")
        userLabelnew.grid(row=3,column=0, padx=20)

        # Verify Password Text Field Input from User --> Add Functionality
        inputPassVal = tk.Text(self, height = 1, width = 20) 
        inputPassVal.grid(row=3,column=1)
        value=inputPassVal.get("1.0","end-1c")
        

        # New User button --> Add functionality to create user once correct data is entered
        #newUser = tk.Button(self,text = "Create New User", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(welcome_page))
        newUser = tk.Button(self,text = "Create New User", font=('Montserrat',10), anchor='center',command=lambda : self.createUser(inputUsernew.get("1.0","end-1c"),inputPassnew.get("1.0","end-1c"),inputPassVal.get("1.0","end-1c")))
        newUser.grid(row=4,column=1, pady = 20)

        # Return to home screen --> Add functionality
        backButton = tk.Button(self,text = "Back", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(welcome_page))
        backButton.grid(row=4,column=0, pady = 20)
    
    def createUser(self,userInput,passInput,passCheck):
        
        validUser = userInput
        validPass = passInput
        checkPass = passCheck
        uCheck = True
        newPatient = Patient(validUser,validPass)
        
        if (validPass != checkPass):
            messagebox.showinfo(title="Invalid Password", message="Invalid password, please verify password entries are identical.")
        if (patient.uniqueUser(newPatient) == False):
            messagebox.showinfo(title="Invalid User", message="This username is already taken, please create another username.")
        elif (validPass == checkPass and uCheck == True):
            #Add new patient
            patient.addPatient(newPatient)
            messagebox.showinfo(title= "New User Successfully Created.", message="New user " + validUser + " was successfully created. Please verify login in Welcome Window.")
            
            
            
#### MAIN PAGE ####
class main_page(tk.Frame):
    # parent is needed for all widgets that are not the root tkinter window
    # controller allows for low coupling, frames can be accessed 
    # with accessing controller instead of frame directly
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        detailLabel = tk.Label(self, text = "Main Menu", font=('Montserrat',18), anchor='center',)
        detailLabel.grid(row=0,column=0,columnspan=2)
        
        aboutButton = tk.Button(self,text = "About", font=('Montserrat',10), anchor='center',command=lambda : messagebox.showinfo(title="About", message="Model Number : 22 \nSoftware Revision Number : 1\nDCM Serial Number : 21\nMcMaster University"))
        aboutButton.grid(row=1,column=0, pady = 20)
        
        set_timeButton = tk.Button(self,text = "Set Date and Time", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(set_date_time))
        set_timeButton.grid(row=2,column=0, pady = 20)
        
        end_telementryButton = tk.Button(self,text = "End Telemetry", font=('Montserrat',10), anchor='center',command=lambda : messagebox.showinfo(title="Attention", message='Telementry session ended'))
        end_telementryButton .grid(row=3,column=0, pady = 20)
        
        newpatientButton = tk.Button(self,text = "Back", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(welcome_page))
        newpatientButton .grid(row=4,column=0, pady = 20)
        
        border = tk.Label(self,text = "|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|", font=('Montserrat',12), anchor='center')
        border.grid(row=1,column=1, rowspan=5,padx = 20)
        
        read_connection = tk.Label(self,text ='Device Not Connected',font=('Montserrat',10),anchor = 'center',fg = '#ff4500')
        read_connection.grid(row=4,column=3)
        
        # ComboBox menu for pace modes
        dropdown = ttk.Combobox(self, width = 10)
        # pace mode options
        dropdown['values'] = ('AOO','AAI','VOO','VVI') 
        dropdown.grid(row = 1, column =2,padx =50)
        
        
        def parameter(e):
            if dropdown.get() == 'AOO':    
                
                openButton = tk.Button(self,text = "Open", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(AOO_page))
                openButton.grid(row=1,column=3, pady = 20)
                print(openButton)
                     
            elif dropdown.get() == 'AAI':
                
                openButton = tk.Button(self,text = "Open", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(AAI_page))
                openButton.grid(row=1,column=3, pady = 20)
               
            elif dropdown.get() == 'VOO':

               openButton = tk.Button(self,text = "Open", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(VOO_page))
               openButton.grid(row=1,column=3, pady = 20)
               
                 
            elif dropdown.get() == 'VVI':
                
                openButton = tk.Button(self,text = "Open", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(VVI_page))
                openButton.grid(row=1,column=3, pady = 20)
                
            else:
                pass
            
        #bind the dropdown menu to parameter function
        dropdown.bind("<<ComboboxSelected>>",parameter)
        
class set_date_time(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        dateSet = tk.Label(self, text = "Calendar View:", font=('Montserrat',18), anchor='center',)
        dateSet.grid(row=0,column=0,columnspan=2, sticky="w")
        cal=DateEntry(self,selectmode='day')
        cal.grid(row=1,column=0,padx=15)
        
        timeSet = tk.Label(self, text = "Current Time:", font=('Montserrat',18), anchor='center',)
        timeSet.grid(row=2,column=0,columnspan=2, sticky="w")
        
        saveButton = tk.Button(self,text = "Log Current Time", font=('Montserrat',10), anchor='center',command=lambda : controller.logTime())
        saveButton.grid(row=3,column=0, pady = 10)
        
        backButton = tk.Button(self,text = "Back", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
        backButton.grid(row=3,column=1, pady = 10, padx = 10)


class AOO_page(tk.Frame):
    # parent is needed for all widgets that are not the root tkinter window
    # controller allows for low coupling, frames can be accessed 
    # with accessing controller instead of frame directly
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        #1 shows label and entry box for lower rate limit
        #lower rate limit label
        lower_rate = tk.Label(self,text = 'Lower Rate Limit', font = ('Montserrat',12),anchor = 'center')
        lower_rate.grid(row = 1, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #lower rate limit field input
        lower_rate_limit_val = ttk.Combobox(self, width = 10) 
        lower_rate_limit_val.grid(column = 2, row = 1,sticky ='W')
        lower_rate_limit_val['values'] = (30,35,40,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,
                                     80,81,82,83,84,85,86,87,88,89,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175) 
        lower_rate_limit_val.current(0)
        
        #2 shows label and entry box for upper rate limit
        #Upper rate limit label
        upper_rate = tk.Label(self,text = 'Upper Rate Limit', font = ('Montserrat',12),anchor = 'center')
        upper_rate.grid(row = 2, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #Upper rate limit field input
        upper_rate_limit_val = ttk.Combobox(self, width = 10) 
        upper_rate_limit_val.grid(row = 2,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        upper_rate_limit_val['values'] = (50,55,60,65,70,75,80,85,90,95,100,105,110,115,
                                     120,125,130,135,140,145,150,155,160,165,170,175) 
        upper_rate_limit_val.current(0)
        
        #3 shows label and entry box for atrial amplitude
        #Atrial amplitude label
        atrial_amp = tk.Label(self,text = 'Atrial Amplitude', font = ('Montserrat',12),anchor = 'center')
        atrial_amp.grid(row = 3, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #atrial_amp field input
        atrial_amplitude_val = ttk.Combobox(self, width = 10) 
        atrial_amplitude_val.grid(row = 3,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        atrial_amplitude_val['values'] = (0,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,
                                     2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5) 
        atrial_amplitude_val.current(0)
        
        #4 shows label and entry box for Atrial pulse
        #Atrial pulse width label
        atrial_puls = tk.Label(self,text = 'Atrial Pulse Width', font = ('Montserrat',12),anchor = 'center')
        atrial_puls.grid(row = 5, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #atrial_pulse field input
        atrial_pulse_val = ttk.Combobox(self, width = 10) 
        atrial_pulse_val.grid(row = 5,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        atrial_pulse_val['values'] = (0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9) 
        atrial_pulse_val.current(0)
        
        
        saveButton = tk.Button(self,text = "Save", font=('Montserrat',10), anchor='center',command=lambda : print({'LRL':lower_rate_limit_val.get(),'URL':upper_rate_limit_val.get(),'AA':atrial_amplitude_val.get(),'AP':atrial_pulse_val.get()}))
        saveButton.grid(row=1,column=0, pady = 10)
        
        backButton = tk.Button(self,text = "Back", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
        backButton.grid(row=2,column=0, pady = 10)
        

        
class VOO_page(tk.Frame):
    # parent is needed for all widgets that are not the root tkinter window
    # controller allows for low coupling, frames can be accessed 
    # with accessing controller instead of frame directly
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        #1 shows label and entry box for lower rate limit
        #lower rate limit label
        lower_rate = tk.Label(self,text = 'Lower Rate Limit', font = ('Montserrat',12),anchor = 'center')
        lower_rate.grid(row = 1, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #lower rate limit field input
        lower_rate_limit_val = ttk.Combobox(self, width = 10) 
        lower_rate_limit_val.grid(column = 2, row = 1,sticky ='W')
        lower_rate_limit_val['values'] = (30,35,40,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,
                                     80,81,82,83,84,85,86,87,88,89,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175) 
        lower_rate_limit_val.current(0)
        
        #2 shows label and entry box for upper rate limit
        #Upper rate limit label
        upper_rate = tk.Label(self,text = 'Upper Rate Limit', font = ('Montserrat',12),anchor = 'center')
        upper_rate.grid(row = 2, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #Upper rate limit field input
        upper_rate_limit_val = ttk.Combobox(self, width = 10) 
        upper_rate_limit_val.grid(row = 2,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        upper_rate_limit_val['values'] = (50,55,60,65,70,75,80,85,90,95,100,105,110,115,
                                     120,125,130,135,140,145,150,155,160,165,170,175) 
        upper_rate_limit_val.current(0)

        #3 shows label and entry box for Ventrical amplitude
        #Ventrical amplitude label
        ventrical_amp = tk.Label(self,text = 'Ventrical Amplitude', font = ('Montserrat',12),anchor = 'center')
        ventrical_amp.grid(row = 4, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #Ventrical_amp field input
        ventrical_amplitude_val = ttk.Combobox(self, width = 10) 
        ventrical_amplitude_val.grid(row = 4,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        ventrical_amplitude_val['values'] = (0,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,
                                     2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5) 
        ventrical_amplitude_val.current(0)
        
        #4 shows label and entry box for Ventrical pulse
        ventrical_puls = tk.Label(self,text = 'Ventrical Pulse Width', font = ('Montserrat',12),anchor = 'center')
        ventrical_puls.grid(row = 6, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #ventrical pulse field input
        ventrical_pulse_val = ttk.Combobox(self, width = 10) 
        ventrical_pulse_val.grid(row = 6,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        ventrical_pulse_val['values'] = (0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9) 
        ventrical_pulse_val.current(0)
        
        saveButton = tk.Button(self,text = "Save", font=('Montserrat',10), anchor='center',command=lambda : print({'LRL':lower_rate_limit_val.get(),'URL':upper_rate_limit_val.get(),'VA':ventrical_amplitude_val.get(),'VP':ventrical_pulse_val.get()}))
        saveButton.grid(row=1,column=0, pady = 10)
        
        backButton = tk.Button(self,text = "Back", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
        backButton.grid(row=2,column=0, pady = 10)
        
        
        
class AAI_page(tk.Frame):
    # parent is needed for all widgets that are not the root tkinter window
    # controller allows for low coupling, frames can be accessed 
    # with accessing controller instead of frame directly
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        #1 shows label and entry box for lower rate limit
        #lower rate limit label
        lower_rate = tk.Label(self,text = 'Lower Rate Limit', font = ('Montserrat',12),anchor = 'center')
        lower_rate.grid(row = 1, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #lower rate limit field input
        lower_rate_limit_val = ttk.Combobox(self, width = 10) 
        lower_rate_limit_val.grid(column = 2, row = 1,sticky ='W')
        lower_rate_limit_val['values'] = (30,35,40,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,
                                     80,81,82,83,84,85,86,87,88,89,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175) 
        lower_rate_limit_val.current(0)
        
        #2 shows label and entry box for upper rate limit
        #Upper rate limit label
        upper_rate = tk.Label(self,text = 'Upper Rate Limit', font = ('Montserrat',12),anchor = 'center')
        upper_rate.grid(row = 2, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #Upper rate limit field input
        upper_rate_limit_val = ttk.Combobox(self, width = 10) 
        upper_rate_limit_val.grid(row = 2,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        upper_rate_limit_val['values'] = (50,55,60,65,70,75,80,85,90,95,100,105,110,115,
                                     120,125,130,135,140,145,150,155,160,165,170,175) 
        upper_rate_limit_val.current(0)
        
        #3 shows label and entry box for atrial amplitude
        #Atrial amplitude label
        atrial_amp = tk.Label(self,text = 'Atrial Amplitude', font = ('Montserrat',12),anchor = 'center')
        atrial_amp.grid(row = 3, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #atrial_amp field input
        atrial_amplitude_val = ttk.Combobox(self, width = 10) 
        atrial_amplitude_val.grid(row = 3,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        atrial_amplitude_val['values'] = (0,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,
                                     2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5) 
        atrial_amplitude_val.current(0)
        
        #4 shows label and entry box for Atrial pulse
        #Atrial pulse width label
        atrial_puls = tk.Label(self,text = 'Atrial Pulse Width', font = ('Montserrat',12),anchor = 'center')
        atrial_puls.grid(row = 5, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #atrial pulse field input
        atrial_pulse_val = ttk.Combobox(self, width = 10) 
        atrial_pulse_val.grid(row = 5,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        atrial_pulse_val['values'] = (0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9) 
        atrial_pulse_val.current(0)
        
        #5 shows label and entry box for atrial sensitivity
        atrial_sense = tk.Label(self,text = 'Atrial Sensitivity', font = ('Montserrat',12),anchor = 'center')
        atrial_sense.grid(row = 7, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #atrial sensitivity field input
        atrial_sensitivity_val = ttk.Combobox(self, width = 10) 
        atrial_sensitivity_val.grid(row = 7,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        atrial_sensitivity_val['values'] = (0.25,0.5,0.75,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0) 
        atrial_sensitivity_val.current(0)
        
        #6 shows label and entry box for ARP
        atrial_period = tk.Label(self,text = 'Atrial Refractory Period', font = ('Montserrat',12),anchor = 'center')
        atrial_period.grid(row = 10, column = 1,sticky = 'we', pady =10,padx =50 )
        
        #arp field input
        arp_val = ttk.Combobox(self, width = 10) 
        arp_val .grid(row = 10,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        arp_val ['values'] = (150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500) 
        arp_val .current(0)
        
        #7 shows label and entry box for PVARP
        #PVARP width label
        pvar_period = tk.Label(self,text = 'PVARP', font = ('Montserrat',12),anchor = 'center')
        pvar_period.grid(row = 11, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #PVARP field input
        pvarp_val  = ttk.Combobox(self, width = 10) 
        pvarp_val .grid(row = 11,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        pvarp_val ['values'] = (150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500) 
        pvarp_val .current(0)
        
        #8 shows label and entry box for Hysteresis
        #Hysteresis width label
        hys_limit = tk.Label(self,text = 'Hysteresis', font = ('Montserrat',12),anchor = 'center')
        hys_limit.grid(row = 12, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #Hysteresis field input
        hysteresis_val  = ttk.Combobox(self, width = 10) 
        hysteresis_val .grid(row = 12,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        hysteresis_val ['values'] =(0,30,35,40,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,
                                     80,81,82,83,84,85,86,87,88,89,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175) 
        hysteresis_val .current(0)
        
        #9 shows label and entry box for Rate Smoothing
        #Rate Smoothing width label
        rate_smoothing = tk.Label(self,text = 'Rate Smoothing (%)', font = ('Montserrat',12),anchor = 'center')
        rate_smoothing.grid(row = 13, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #Rate Smoothing field input
        rate_smoothing_val  = ttk.Combobox(self, width = 10) 
        rate_smoothing_val .grid(row = 13,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        rate_smoothing_val ['values'] =(0,3,6,9,12,15,18,21,25) 
        rate_smoothing_val .current(0)
        
        
        #no functionality
        saveButton = tk.Button(self,text = "Save", font=('Montserrat',10), anchor='center',command=lambda :print({'LRL':lower_rate_limit_val.get(),'URL':upper_rate_limit_val.get(),'AA':atrial_amplitude_val.get(),'AP':atrial_pulse_val.get(),'AS':atrial_sensitivity_val.get(),'ARP':arp_val.get(),'PVARP':pvarp_val.get(),'H':hysteresis_val.get(),'RS':rate_smoothing_val.get()}))
        saveButton.grid(row=1,column=0, pady = 10)
        
        backButton = tk.Button(self,text = "Back", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
        backButton.grid(row=2,column=0, pady = 10)

class VVI_page(tk.Frame):
    # parent is needed for all widgets that are not the root tkinter window
    # controller allows for low coupling, frames can be accessed 
    # with accessing controller instead of frame directly
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        #1 shows label and entry box for lower rate limit
        #lower rate limit label
        lower_rate = tk.Label(self,text = 'Lower Rate Limit', font = ('Montserrat',12),anchor = 'center')
        lower_rate.grid(row = 1, column = 1,sticky = 'we', pady = 10,padx =50 )
       
        #lower rate limit field input
        lower_rate_limit_val = ttk.Combobox(self, width = 10) 
        lower_rate_limit_val.grid(column = 2, row = 1,sticky ='W')
        lower_rate_limit_val['values'] = (30,35,40,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,
                                    80,81,82,83,84,85,86,87,88,89,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175) 
        lower_rate_limit_val.current(0)
       
        #2 shows label and entry box for upper rate limit
        #Upper rate limit label
        upper_rate = tk.Label(self,text = 'Upper Rate Limit', font = ('Montserrat',12),anchor = 'center')
        upper_rate.grid(row = 2, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #Upper rate limit field input
        upper_rate_limit_val = ttk.Combobox(self, width = 10) 
        upper_rate_limit_val.grid(row = 2,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        upper_rate_limit_val['values'] = (50,55,60,65,70,75,80,85,90,95,100,105,110,115,
                                    120,125,130,135,140,145,150,155,160,165,170,175) 
        upper_rate_limit_val.current(0)
        
        #3 shows label and entry box for Ventrical amplitude
        #ventrical_amp label
        ventrical_amp = tk.Label(self,text = 'Ventrical Amplitude', font = ('Montserrat',12),anchor = 'center')
        ventrical_amp.grid(row = 4, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #ventrical_amp field input
        ventrical_amplitude_val = ttk.Combobox(self, width = 10) 
        ventrical_amplitude_val.grid(row = 4,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        ventrical_amplitude_val['values'] = (0,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,
                                     2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5) 
        ventrical_amplitude_val.current(0)
        
        #4 shows label and entry box for Ventrical pulse
        ventrical_puls = tk.Label(self,text = 'Ventrical Pulse Width', font = ('Montserrat',12),anchor = 'center')
        ventrical_puls.grid(row = 6, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #ventrical_pulse field input
        ventrical_pulse_val = ttk.Combobox(self, width = 10) 
        ventrical_pulse_val.grid(row = 6,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        ventrical_pulse_val['values'] = (0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9) 
        ventrical_pulse_val.current(0)
        
        #5 shows label and entry box for ventrical sensitivity
        ventrical_sense = tk.Label(self,text = 'Ventrical Sensitivity', font = ('Montserrat',12),anchor = 'center')
        ventrical_sense.grid(row = 8, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #ventrical sensitivity field input
        ventrical_sensitivity_val  = ttk.Combobox(self, width = 10) 
        ventrical_sensitivity_val .grid(row = 8,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        ventrical_sensitivity_val ['values'] = (0.25,0.5,0.75,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0) 
        ventrical_sensitivity_val .current(0)
        
        #6 shows label and entry box for VRP
        #VRP width label
        ventrical_period = tk.Label(self,text = 'Ventrical Refractory Period', font = ('Montserrat',12),anchor = 'center')
        ventrical_period.grid(row = 9, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #VRP field input
        vrp_val  = ttk.Combobox(self, width = 10) 
        vrp_val .grid(row = 9,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        vrp_val ['values'] = (150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500) 
        vrp_val .current(0)
        
        #7 shows label and entry box for Hysteresis
        hys_limit = tk.Label(self,text = 'Hysteresis', font = ('Montserrat',12),anchor = 'center')
        hys_limit.grid(row = 12, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #Hysteresis field input
        hysteresis_val  = ttk.Combobox(self, width = 10) 
        hysteresis_val .grid(row = 12,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        hysteresis_val ['values'] =(0,30,35,40,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,
                                     80,81,82,83,84,85,86,87,88,89,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175) 
        hysteresis_val .current(0)
        
        #8 shows label and entry box for Rate Smoothing
        #Rate Smoothing width label
        rate_smoothing = tk.Label(self,text = 'Rate Smoothing (%)', font = ('Montserrat',12),anchor = 'center')
        rate_smoothing.grid(row = 13, column = 1,sticky = 'we', pady = 10,padx =50 )
        
        #Rate Smoothing field input
        rate_smoothing_val  = ttk.Combobox(self, width = 10) 
        rate_smoothing_val .grid(row = 13,column = 2,sticky ='W') 
        # Adding combobox drop down list 
        rate_smoothing_val ['values'] =(0,3,6,9,12,15,18,21,25) 
        rate_smoothing_val .current(0)
        
        #no functionality
        saveButton = tk.Button(self,text = "Save", font=('Montserrat',10), anchor='center',command=lambda : print({'LRL':lower_rate_limit_val.get(),'URL':upper_rate_limit_val.get(),'VA':ventrical_amplitude_val.get(),'VP':ventrical_pulse_val.get(),'VS':ventrical_sensitivity_val.get(),'VRP':vrp_val.get(),'H':hysteresis_val.get(),'RS':rate_smoothing_val.get()}))
        saveButton.grid(row=1,column=0, pady = 10)
        
        backButton = tk.Button(self,text = "Back", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
        backButton.grid(row=2,column=0, pady = 10)



def main():
    patient.createPD()
    pacemakerApp = mainWindow()
    pacemakerApp.mainloop()
    
    
if __name__ == '__main__':
    main()
