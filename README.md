This is a literal interface to the SCPI Language of the SDG830 signal generator (see the programming manual)   
Quite presumably will work with others of the same family.  
The ID of the specific device must be inserted in the code. Instructions on the source file.  
Usage: sudo ./SDG830.py ["command string" | keycode list]  # sudo may or may not be needed, depending on the file mode of (probably) /dev/usbtmc1  
Tested commands (C1: seems to be not needed in this model and case seems to be ignored)  
"ARWV INDEX, 50"  (set user-defined wave #1)  
ARWV?  
"OUTP OFF"  
"OUTP ON"  
OUTP?  
"VKEY VALUE,9,STATE,1" (can be abbreviated to just "9")  
9 28 49 50 51 52 18 (select ARB and set freq to 1234Hz)  
9 23 49 28 (select ARB and set AMPL to 1Vpp)  
