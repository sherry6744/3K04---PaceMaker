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
        
        for pageNum in (welcome_page,user_page,main_page,parameters_page,set_date_time):
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
        image1 = Image.open(r"C:\Users\aggar\OneDrive\Desktop\pacemaker.png") #Fix to make locally stored in same location as patient info
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
        value = inputPassVal.get("1.0","end-1c")
        

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
        newPatient = Patient(validUser,validPass,{})
        
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
        global mode
        
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        detailLabel = tk.Label(self, text = "Main Menu", font=('Montserrat',18), anchor='center',)
        detailLabel.grid(row=0,column=0,columnspan=2)
        
        aboutButton = tk.Button(self,text = "About", font=('Montserrat',10), anchor='center',command=lambda : messagebox.showinfo(title="About", message="Model Number : 22 \nSoftware Revision Number : 1\nDCM Serial Number : 21\nMcMaster University"))
        aboutButton.grid(row=1,column=0, pady = 20)
        
        aboutButton = tk.Button(self,text = "Egram Data", font=('Montserrat',10), anchor='center',command=lambda : messagebox.showinfo(title="Egram", message="Egram data will show once button is pressed"))
        aboutButton.grid(row=2,column=2, pady = 20)
        
        
        set_timeButton = tk.Button(self,text = "Set Date and Time", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(set_date_time))
        set_timeButton.grid(row=2,column=0, pady = 20)
        
        end_telementryButton = tk.Button(self,text = "End Telemetry", font=('Montserrat',10), anchor='center',command=lambda : messagebox.showinfo(title="Attention", message='Telementry session ended'))
        end_telementryButton .grid(row=3,column=0, pady = 20)
        
        newpatientButton = tk.Button(self,text = "Back", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(welcome_page))
        newpatientButton .grid(row=4,column=0, pady = 20)
        
        border = tk.Label(self,text = "|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|", font=('Montserrat',12), anchor='center')
        border.grid(row=1,column=1, rowspan=5,padx = 20)
        
        read_connection = tk.Label(self,text ='Device Not Connected',font=('Montserrat',10),anchor = 'center',fg = '#ff4500')
        read_connection.grid(row=4,column=2)
        
        parameterButton = tk.Button(self,text = "Change Parameters", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(parameters_page))
        parameterButton .grid(row=1,column=2, pady = 20,padx = 50)
        
    
        
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


