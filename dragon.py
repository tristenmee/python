# FILE: dragon.py

import random

print "Welcome to the Dragon game!"

duration = input("How many rounds would you like to play? ")
number = random.randint(1, 10)
correct = 0

dragon = """ 
                _/(               <~\  /~>               )\_
              .~   ~-.            /^-~~-^\            .-~   ~.
           .-~        ~-._       : /~\/~\ :       _.-~        ~-.
        .-~               ~~--.__: \0/\0/ ;__,--~~               ~-.
       /                        ./\. ^^ ./\.                        \
      .                         |  ( )( )  |                         .
      -~~--.        _.---._    /~   U`'U   ~\    _.---._        .--~~-
            ~-. .--~       ~~-|              |-~~       ~--. .-~
               ~              |  :        :  |_             ~
                              `\,'  :  :  `./' ~~--._
                             .(<___.'  `,___>),--.___~~-.
                             ~ (((( ~--~ ))))      _.~  _)
                                ~~~      ~~~/`.--~ _.--~
                                            \,~~~~~\n
          """


for i in range(duration):

	print dragon * number

	answer = input("How many dragons are present : ")

	if answer == number:
		print "Correct!"
		correct = correct + 1

	else:
		print "Incorrect!"

incorrect = duration - correct
print "You got " + str(correct) + " correct and " + str(incorrect) + " incorrect out of " + str(duration)
