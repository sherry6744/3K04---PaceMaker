#SERIAL COMMUNICATION TEST
import serial
import struct
from time import sleep

# Use the following command to check your computer ports
# python -m serial.tools.list_ports

# Might need to change this depending on your computer ports
port_val = 'COM5'
sync = '0x16' # Needed to send data
echo_param = b'\x22' # Needed to echo data
set_param = b'\x55' # Needed to set parameters
sync_set = b'\x16\x22'
red_enable = struct.pack("B",0)
green_enable = struct.pack("B",0)
blue_enable = struct.pack("B",1)
off_time = struct.pack("f",0.9)
switch_time = struct.pack("H",400)

#parameter = {'Mode' : 'VVIR','LRL':0,'URL':0,'MSR':0,'AA':0,'AP':0,'AS':0,'ARP':0,'VA':0,'VP':0,'VS':0,'VRP':0,
#             'PVARP':0,'H':0,'RS':0,'AT': 0,'RT':0,'RspT':0,'RecT':0}


MODE = struct.pack("H",parameter['Mode'])
LOWER_RATE_LIMIT = struct.pack("H",parameter['LRL'])
#UPPER_RATE_LIMIT = struct.pack("H",parameter['URL'])
MAX_SENS_RATE = struct.pack("H",parameter['MSR'])
ATR_AMP = struct.pack("f",parameter['AA'])
ATR_PW = struct.pack("f",parameter['AP'])
ATR_SENS = struct.pack("f",parameter['AS'])
ARP = struct.pack("H",parameter['ARP'])
VENT_AMP = struct.pack("f",parameter['VA'])
VENT_PW = struct.pack("f",parameter['VP'])
VENT_SENS = struct.pack("f",parameter['VS'])
VRP = struct.pack("H",parameter['VRP'])
PVARP = struct.pack("H",parameter['PVARP'])
#HYES = struct.pack("H",parameter['H'])
#RATE_SMO = struct.pack("H",parameter['RS'])
ACTIVITY_THRES = struct.pack("H",parameter['AT'])
RECOV_TIME = struct.pack("H",parameter['RT'])
RESPOND_FACTOR = struct.pack("H",parameter['RspT'])
REACTION_TIME = struct.pack("H",parameter['RecT'])


# Use struct to convert between python values and C structs represented as Python Strings
# Convert to binary values using struct.pack()
# "B" gives unsigned char
# 'b' gives signed char
def main():
    with serial.Serial(port_val,baudrate=115200) as ser:
        # ser.write(sync + set_param + red_enable + green_enable + blue_enable + off_time + switch_time) 
        # ser.write(sync + set_param + MODE + LOWER_RATE_LIMIT +  MAX_SENS_RATE + ATR_AMP + ATR_PW + ATR_SENS + ARP + VENT_AMP + VENT_PW + VENT_SENS + VRP + PVARP + ACTIVITY_THRES + RECOV_TIME + RESPOND_FACTOR + REACTION_TIME  + off_time + switch_time) 
        ser.write(b'\x16\x55' + b'\x00' + struct.pack("B",1) + b'\x00'*7)
        #sleep(0.1)
    
    
if __name__ == "__main__":
    main()
    

