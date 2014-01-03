# FILE: sentgen.py

import linecache
import random

while 1:
	answer = raw_input("(E)dit, (G)enerate, or (Q)uit : ")

	if answer == "E":
		name = raw_input("(adjective.txt) - (adverb.txt) - (article.txt) - (noun.txt) - (pronoun.txt) - (verb.txt)")
		file = open(name, "a")
		text = raw_input("Enter word to be added : ")
		file.write("\n" + str(text))
		file.close()

	if answer == "G":
		line_number1 = random.randint(1, 4)
		pronoun = linecache.getline("pronoun.txt", line_number1)

		line_number2 = random.randint(1, 74)
		adverb = linecache.getline("adverb.txt", line_number2)

		line_number3 = random.randint(1, 330)
		verb = linecache.getline("verb.txt", line_number3)

		line_number4 = random.randint(1, 2)
		article = linecache.getline("article.txt", line_number4)

		line_number5 = random.randint(1, 1134)
		adjective = linecache.getline("adjective.txt", line_number5)

		line_number6 = random.randint(1, 263)
		noun = linecache.getline("noun.txt", line_number6)

		print "\n                            " + (pronoun)
		print "\n                            " + (adverb)
		print "\n                            " + (verb)
		print "\n                            " + (article)
		print "                              " + (adjective)
		print "                            " + (noun)

	if answer == "Q":
		break
