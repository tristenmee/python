# FILE: Mathquiz.py
 
from random import randint 
 
correct = 0
 
duration = input("How many questions would you like to answer? ")
 
level = raw_input("What level, (E)asy, (M)edium, or (H)ard? ")
 
if level == 'E':
  for i in range(duration):
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    product = n1 * n2
    answer = input("What's" + str(n1) + " times " + str(n2) + "? ")
    if answer == product:
      print "That's right -- well done."
      correct = correct + 1
    else:
       print "No, I'm afraid the answer is " + str(product) + "."



if level == 'E':
  for i in range(duration):
    n1 = randint(1, 25)
    n2 = randint(1, 25)
    product = n1 * n2
    answer = input("What's" + str(n1) + " times " + str(n2) + "? ")
    if answer == product:
      print "That's right -- well done."
      correct = correct + 1
    else:
       print "No, I'm afraid the answer is " + str(product) + "."



if level == 'E':
  for i in range(duration):
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    product = n1 * n2
    answer = input("What's" + str(n1) + " times " + str(n2) + "? ")
    if answer == product:
      print "That's right -- well done."
      correct = correct + 1
    else:
       print "No, I'm afraid the answer is " + str(product) + "."



print "I asked you " + str(duration) + " questions.  You got " + str(correct) + " of them right.\n"
print "Well done!"
