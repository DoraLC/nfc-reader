import readCard

while True:
    reading = readCard.readuid(9600)
    if reading != None:
        print(reading)