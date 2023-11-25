#SERIAL COMMUNICATION 
#ASSIGNMENT 2
import serial
import struct
from time import sleep
import os.path
import csv
import pandas as pd
import global_vars
pd.options.mode.chained_assignment = None  # default='warn'

# Use the following command to check your computer ports
# python -m serial.tools.list_ports

# Might need to change this depending on your computer ports
port_val = 'COM5'
sync = b'\x16' # Needed to send data
echo_param = b'\x22' # Needed to echo data
set_param = b'\x55' # Needed to set parameters


# Use struct to convert between python values and C structs represented as Python Strings
# Convert to binary values using struct.pack()
# "B" gives unsigned char
# 'b' gives signed char
# Sending a total of 46 bytes of data , calculations in notebook and matches matlab code
def write_param(user):
    with open('patientData.csv', 'r') as csvfile:
        userName = pd.read_csv(csvfile, delimiter=' ')
        col_1 = userName['Username']
        col_3 = userName['Parameters']
        parseRow = 0
        params_dict = {}
        for patients in range(col_1.size):
                    if(user != str(col_1.values[patients])):
                        continue
                    if(user == str(col_1.values[patients])):
                        if str(col_3.values[patients]) == "nan":
                            print("not loading values.")
                        elif str(col_3.values[patients]) != "null":
                            #print("Loading Values...")
                            # Example of CSV data: "{'Mode': 'VOO', 'LRL': '30', 'URL': '50', 'MSR': 0, 'AA': 0, 'AP': 0, 'AS': 0, 'ARP': 0, 'VA': '0', 'VP': '1', 'VS': 0, 'VRP': 0, 'PVARP': 0, 'H': 0, 'RS': 0, 'AT': 0, 'RT': 0, 'RspT': 0, 'RecT': 0}"
                            params = col_3.values[patients]
                            # Converting to dictionary
                            params_dict = eval(params)
                            #print(params_dict)
                            MODE = struct.pack("H",int(params_dict['Mode']))
                            LOWER_RATE_LIMIT = struct.pack("H",int(params_dict['LRL']))
                            #UPPER_RATE_LIMIT = struct.pack("H",int(parameter['URL']))
                            MAX_SENS_RATE = struct.pack("H",int(params_dict['MSR']))
                            ATR_AMP = struct.pack("f",float(params_dict['AA']))
                            ATR_PW = struct.pack("f",float(params_dict['AP']))
                            ATR_SENS = struct.pack("f",float(params_dict['AS']))
                            ARP = struct.pack("H",int(params_dict['ARP']))
                            VENT_AMP = struct.pack("f",float(params_dict['VA']))
                            VENT_PW = struct.pack("f",float(params_dict['VP']))
                            VENT_SENS = struct.pack("f",float(params_dict['VS']))
                            VRP = struct.pack("H",int(params_dict['VRP']))
                            PVARP = struct.pack("H",int(params_dict['PVARP']))
                            #HYES = struct.pack("H",int(parameter['H']))
                            #RATE_SMO = struct.pack("H",int(parameter['RS']))
                            ACTIVITY_THRES = struct.pack("H",int(params_dict['AT']))
                            RECOV_TIME = struct.pack("H",int(params_dict['RT']))
                            RESPOND_FACTOR = struct.pack("H",int(params_dict['RspT']))
                            REACTION_TIME = struct.pack("H",int(params_dict['RecT']))
            
    with serial.Serial(port_val,baudrate=115200,timeout=1) as ser:
        if(params_dict != {}):
            print("Mode: ", MODE)
            print("LOWER_RATE_LIMIT: " , LOWER_RATE_LIMIT)
            print("MAX_SENS_RATE: " , MAX_SENS_RATE)
            print("ATR_AMP: " , ATR_AMP)
            print("ATR_PW: " , ATR_PW)
            print("ATR_SENS: " , ATR_SENS)
            print("ARP: " , ARP)
            print("VENT_AMP: " , VENT_AMP)
            print("VENT_PW: " , VENT_PW)
            print("VENT_SENS: " , VENT_SENS)
            print("VRP: " , VRP)
            print("PVARP: " , PVARP)
            print("ACTIVITY_THRES: " , ACTIVITY_THRES)
            print("RECOV_TIME: ",  RECOV_TIME)
            print("RESPOND_FACTOR: " , RESPOND_FACTOR)
            print("REACTION_TIME: " , REACTION_TIME)
            param_send = sync + set_param + MODE + LOWER_RATE_LIMIT +  MAX_SENS_RATE + ATR_AMP + ATR_PW + ATR_SENS + ARP + VENT_AMP + VENT_PW + VENT_SENS + VRP + PVARP + ACTIVITY_THRES + RECOV_TIME + RESPOND_FACTOR + REACTION_TIME
            #ser.write(param_send) 
            
            print(param_send)
            ser.write(param_send)
            #print(param_send.hex())
            #print(param_send)
            ser.close()
        else:
            print("No Data")
        
def read_param():
    
        with serial.Serial(port_val,baudrate=115200,timeout=1) as ser:
            echo = sync + echo_param
            # Need to write the command that enables the reading of data which is sent to transmitter
            ser.write(echo)
            #print(echo)
            sleep(20)
            vals = ser.read(46)
            #print(vals)
            #bytesToRead = ser.inWaiting()
            ser.close()
            
        
        
