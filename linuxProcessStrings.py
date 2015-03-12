#!/usr/bin/env python
#Memory region parser based off of "Gilles" script here - http://unix.stackexchange.com/questions/6301/how-do-i-read-from-proc-pid-mem-under-linux

import re
import os
import signal
import sys

def parsemem(data):
	#find all ASCII strings > length 4 of characters
	return re.findall("[^\x00-\x1F\x7F-\xFF]{4,}", data)

def explore(processid):
	#Pause the process to examine
	os.kill(int(processid), signal.SIGSTOP)

	#Open the file of process memory maps
	maps_file = open("/proc/"+processid+"/maps", 'r')
	mem_file = open("/proc/"+processid+"/mem", 'r', 0)

	#Parse each region of a process memory and print it out
	for line in maps_file.readlines():  # for each mapped memory region in the process
		m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
		#only attempt if region is read-enabled
		if m.group(3) == 'r':
			#Start memory address
			start = long(m.group(1), 16)

			#Stop memory address
			end = long(m.group(2), 16)
			#Temporary fix for int overflow in the vsyscall region
			if start > sys.maxint:
				continue
			mem_file.seek(start)  #seek to region start
			chunk = mem_file.read(end - start)  # read region contents
			
			#print the list of matching strings to the regex
			for found_str in parsemem(chunk):
				print found_str
	#close maps and mem
	maps_file.close()
	mem_file.close()
	
	#Free the process
	os.kill(int(processid), signal.SIGCONT)

def main(argv):
	if len(argv) < 2:
		print "Syntax: ./linuxProcessStrings.py [PID]"
		return
	else:
		explore(argv[1])

if __name__ == "__main__":
    main(sys.argv)

