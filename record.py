# FILE record.py

name = raw_input("Enter a file to be read: ")

file = open(name, "r")

print file.readlines()

write = raw_input("Would you like to write this file? (Y) (N) ")

if write == 'Y':
	file = open(name, "w")
	line = input("Which line would you like to write? ")
	text = raw_input("Enter text to be written : ")
	file.write(text + "\n")
elif write == 'N':
	print "Goodbye then."
else:
	print "Input Invalid"
