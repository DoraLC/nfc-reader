import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)

while True:
    uid = ser.readline()

    if len(uid) != 0:
        print(uid)