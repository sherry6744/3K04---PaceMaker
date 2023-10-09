### PATIENT FILE ###
import os.path
import csv

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
        with open('patientData.csv', 'w', newline='') as csvfile:
            patientInfo = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            patientInfo.writerow(['Username', 'Password'])
            
def addPatient(patientObj):
    with open('patientData.csv', 'a') as csvfile:
            patientInfo = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            patientInfo.writerow([str(patientObj.username), str(patientObj.password)])