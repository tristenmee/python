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



elif level == 'M':
	for i in range(25):
    		n1 = randint(1, 25)
    		n2 = randint(1, 25)
    		product = n1 * n2
    
    	answer = input("What's" + str(n1) + " times " + str(n2) + "? ")
    	if answer == product:
    	    print "That's right -- well done."
    	    correct = correct + 1
    	else:
    	    print "No, I'm afraid the answer is" + str(product) + "."



elif level == 'H':
	for i in range(100):
    		n1 = randint(1, 100)
    		n2 = randint(1, 100)
    		product = n1 * n2
    
    	answer = input("What's" + str(n1) + " times " + str(n2) + "? ")
    	if answer == product:
    	    print "That's right -- well done."
    	    correct = correct + 1
    	else:
    	    print "No, I'm afraid the answer is" + str(product) + "."
else:
	print "Invalid Input"



print "I asked you " + str(questions) + " questions.  You got " + str(correct) + " of them right.\n"
print "Well done!"
