# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain
import time, json
import serial
from statistics import median
# Import the ADS1x15 module.
import Adafruit_ADS1x15

class Params:
    def __init__(self):
        self.uart = 'uart.txt'
        self.adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)
        self.adc2 = Adafruit_ADS1x15.ADS1015()
        self.GAIN = 1
        self.Xs = (207.0,419.0,619.0,824.0,1032.0,1241.0,1444.0,1649.0)
    
    def continousRead(self):
        print('Reading ADS1x15 values, press Ctrl-C to quit...')
        # Print nice channel column headers.
        print('| {0:10d} | {1:10d} | {2:10d} | {3:10d} | {0:10d} | {1:10d} | {2:10d} | {3:10d} |'.format(*range(8)))
        print('-' * 53*2)
        # Main loop.
        while True:
            # Read all the ADC channel values in a list.
            values = [0]*8
    
            values[0] = (self.adc.read_adc(0, gain=self.GAIN)/(8.0*self.Xs[0])*4096)
            values[1] = (self.adc.read_adc(1, gain=self.GAIN)/(8.0/2.0*self.Xs[1])*4096)
            values[2] = (self.adc.read_adc(2, gain=self.GAIN)/(8.0/3.0*self.Xs[2])*512)
            values[3] = (self.adc.read_adc(3, gain=self.GAIN)/(8.0/4.0*self.Xs[3])*512)
            values[4] = (self.adc2.read_adc(0, gain=self.GAIN)/(8.0/5.0*self.Xs[4])*100)
            values[5] = (self.adc2.read_adc(1, gain=self.GAIN)/(8.0/6.0*self.Xs[5])*360)
            values[6] = ((self.adc2.read_adc(2, gain=self.GAIN)/(8.0/7.0*self.Xs[6])*180)-90)
            values[7] = ((self.adc2.read_adc(3, gain=self.GAIN)/(8.0/8.0*self.Xs[7])*360)-180)
    
    
            # Print the ADC values.
            print('| {0:10.8f} | {1:10.8f} | {2:10.8f} | {3:10.8f} | {4:10.8f} | {5:10.8f} | {6:10.8f} | {7:10.8f} |'.format(*values))
            # Pause for half a second.
            time.sleep(0.2)

    def singleRead(self):
        values = [0] * 9
        file = open(self.uart, 'r')

        values[0] = (self.adc.read_adc(0, gain=self.GAIN) / (8.0 * self.Xs[0]) * 4096)
        values[1] = (self.adc.read_adc(1, gain=self.GAIN) / (8.0 / 2.0 * self.Xs[1]) * 4096)
        values[2] = (self.adc.read_adc(2, gain=self.GAIN) / (8.0 / 3.0 * self.Xs[2]) * 512)
        values[3] = (self.adc.read_adc(3, gain=self.GAIN) / (8.0 / 4.0 * self.Xs[3]) * 512)
        values[4] = (self.adc2.read_adc(0, gain=self.GAIN) / (8.0 / 5.0 * self.Xs[4]) * 100)
        values[5] = (self.adc2.read_adc(1, gain=self.GAIN) / (8.0 / 6.0 * self.Xs[5]) * 360)
        values[6] = ((self.adc2.read_adc(2, gain=self.GAIN) / (8.0 / 7.0 * self.Xs[6]) * 180) - 90)
        values[7] = ((self.adc2.read_adc(3, gain=self.GAIN) / (8.0 / 8.0 * self.Xs[7]) * 360) - 180)
        values[8] = file.read()

        file.close()
        return json.dumps(values)

    def singleSteadyRead(self):
        values = [0] * 9
        params = [0] * 9
        for value in values:
            value = [0] * 10

        file = open(self.uart, 'r')

        for i in range(0, 10):
            values[0][i] = (self.adc.read_adc(0, gain=self.GAIN) / (8.0 * self.Xs[0]) * 4096)
            values[1][i] = (self.adc.read_adc(1, gain=self.GAIN) / (8.0 / 2.0 * self.Xs[1]) * 4096)
            values[2][i] = (self.adc.read_adc(2, gain=self.GAIN) / (8.0 / 3.0 * self.Xs[2]) * 512)
            values[3][i] = (self.adc.read_adc(3, gain=self.GAIN) / (8.0 / 4.0 * self.Xs[3]) * 512)
            values[4][i] = (self.adc2.read_adc(0, gain=self.GAIN) / (8.0 / 5.0 * self.Xs[4]) * 100)
            values[5][i] = (self.adc2.read_adc(1, gain=self.GAIN) / (8.0 / 6.0 * self.Xs[5]) * 360)
            values[6][i] = ((self.adc2.read_adc(2, gain=self.GAIN) / (8.0 / 7.0 * self.Xs[6]) * 180) - 90)
            values[7][i] = ((self.adc2.read_adc(3, gain=self.GAIN) / (8.0 / 8.0 * self.Xs[7]) * 360) - 180)

        params[0] = median(values[0])
        params[1] = median(values[1])
        params[2] = median(values[2])
        params[3] = median(values[3])
        params[4] = median(values[4])
        params[5] = median(values[5])
        params[6] = median(values[6])
        params[7] = median(values[7])
        params[8] = file.read()

        file.close()
        return json.dumps(params)

    def readUart(self):
        with serial.Serial("/dev/serial0", 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE) as ser:

            while True:
                data = ser.read(5)
                file = open(self.uart, 'w')
                file.write(data)
                file.close()
                time.sleep(0.05)

        return data

