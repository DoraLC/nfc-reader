import serial

def readuid(brate):
    ser =serial.Serial('/dev/ttyUSB0', brate, timeout = 1)
    uid = ser.readline()
    return uid if len(uid)!=0 else None
