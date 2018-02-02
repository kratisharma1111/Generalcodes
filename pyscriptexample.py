
"""
    pyscriptexample.py
    a small program to demonstrate the use of short python programs in bash shell command lines
    uses the sys model to gain access to stdin and stdout streams
    also uses sys to gain access to command line arguments  in sys.argv



"""

#!/usr/bin/env python  ## shebang line

##In computing, a shebang (also called a hashbang, hashpling, pound bang, or
##crunchbang) refers to the characters "#!" when they are the first two
##characters in an interpreter directive as the first line of a text file. In a
##Unix-like operating system, the program loader takes the presence of these two
##characters as an indication that the file is a script, and tries to execute
##that script using the interpreter specified by the rest of the first line in
##the file.


## import the sys modeul
import sys

##for a in sys.argv:
##	sys.stdout.write("%s\n"%a)
if len(sys.argv) < 2:
    sys.stdout.write("error - no command line text to search for\n")
    exit()
f= sys.argv[1]
i = 0
for text in sys.stdin.readlines():
	if text.find(f)>=0:
		sys.stdout.write("line %d %s"%(i,text))
	i += 1

