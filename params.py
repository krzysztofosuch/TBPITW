# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain
import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15


# Create an ADS1115 ADC (16-bit) instance.
#adc = Adafruit_ADS1x15.ADS1115()

# Or create an ADS1015 ADC (12-bit) instance.
adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
adc2 = Adafruit_ADS1x15.ADS1015()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

Xs = (207.0,419.0,619.0,824.0,1032.0,1241.0,1444.0,1649.0)

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} | {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(8)))
print('-' * 37*2)
# Main loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*8

    values[0] = (adc.read_adc(0, gain=GAIN)/(8*Xs[0]))*4096
    values[1] = (adc.read_adc(1, gain=GAIN)/(4*Xs[1]))*4096
    values[2] = (adc.read_adc(2, gain=GAIN)/(60/25*Xs[2]))*512
    values[3] = (adc.read_adc(3, gain=GAIN)/(15/8*Xs[3]))*512
    values[4] = (adc2.read_adc(0, gain=GAIN)/(60/39*Xs[4]))*100
    values[5] = (adc2.read_adc(1, gain=GAIN)/(30/23*Xs[5]))*360
    values[6] = ((adc2.read_adc(2, gain=GAIN)/(60/53*Xs[6]))*180)-90
    values[7] = ((adc2.read_adc(3, gain=GAIN)/(3/15.0*Xs[7]))*360)-180
    
    # Print the ADC values.
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} | {4:>6} | {5:>6} | {6:>6} | {7:>6} |'.format(*values))
    # Pause for half a second.
    time.sleep(0.5)
