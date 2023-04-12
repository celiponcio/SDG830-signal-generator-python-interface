##!/usr/bin/python
# this is a literal interface to the SCPI Language of the SDG830 signal generator (see the programming manual)
# quite presumably will work with others of the same family
# usage: sudo ./SDG830.py "OUTP ON" # sudo mey or may not be needed, depending on the file mode of (probably) /dev/usbtmc1
# tested commands (C1: seems to be not needed in this model and case seems to be ignored
# "ARWV INDEX, 50"  (set user-defined wave #1)
# ARWV?
# "OUTP OFF"
# "OUTP ON"
# OUTP?
# "VKEY VALUE,9,STATE,1" (can be abbreviated to just "9")
# 9 28 49 50 51 52 18 (select ARB and set freq to 1234Hz
# 9 23 49 28 (select ARB and set AMPL to 1Vpp

import pyvisa as pyvisa
import sys, time

delay = 1 # delay between commands

rm = pyvisa.ResourceManager('@py')
#print(rm.list_resources())
my_instrument = rm.open_resource('USB0::62701::60986::NDG08CBQ4R0189::0::INSTR') # copy here the output of the previous commadn or use pyvisa-shell to find out
print(my_instrument)
my_instrument.write('CHDR LONG'); # time.sleep(delay) # solves query problems from crash to warning
# try pyvisa-shell or See https://github.com/pyvisa/pyvisa-py/issues/20
#print(my_instrument.query('*IDN?')); time.sleep(delay) # long-answer queries seem to trigger a warning

for i in range(len(sys.argv)-1):
    time.sleep(delay) # separate commands in time or the second will fail
    s = str(sys.argv[i+1])
    print(s)
    if s.find('?') > -1:
        print(my_instrument.query(s))
    elif s.isdigit(): # keycode
        my_instrument.write('VKEY VALUE,' + s + ',STATE,1')
        time.sleep(10) # this command requires particularly long delay
    else:
        my_instrument.write(s)

my_instrument.close()
