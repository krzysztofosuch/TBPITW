import serial

with serial.Serial ("/dev/serial0", 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE) as ser:
    print('connected')

    print(ser.is_open)
    #ser.baudrate = 9600                     #Set baud rate to 9600
#    ser.write([0xb4, 0x00, 0x00, 0x20, 0xb4])
    #ser.write(0x01)
 #   print('data sent')

    data = []

    for i in range (1,100):
        #data.append(ser.read(5))                     #Read ten characters from serial port to data
        print(ser.read(5))                     #Read ten characters from serial port to data
        #print(data)

#ser.close() 
