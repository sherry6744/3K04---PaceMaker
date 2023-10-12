# Notes on Running...
# Python 3.12
# Please install Pillow with the following commands in terminal
# python -m pip install --upgrade pip
# python -m pip install --upgrade Pillow
# Download pacemaker.jpg from github and change directory in line 72 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from patient import Patient
import patient
from parameters import *
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
        
        for pageNum in (welcome_page,user_page,main_page,AOO_page,AAI_page,VOO_page,VVI_page):
            page = pageNum(base,self)
            self.pages[pageNum] = page
            page.grid(row = 0, column = 0, stick="nsew")
        
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
    
#### WELCOME PAGE ####
class welcome_page(tk.Frame):
    # parent is needed for all widgets that are not the root tkinter window
    # controller allows for low coupling, frames can be accessed 
    # with accessing controller instead of frame directly
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        # Main frame | Contains Title, Login prompt, and User/Pass grid
        
        # Import Media
        #image1 = Image.open(r"C:\Users\aggar\OneDrive\Desktop\Mcmaster\Sem 5\3K04\3K04---PaceMaker\pacemaker.png") #Fix to make locally stored in same location as patient info
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
        
        aboutButton = tk.Button(self,text = "About", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
        aboutButton.grid(row=1,column=0, pady = 20)
        
        set_timeButton = tk.Button(self,text = "Set Date and Time", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
        set_timeButton.grid(row=2,column=0, pady = 20)
        
        end_telementryButton = tk.Button(self,text = "End Telemetry", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
        end_telementryButton .grid(row=3,column=0, pady = 20)
        
        newpatientButton = tk.Button(self,text = "New Patient", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(welcome_page))
        newpatientButton .grid(row=4,column=0, pady = 20)
        
        border = tk.Label(self,text = "|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|", font=('Montserrat',12), anchor='center')
        border.grid(row=1,column=1, rowspan=5,padx = 20)
        
        read_connection = tk.Label(self,text ='Device Not Connected',font=('Montserrat',10),anchor = 'center',fg = '#ff4500')
        read_connection.grid(row=5,column=3)
        
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
        
                

class AOO_page(tk.Frame):
    # parent is needed for all widgets that are not the root tkinter window
    # controller allows for low coupling, frames can be accessed 
    # with accessing controller instead of frame directly
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        #1 shows label and entry box for lower rate limit
        lower_rate_limit_val = lower_rate_limit(self)
        #2 shows label and entry box for upper rate limit
        upper_rate_limit_val = upper_rate_limit(self)
        #3 shows label and entry box for atrial amplitude
        atrial_amplitude_val = atrial_amplitude(self)
        #4 shows label and entry box for Atrial pulse
        atrial_pulse_val = atrial_pulse(self)
        
        #no functionality
        saveButton = tk.Button(self,text = "Save", font=('Montserrat',10), anchor='center',command=lambda : print({'LRL':lower_rate_limit_val,'URL':upper_rate_limit_val,'AA':atrial_amplitude_val,'AP':atrial_pulse_val}))
        saveButton.grid(row=1,column=0, pady = 10)
        
        backButton = tk.Button(self,text = "Back", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
        backButton.grid(row=2,column=0, pady = 10)
        
       # return {'LRL':lower_rate_limit_val,'URL':upper_rate_limit_val,'AA':atrial_amplitude_val,'AP':atrial_pulse_val}

        
class VOO_page(tk.Frame):
    # parent is needed for all widgets that are not the root tkinter window
    # controller allows for low coupling, frames can be accessed 
    # with accessing controller instead of frame directly
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, height=500,width=600)
        
        #1 shows label and entry box for lower rate limit
        lower_rate_limit_val = lower_rate_limit(self)
        #2 shows label and entry box for upper rate limit
        upper_rate_limit_val = upper_rate_limit(self)
        #3 shows label and entry box for Ventrical amplitude
        ventrical_amplitude_val = ventrical_amplitude(self)
        #4 shows label and entry box for Ventrical pulse
        ventrical_pulse_val = ventrical_pulse(self)
        
        #no functionality
        saveButton = tk.Button(self,text = "Save", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
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
        lower_rate_limit_val = lower_rate_limit(self)
        #2 shows label and entry box for upper rate limit
        upper_rate_limit_val = upper_rate_limit(self)
        #3 shows label and entry box for atrial amplitude
        atrial_amplitude_val = atrial_amplitude(self)
        #4 shows label and entry box for Atrial pulse
        atrial_pulse_val = atrial_pulse(self)
        #5 shows label and entry box for atrial sensitivity
        atrial_sensitivity_val = atrial_sensitivity(self)
        #6 shows label and entry box for ARP
        arp_val = arp(self)
        #7 shows label and entry box for PVARP
        pvarp_val = pvarp(self)
        #8 shows label and entry box for Hysteresis
        hysteresis_val = hysteresis(self)
        #9 shows label and entry box for Rate Smoothing
        rate_smoothing_val = rate_smoothing(self)
        
        #no functionality
        saveButton = tk.Button(self,text = "Save", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
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
        lower_rate_limit_val = lower_rate_limit(self)
        #2 shows label and entry box for upper rate limit
        upper_rate_limit_val = upper_rate_limit(self)
        #3 shows label and entry box for Ventrical amplitude
        ventrical_amplitude_val = ventrical_amplitude(self)
        #4 shows label and entry box for Ventrical pulse
        ventrical_pulse_val = ventrical_pulse(self)
        #5 shows label and entry box for atrial sensitivity
        ventrical_sensitivity_val = ventrical_sensitivity(self)
        #6 shows label and entry box for ARP
        vrp_val = vrp(self)
        #7 shows label and entry box for Hysteresis
        hysteresis_val = hysteresis(self)
        #8 shows label and entry box for Rate Smoothing
        rate_smoothing_val = rate_smoothing(self)
        
        #no functionality
        saveButton = tk.Button(self,text = "Save", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
        saveButton.grid(row=1,column=0, pady = 10)
        
        backButton = tk.Button(self,text = "Back", font=('Montserrat',10), anchor='center',command=lambda : controller.display_page(main_page))
        backButton.grid(row=2,column=0, pady = 10)



def main():
    patient.createPD()
    pacemakerApp = mainWindow()
    pacemakerApp.mainloop()
    
    
if __name__ == '__main__':
    main()