class parameters_page(tk.Frame):
    # parent is needed for all widgets that are not the root tkinter window
    # controller allows for low coupling, frames can be accessed 
    # with accessing controller instead of frame directly
    def __init__(self, parent, controller):
        
        
        tk.Frame.__init__(self,parent, height=500,width=600)
        
       #below the parameters used in the various modes have been defined with their respective values 
        
    #1 Lower Rate Limit
        
        # label
        lower_rate = tk.Label(self,text = 'Lower Rate Limit', font = ('Montserrat',10),anchor = 'center')
        lower_rate.grid(row = 1, column = 0,sticky = 'w',pady =5,padx =40 )
        #input
        lower_rate_limit_val = ttk.Combobox(self, width = 5) 
        lower_rate_limit_val.grid(row = 1,column = 1,sticky ='W')
        #values
        lower_rate_limit_val['values'] = (30,35,40,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,
                                    80,81,82,83,84,85,86,87,88,89,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175) 
        lower_rate_limit_val.current(0)
       
    #2 Upper Rate Limit
        
        # label
        upper_rate = tk.Label(self,text = 'Upper Rate Limit', font = ('Montserrat',10),anchor = 'center')
        upper_rate.grid(row = 1, column = 2,sticky = 'w',pady =10,padx =40)
        # input
        upper_rate_limit_val = ttk.Combobox(self, width = 5) 
        upper_rate_limit_val.grid(row = 1,column = 3,sticky ='W') 
        # values
        upper_rate_limit_val['values'] = (50,55,60,65,70,75,80,85,90,95,100,105,110,115,
                                    120,125,130,135,140,145,150,155,160,165,170,175) 
        upper_rate_limit_val.current(0)    
        
    #3 Atrial Amplitude
        
        # label
        atrial_amp = tk.Label(self,text = 'Atrial Amplitude', font = ('Montserrat',10),anchor = 'center')
        atrial_amp.grid(row = 2, column = 0,sticky = 'w',pady =10,padx =40 )
        # input
        atrial_amplitude_val = ttk.Combobox(self, width = 5) 
        atrial_amplitude_val.grid(row = 2,column = 1,sticky ='W') 
        # values
        atrial_amplitude_val['values'] = (0,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,
                                     2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5) 
        atrial_amplitude_val.current(0)
        
    #4 Ventrical amplitude
        
        # label
        ventrical_amp = tk.Label(self,text = 'Ventrical Amplitude', font = ('Montserrat',10),anchor = 'center')
        ventrical_amp.grid(row = 2, column = 2,sticky = 'w',pady =10,padx =40)
        #input
        ventrical_amplitude_val = ttk.Combobox(self, width = 5) 
        ventrical_amplitude_val.grid(row = 2,column = 3,sticky ='W') 
        #values
        ventrical_amplitude_val['values'] = (0,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,
                                     2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5) 
        ventrical_amplitude_val.current(0)
        
    #5 Atrial Pulse
        
        # label
        atrial_puls = tk.Label(self,text = 'Atrial Pulse Width', font = ('Montserrat',10),anchor = 'center')
        atrial_puls.grid(row = 3, column = 0,sticky = 'w',pady =10,padx =40)
        #atrial pulse field input
        atrial_pulse_val = ttk.Combobox(self, width = 5) 
        atrial_pulse_val.grid(row = 3,column = 1,sticky ='W') 
        # Adding combobox drop down list 
        atrial_pulse_val['values'] = (0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9) 
        atrial_pulse_val.current(0)
        
    #6 Ventrical pulse width
    
        #Label
        ventrical_puls = tk.Label(self,text = 'Ventrical Pulse Width', font = ('Montserrat',10),anchor = 'center')
        ventrical_puls.grid(row = 3, column = 2,sticky = 'w',pady =10,padx =40 )
        
        # input
        ventrical_pulse_val = ttk.Combobox(self, width = 5) 
        ventrical_pulse_val.grid(row = 3,column = 3,sticky ='W') 
        # values  
        ventrical_pulse_val['values'] = (0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9) 
        ventrical_pulse_val.current(0)
        
    #7 Atrial Sensitivity
        
        # label
        atrial_sense = tk.Label(self,text = 'Atrial Sensitivity', font = ('Montserrat',10),anchor = 'center')
        atrial_sense.grid(row = 4, column = 0,sticky = 'w',pady =10,padx =40 )
        # input
        atrial_sensitivity_val = ttk.Combobox(self, width = 5) 
        atrial_sensitivity_val.grid(row = 4,column = 1,sticky ='W') 
        # values
        atrial_sensitivity_val['values'] = (0.25,0.5,0.75,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0) 
        atrial_sensitivity_val.current(0)
        
    #8 Ventrical Sensitivity

        # Label
        ventrical_sense = tk.Label(self,text = 'Ventrical Sensitivity', font = ('Montserrat',10),anchor = 'center')
        ventrical_sense.grid(row = 4, column = 2,sticky = 'w',pady =10,padx =40)
        # input
        ventrical_sensitivity_val  = ttk.Combobox(self, width = 5) 
        ventrical_sensitivity_val .grid(row = 4,column = 3,sticky ='W') 
        # values
        ventrical_sensitivity_val ['values'] = (0.25,0.5,0.75,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0) 
        ventrical_sensitivity_val .current(0)
        
    #9 ARP
        
        # label
        atrial_period = tk.Label(self,text = 'ARP', font = ('Montserrat',10),anchor = 'center')
        atrial_period.grid(row = 5, column = 0,sticky = 'w',pady =10 ,padx =40)
        # input
        arp_val = ttk.Combobox(self, width = 5) 
        arp_val .grid(row = 5,column =1,sticky ='W') 
        # values
        arp_val ['values'] = (150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500) 
        arp_val .current(0)    
       
    #10 VRP

        # label
        ventrical_period = tk.Label(self,text = 'VRP', font = ('Montserrat',10),anchor = 'center')
        ventrical_period.grid(row = 5, column = 2,sticky = 'w',pady =10 ,padx =40)
        # input
        vrp_val  = ttk.Combobox(self, width = 5) 
        vrp_val .grid(row = 5,column = 3,sticky ='W') 
        # values
        vrp_val ['values'] = (150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500) 
        vrp_val .current(0)
        
    #11 PVARP
    
        # label
        pvar_period = tk.Label(self,text = 'PVARP', font = ('Montserrat',10),anchor = 'center')
        pvar_period.grid(row = 6, column = 0,sticky = 'w',pady =10,padx =40)    
        # input
        pvarp_val  = ttk.Combobox(self, width = 5) 
        pvarp_val .grid(row = 6,column = 1,sticky ='W') 
        # values
        pvarp_val ['values'] = (150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500) 
        pvarp_val .current(0)
        
    #12 Maximum Sensor Rate 
        
        # label
        max_sens = tk.Label(self,text = 'Maximum Sensor Rate', font = ('Montserrat',10),anchor = 'center')
        max_sens.grid(row = 6, column = 2,sticky = 'w',pady =10,padx =40)
        # input
        max_sens_val = ttk.Combobox(self, width = 5) 
        max_sens_val.grid(row = 6,column = 3,sticky ='W') 
        # values
        max_sens_val['values'] = (50,55,60,65,70,75,80,85,90,95,100,105,110,115,
                                    120,125,130,135,140,145,150,155,160,165,170,175) 
        max_sens_val.current(0)
        
    #13 Hysteresis
        
        # Label
        hys_limit = tk.Label(self,text = 'Hysteresis', font = ('Montserrat',10),anchor = 'center')
        hys_limit.grid(row = 7, column = 0,sticky = 'w',pady =10 ,padx =40)
        # input
        hysteresis_val = ttk.Combobox(self, width = 5) 
        hysteresis_val.grid(row = 7,column = 1,sticky ='W') 
        # values
        hysteresis_val['values'] =(0,30,35,40,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,
                                     80,81,82,83,84,85,86,87,88,89,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175) 
        hysteresis_val.current(0)
        
    #14 Rate Smoothing
        
        # label
        rate_smoothing = tk.Label(self,text = 'Rate Smoothing', font = ('Montserrat',10),anchor = 'center')
        rate_smoothing.grid(row = 7, column = 2,sticky = 'w', pady =10,padx =40)
        # input
        rate_smoothing_val  = ttk.Combobox(self, width = 5) 
        rate_smoothing_val.grid(row = 7,column = 3,sticky ='W') 
        # values
        rate_smoothing_val['values'] =(0,3,6,9,12,15,18,21,25) 
        rate_smoothing_val.current(0)
        
    #15 Activity Threshold
    
        # label
        activity_thresh = tk.Label(self,text = 'Activity Threshold', font = ('Montserrat',10),anchor = 'center')
        activity_thresh.grid(row = 8, column = 0,sticky = 'w',pady =10,padx =40)    
        # input
        activity_thresh_val = ttk.Combobox(self, width = 5) 
        activity_thresh_val.grid(row = 8,column = 1,sticky ='W') 
        # values
        activity_thresh_val['values'] = ('V-Low','Low','Med-Low','Med','Med-High','High','V-High') 
        activity_thresh_val.current(0)
        
    #16 Reaction Time 
        
        # label
        react_time = tk.Label(self,text = 'Reaction Time ', font = ('Montserrat',10),anchor = 'center')
        react_time.grid(row = 8, column = 2,sticky = 'w',pady =10,padx =40)
        # input
        react_time_val = ttk.Combobox(self, width = 5) 
        react_time_val.grid(row = 8,column = 3,sticky ='W') 
        # values
        react_time_val['values'] = (10,20,30,40,50) 
        react_time_val.current(0)
        
    #17 Response Fcator
        
        # Label
        response_time = tk.Label(self,text = 'Response Fcator', font = ('Montserrat',10),anchor = 'center')
        response_time.grid(row = 9, column = 0,sticky = 'w',pady =10 ,padx =40)
        # input
        response_time_val = ttk.Combobox(self, width = 5) 
        response_time_val.grid(row = 9,column = 1,sticky ='W') 
        # values
        response_time_val['values'] =(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16) 
        response_time_val.current(0)
        
    #18 Recovery Time
        
        # label
        recovery_time = tk.Label(self,text = 'Recovery Time', font = ('Montserrat',10),anchor = 'center')
        recovery_time.grid(row = 9, column = 2,sticky = 'w', pady =10,padx =40)
        # input
        recovery_time_val = ttk.Combobox(self, width = 5) 
        recovery_time_val.grid(row = 9,column = 3,sticky ='W') 
        # values
        recovery_time_val['values'] =(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16) 
        recovery_time_val.current(0)
        
    # Pacing Mode's ComboBox
    
        dropdown = ttk.Combobox(self, width = 5)
        # pacing options 
        dropdown['values'] = ('AOO','AAI','VOO','VVI','AOOR','AAIR','VOOR','VVIR') 
        dropdown.grid(row = 0, column =0,sticky ='w',padx =40,pady =10)
        
        
        def parameter(e):
            
            # based on the mode selected the required parameter dropdowns are enabled and the rest are disabled
            
            if dropdown.get() == 'AOO':    
                
                atrial_amplitude_val.config(state = 'normal') 
                ventrical_amplitude_val.config(state = 'disabled')
                atrial_pulse_val.config(state = 'normal')
                ventrical_pulse_val.config(state = 'disabled')
                atrial_sensitivity_val.config(state = 'disabled')
                ventrical_sensitivity_val.config(state = 'disabled')
                arp_val.config(state = 'disabled')
                vrp_val.config(state = 'disabled')
                pvarp_val.config(state = 'disabled')
                max_sens_val.configure(state = 'disabled')
                hysteresis_val.config(state = 'disabled')
                rate_smoothing_val.config(state = 'disabled')
                activity_thresh_val.config(state = 'disabled')
                react_time_val.config(state = 'disabled')
                response_time_val.config(state = 'disabled')
                recovery_time_val.config(state = 'disabled')
                     
            elif dropdown.get() == 'AAI':
                
                atrial_amplitude_val.config(state = 'normal')
                ventrical_amplitude_val.config(state = 'disabled')
                atrial_pulse_val.config(state = 'normal')
                ventrical_pulse_val.config(state = 'disabled')
                atrial_sensitivity_val.config(state = 'normal')
                ventrical_sensitivity_val.config(state = 'disabled')
                arp_val.config(state = 'normal')
                vrp_val.config(state = 'disabled')
                pvarp_val.config(state = 'normal')
                max_sens_val.configure(state = 'disabled')
                hysteresis_val.config(state = 'normal')
                rate_smoothing_val.config(state = 'normal')
                activity_thresh_val.config(state = 'disabled')
                react_time_val.config(state = 'disabled')
                response_time_val.config(state = 'disabled')
                recovery_time_val.config(state = 'disabled')
               
            elif dropdown.get() == 'VOO':

               atrial_amplitude_val.config(state = 'disabled')
               ventrical_amplitude_val.config(state = 'normal')
               atrial_pulse_val.config(state = 'disabled')
               ventrical_pulse_val.config(state = 'normal')
               atrial_sensitivity_val.config(state = 'disabled')
               ventrical_sensitivity_val.config(state = 'disabled')
               arp_val.config(state = 'disabled')
               vrp_val.config(state = 'disabled')
               pvarp_val.config(state = 'disabled')
               max_sens_val.configure(state = 'disabled')
               hysteresis_val.config(state = 'disabled')
               rate_smoothing_val.config(state = 'disabled')
               activity_thresh_val.config(state = 'disabled')
               react_time_val.config(state = 'disabled')
               response_time_val.config(state = 'disabled')
               recovery_time_val.config(state = 'disabled')
               
                 
            elif dropdown.get() == 'VVI':
                
                atrial_amplitude_val.config(state = 'disabled')
                ventrical_amplitude_val.config(state = 'normal')
                atrial_pulse_val.config(state = 'disabled')
                ventrical_pulse_val.config(state = 'normal')
                atrial_sensitivity_val.config(state = 'disabled')
                ventrical_sensitivity_val.config(state = 'normal')
                arp_val.config(state = 'disabled')
                vrp_val.config(state = 'normal')
                pvarp_val.config(state = 'disabled')
                max_sens_val.configure(state = 'disabled')
                hysteresis_val.config(state = 'normal')
                rate_smoothing_val.config(state = 'normal')
                activity_thresh_val.config(state = 'disabled')
                react_time_val.config(state = 'disabled')
                response_time_val.config(state = 'disabled')
                recovery_time_val.config(state = 'disabled')
                
            elif dropdown.get() == 'AOOR':
                 
                 atrial_amplitude_val.config(state = 'normal')
                 ventrical_amplitude_val.config(state = 'disabled')
                 atrial_pulse_val.config(state = 'normal')
                 ventrical_pulse_val.config(state = 'disabled')
                 atrial_sensitivity_val.config(state = 'disabled')
                 ventrical_sensitivity_val.config(state = 'disabled')
                 arp_val.config(state = 'disabled')
                 vrp_val.config(state = 'disabled')
                 pvarp_val.config(state = 'disabled')
                 max_sens_val.configure(state = 'normal')
                 hysteresis_val.config(state = 'disabled')
                 rate_smoothing_val.config(state = 'disabled')
                 activity_thresh_val.config(state = 'normal')
                 react_time_val.config(state = 'normal')
                 response_time_val.config(state = 'normal')
                 recovery_time_val.config(state = 'normal')
                 
            elif dropdown.get() == 'AAIR':
                 
                atrial_amplitude_val.config(state = 'normal')
                ventrical_amplitude_val.config(state = 'disabled')
                atrial_pulse_val.config(state = 'normal')
                ventrical_pulse_val.config(state = 'disabled')
                atrial_sensitivity_val.config(state = 'normal')
                ventrical_sensitivity_val.config(state = 'disabled')
                arp_val.config(state = 'normal')
                vrp_val.config(state = 'disabled')
                pvarp_val.config(state = 'normal')
                max_sens_val.configure(state = 'normal')
                hysteresis_val.config(state = 'normal')
                rate_smoothing_val.config(state = 'normal')
                activity_thresh_val.config(state = 'normal')
                react_time_val.config(state = 'normal')
                response_time_val.config(state = 'normal')
                recovery_time_val.config(state = 'normal')
                 
            elif dropdown.get() == 'VOOR':
                 
                 atrial_amplitude_val.config(state = 'disabled')
                 ventrical_amplitude_val.config(state = 'normal')
                 atrial_pulse_val.config(state = 'disabled')
                 ventrical_pulse_val.config(state = 'normal')
                 atrial_sensitivity_val.config(state = 'disabled')
                 ventrical_sensitivity_val.config(state = 'disabled')
                 arp_val.config(state = 'disabled')
                 vrp_val.config(state = 'disabled')
                 pvarp_val.config(state = 'disabled')
                 max_sens_val.configure(state = 'normal')
                 hysteresis_val.config(state = 'disabled')
                 rate_smoothing_val.config(state = 'disabled')
                 activity_thresh_val.config(state = 'normal')
                 react_time_val.config(state = 'normal')
                 response_time_val.config(state = 'normal')
                 recovery_time_val.config(state = 'normal')
                 
            elif dropdown.get() == 'VVIR':
                 
                 atrial_amplitude_val.config(state = 'disabled')
                 ventrical_amplitude_val.config(state = 'normal')
                 atrial_pulse_val.config(state = 'disabled')
                 ventrical_pulse_val.config(state = 'normal')
                 atrial_sensitivity_val.config(state = 'disabled')
                 ventrical_sensitivity_val.config(state = 'normal')
                 arp_val.config(state = 'disabled')
                 vrp_val.config(state = 'normal')
                 pvarp_val.config(state = 'disabled')
                 max_sens_val.configure(state = 'normal')
                 hysteresis_val.config(state = 'normal')
                 rate_smoothing_val.config(state = 'normal')
                 activity_thresh_val.config(state = 'normal')
                 react_time_val.config(state = 'normal')
                 response_time_val.config(state = 'normal')
                 recovery_time_val.config(state = 'normal')
                 
            else:
                pass
            
        #bind the dropdown menu to parameter function
        dropdown.bind("<<ComboboxSelected>>",parameter)
        
        def get_val():
            
            # the value stored in the dropdowns is taken and displayed on the python console 
            if dropdown.get() =='AOO':
                parameter = {'Mode' : 'AOO','LRL':lower_rate_limit_val.get(),'URL':upper_rate_limit_val.get(),'AA':atrial_amplitude_val.get(),'AP':atrial_pulse_val.get()}
                print(parameter)      
                
            elif dropdown.get() =='AAI':
                parameter = {'Mode' : 'AAI','LRL':lower_rate_limit_val.get(),'URL':upper_rate_limit_val.get(),'AA':atrial_amplitude_val.get(),'AP':atrial_pulse_val.get(),'AS':atrial_sensitivity_val.get(),'ARP':arp_val.get(),'PVARP':pvarp_val.get(),'H':hysteresis_val.get(),'RS':rate_smoothing_val.get()}
                print(parameter)
                
            elif dropdown.get() =='VOO':
                parameter = {'Mode' : 'VOO','LRL':lower_rate_limit_val.get(),'URL':upper_rate_limit_val.get(),'VA':ventrical_amplitude_val.get(),'VP':ventrical_pulse_val.get()}
                print(parameter)
            
            elif dropdown.get() =='VVI':   
                parameter = {'Mode' : 'VVI','LRL':lower_rate_limit_val.get(),'URL':upper_rate_limit_val.get(),'VA':ventrical_amplitude_val.get(),'VP':ventrical_pulse_val.get(),'VS':ventrical_sensitivity_val.get(),'VRP':vrp_val.get(),'H':hysteresis_val.get(),'RS':rate_smoothing_val.get()}
                print(parameter)
                
            elif dropdown.get() =='AOOR':
                parameter = {'Mode' : 'AOO','LRL':lower_rate_limit_val.get(),'URL':upper_rate_limit_val.get(),'MSR':max_sens_val.get(),'AA':atrial_amplitude_val.get(),'AP':atrial_pulse_val.get(),'AT': activity_thresh_val.get(),'RT':react_time_val.get(),'RspT':response_time_val.get(),'RecT':recovery_time_val.get()}
                print(parameter)      
                
            elif dropdown.get() =='AAIR':
                parameter = {'Mode' : 'AAI','LRL':lower_rate_limit_val.get(),'URL':upper_rate_limit_val.get(),'MSR':max_sens_val.get(),'AA':atrial_amplitude_val.get(),'AP':atrial_pulse_val.get(),'AS':atrial_sensitivity_val.get(),'ARP':arp_val.get(),'PVARP':pvarp_val.get(),'H':hysteresis_val.get(),'RS':rate_smoothing_val.get(),'AT': activity_thresh_val.get(),'RT':react_time_val.get(),'RspT':response_time_val.get(),'RecT':recovery_time_val.get()}
                print(parameter)
                
            elif dropdown.get() =='VOOR':
                parameter = {'Mode' : 'VOO','LRL':lower_rate_limit_val.get(),'URL':upper_rate_limit_val.get(),'MSR':max_sens_val.get(),'VA':ventrical_amplitude_val.get(),'VP':ventrical_pulse_val.get(),'AT': activity_thresh_val.get(),'RT':react_time_val.get(),'RspT':response_time_val.get(),'RecT':recovery_time_val.get()}
                print(parameter)
            
            elif dropdown.get() =='VVIR':   
                parameter = {'Mode' : 'VVI','LRL':lower_rate_limit_val.get(),'URL':upper_rate_limit_val.get(),'MSR':max_sens_val.get(),'VA':ventrical_amplitude_val.get(),'VP':ventrical_pulse_val.get(),'VS':ventrical_sensitivity_val.get(),'VRP':vrp_val.get(),'H':hysteresis_val.get(),'RS':rate_smoothing_val.get(),'AT': activity_thresh_val.get(),'RT':react_time_val.get(),'RspT':response_time_val.get(),'RecT':recovery_time_val.get()}
                print(parameter)
                
            else:
                messagebox.showinfo(title="Error", message="Choose a pacing mode on the top left corner")

      
        saveButton = tk.Button(self,text = "Save", font=('Montserrat',10), anchor='center',command=lambda :get_val())
        saveButton.grid(row=0,column=2, pady = 10)
        
        backButton = tk.Button(self,text = "Back", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
        backButton.grid(row=0,column=3, pady = 10)



def main():
    patient.createPD()
    pacemakerApp = mainWindow()
    pacemakerApp.mainloop()
    
    
if __name__ == '__main__':
    main()
