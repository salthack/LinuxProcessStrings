# LinuxProcessStrings
A forensic tool to parse strings out of a process's mapped memory on Linux

# Usage
Select the correct script: linuxProcessStrings.py (64-bit) or linuxProcessStrings32bit.py (32-bit).
Give the script execute rights (chmod 755 linuxProcessStrings.py)
sudo ./linuxProcessStrings.py [PID]
(The script must be run as root.)

# About
This will output any ASCII strings (greater than 4 characters) in the process's readable memory regions to the console.
The output can be piped to a file or through netcat.

Tested on Ubuntu 14.04 (64 bit) and Ubuntu 12.04 (32-bit)

Use at your own risk. Some processes do not take well to being paused.