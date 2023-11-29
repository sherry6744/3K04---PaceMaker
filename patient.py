### PATIENT FILE ###
import os.path
import csv
import pandas as pd
import global_vars
pd.options.mode.chained_assignment = None  # default='warn'


## PATIENT OBJECT
class Patient:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def __str__(self):
        return "Username is % s, " \
        "Password is % s" % (self.username, self.password)
       
## CREATE PATIENT DATA CSV FILE 
def createPD():
    dataPath = './patientData.csv'
    checkFile = os.path.exists(dataPath)
    if(checkFile == False):
        with open('patientData.csv', 'w',newline='') as csvfile:
            patientInfo = csv.writer(csvfile, delimiter=' ')
            patientInfo.writerow(['Username', 'Password', 'Parameters'])
    
## ADDS NEW VALID PATIENT TO CSV
def addPatient(patientObj):
    with open('patientData.csv', 'a', newline='') as csvfile:
        patientInfo = csv.writer(csvfile, delimiter=' ')
        patientInfo.writerow([str(patientObj.username), str(patientObj.password), "null"])
    print(availUsers())

## VALIDATES UNIQUE USERNAME       
def uniqueUser(patientObj):
    with open('patientData.csv', 'r') as csvfile:
        userName = pd.read_csv(csvfile, delimiter=' ')
        print(userName.columns.tolist()) 
        col = userName['Username'].tolist()
        for users in col:
            if(patientObj.username == users):
                return False
        return True

## CONFIRMS USERNAME/PASSWORD LOGIN IS CORRECT
def loginUser(userInput,passInput):
    with open('patientData.csv', 'r') as csvfile:
        patientVals = pd.read_csv(csvfile, delimiter=' ')
        col_1 = patientVals['Username']
        col_2 = patientVals['Password']
    for patients in range(col_1.size):
         if(userInput != str(col_1.values[patients])):
             continue
         if(userInput == str(col_1.values[patients])):
             if(passInput == str(col_2.values[patients])):
                global_vars.curr_user = userInput
                return(2)
             else:
                return(1)
    return(0)

## DETERMINE IF MAX USER NUMBER REACHED
def availUsers():
    with open('patientData.csv', 'r') as csvfile:
        userName = pd.read_csv(csvfile, delimiter=' ') 
        col = userName['Username']
    return int(10-col.size)



## SAVE DATA TO CSV
def saveParams(param_vals, user):
    with open('patientData.csv', 'r') as csvfile:
        userName = pd.read_csv(csvfile, delimiter=' ')
        col_1 = userName['Username']
        col_2 = userName['Password']
        col_3 = userName['Parameters']
        parseRow = 0
        for patients in range(col_1.size):
            if(user != str(col_1.values[patients])):
                continue
            if(user == str(col_1.values[patients])):
                print("Patient " + str(user) + " found on line " + str(patients+2) + " in database. This is user number " + str(patients+1))
                print("Note that Username and Password are on the 1st row of the database. First user begins on 2nd line.")
                parseRow = patients+2
                print(parseRow)
                userName['Parameters'][patients] = pd.to_numeric(['Parameters'], errors='coerce')
                userName = userName.fillna("null")
                userName['Parameters'][patients] = param_vals
                userName.to_csv('patientData.csv', index=False, sep=" ")
                
## LOAD USER SAVED PARAMETERS
def set_val(user):
    with open('patientData.csv', 'r') as csvfile:
        userName = pd.read_csv(csvfile, delimiter=' ')
        col_1 = userName['Username']
        col_2 = userName['Password']
        col_3 = userName['Parameters']
        user_params = ""
        print(global_vars.curr_user)
        print("test"+ col_3.values[0])
        parseRow = 0
        #print(userName['Parameters'][patients])
        for patients in range(col_1.size):
            if(user != str(col_1.values[patients])):
                continue
            if(user == str(col_1.values[patients])):
                if str(col_3.values[patients]) == "nan":
                    print("not loading values.")
                elif str(col_3.values[patients]) != "null":
                    print("Loading Values...")
                    user_params = col_3.values[patients]
                    print(type(user_params))
                    
        return user_params
                 
                
                
                
