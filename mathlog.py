# FILE: mathlog.py

file = open("log.txt", "a")

while 1:
	form = raw_input("(A)ddition, (S)ubtraction, (M)ultiplication, (D)ivision, or (Q)uit : ")

	if form == 'Q':
		break
	elif form == 'A':
		num1 = input("Enter first number : ")
		num2 = input("Enter second number : ")
		answer = num1 + num2
		print "The answer is " + str(answer)
		file.write("\n" + str(num1) + " + " + str(num2) + " = " + str(answer))

	elif form == 'S':
		num1 = input("Enter first number : ")
		num2 = input("Enter second number : ")
		answer = num1 - num2
		print "The answer is " + str(answer)
		file.write("\n" + str(num1) + " - " + str(num2) + " = " + str(answer))

	elif form == 'M':
		num1 = input("Enter first number : ")
		num2 = input("Enter second number : ")
		answer = num1 * num2
		print "The answer is " + str(answer)
		file.write("\n" + str(num1) + " x " + str(num2) + " = " + str(answer))

	elif form == 'D':
		num1 = input("Enter first number : ")
		num2 = input("Enter second number : ")
		answer = num1 / num2
		print "The answer is " + str(answer)
		file.write("\n" + str(num1) + " / " + str(num2) + " = " + str(answer))

	elif form == 'Q':
		break
		file.close()

	else:
		print "Invalid Input"
