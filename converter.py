# FILE: converter.py

temp = input('Enter a temperature: ')

conversion = raw_input('Convert to (F)ahrenheit or (C)elsius? ')

if conversion == 'F':
    temp1 = temp * 9
    temp2 = temp1 / 5
    temp3 = temp2 + 32
    print str(temp3)
elif conversion == 'C':
    temp1 = temp - 32
    temp2 = temp1 * 5
    temp3 = temp2 / 9
    print str(temp3)
else:
    print "Invalid input"
