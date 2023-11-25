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


# Use struct to convert between python values and C structs represented as Python Strings
# Convert to binary values using struct.pack()
# "B" gives unsigned char
# 'b' gives signed char
def main():
    
    with serial.Serial(port_val,baudrate=115200,timeout=1) as ser:
        # ser.write(sync + set_param + red_enable + green_enable + blue_enable + off_time + switch_time) 
        #ser.write(b'\x16\x55' + b'\x00' + struct.pack("B",1) + b'\x00'*7)
        # ser.write(b'\x16\x22' + b'\x00' + struct.pack("B",1) + b'\x00'*7)
        #sleep(0.1)
        testVals = b'\x16\x22' + b'\x00'*9
        ser.write(testVals)

        print(testVals.hex())
        sleep(20)
        vals = ser.read(9)
        print(vals)
        #bytesToRead = ser.inWaiting()
        
        
    
if __name__ == "__main__":
    main()
