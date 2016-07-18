
#USER INPUT
#inp = raw_input('Europe floor?')
#usf = int(inp) + 1
#print "US floor",usf

#assignment 2.3

#hrs = raw_input("Enter Hours:")
#hrs = float(hrs)
#rate = raw_input("Enter pay rate:")
#rate = float(rate)
#pay = hrs * rate
#print pay

#conditional stuff
#x = 11
#if x < 10:
#	print 'Smaller'
#elif x == 11:
#	print 'Bigger'
#else:
#	print 'huge'
#print 'BANG DONE'

#try catch

#astr = 'Bob'
#try:
#	print 'Hello'
#	istr = int(astr)
#	print 'There'
#except:
#	istr = -1
#print 'Done',istr

#video exercise
	hrs = raw_input("Enter Hours:")
	hrs = float(hrs)
	rate = raw_input("Enter pay rate:")
	rate = float(rate)
if hrs > 40:
	over = hrs - 40
	pay1 = over * (1.5 * rate)
	pay = 40 * rate
	gross = pay + pay1
else:
	gross = hrs * rate
print gross
