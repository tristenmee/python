# FILE: guess.py

import random

number = random.randint(1,10)
guesses = 0

guess = input('Enter a number between 1 and 10: ')


while guesses < 1000:
	guess = input('Enter a number between 1 and 10: ')
	if guess > number:
		print "Your guess is too high."
		guesses = guesses + 1
	if guess < number:
		print "Your guess is too low."
		guesses = guesses + 1
	if guess == number:
		break

if guess == number:
	print "Correct!  You got it in " + str(guesses) + " tries."
