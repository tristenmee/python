# File: non-repeatpass.py


#Imports random, choice, and time
import random
import time
from random import choice


#Sets the password that needs to be found
password = "89bd"


#Sets the number of password attempts
attempts = 0


#List that contains possible digits
possibleDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 


#Starts the clock
start = time.time()


while 1:


	#Picks a random digts from my possibleDigits list
	digit1 = choice(possibleDigits)
	digit2 = choice(possibleDigits)
	digit3 = choice(possibleDigits)
	digit4 = choice(possibleDigits)


	#Adds all the randomly generated digits together
	psuedoPassword = digit1 + digit2 + digit3 + digit4


	#Reads all the lines from passwords.txt and cheacks if psuedopass
	#is equal to any of the already tried passwords
	file = open("passwords.txt", "r")
	triedPasswords = file.readlines()
	

	#Checks passwords.txt to see if the pass has already been tried
	#and returns to the top of the loop if it is the same
	if psuedoPassword == triedPasswords:
		continue


	else:


		#Prints the made up password	
		print psuedoPassword


		#States that if the made up password is = to the real password
		#then it will break the loop and print the password  with the 
		#number of attempts and elapsed time, but if its not equal it 
		#will log it in passwords.txt and generate a new number
		if psuedoPassword == password:


			#Stops the time
			end = time.time()
			elapsed = end - start


			#Prints the password, attmepts, and time
			print "The password is " + psuedoPassword
			print "It took " + attemps + " tries and " + elapsed + " seconds."


			#Stops the time
			end = time.time()
			elapsed = end - start


			#Writes over the file
			file = open("passwords.txt", "w")
			file.write("")
			file.close


			#Breaks the loop
			break

		else:
			file = open("passwords.txt", "a")
			file.write(psuedoPassword + "\n")
			file.close
			attempts = attempts + 1
