# FILE: Mathquiz.py

from random import randint 
from goto import goto, comefrom, label

correct = 0
questions = 0

duration = input("How many questions would you like to answer?")

level = raw_input("What level, (E)asy, (M)edium, or (H)ard? ")

label .start
if level == 'E':
	for i in range(10):
   			n1 = randint(1, 10)
   			n2 = randint(1, 10)
   			product = n1 * n2
   			answer = input("What's" + str(n1) + " times " + str(n2) + "? ")
   	if answer == product:
   		    print "That's right -- well done."
   		    correct = correct + 1
   		    questions = questions + 1

   	elif duration >= questions:
   	    		goto .start


	else:
   	    print "No, I'm afraid the answer is" + str(product) + "."
   	    questions = questions + 1

   	    if duration >= questions:
   	    		goto .start
