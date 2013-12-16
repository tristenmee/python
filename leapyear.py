# FILE: leapyear.py

year = input('Enter a year: ')

if year % 4 == 0:
    print str(year) + " is a leap year."
elif year % 4 != 0:
    print str(year) + " is not a leap year."
else:
    print "Invalid Input"
