#score = raw_input("Enter Score: ")
#score = float(score)

#if score > 1.0 or score < 0.0:
#	print "Not in range"
#else:
#	if score >= 0.9:
#		print 'A'
#	elif score >= 0.8:
#		print 'B'
#	elif score >= 0.7:
#		print 'C'
#	elif score >= 0.6:
#		print 'D'
#	elif score < 0.6:
#		print 'F'

#4.6

#def computePay(h,r):
#	h = h - 40
#	grossPay = (h * (1.5*rate) + (40 * rate))
#	return grossPay

#hrs = raw_input("Enter Hours:")
#hrs = float(hrs)
#rate = raw_input("Enter Rate:")
#rate = float(rate)
#if hrs > 40:
#	p = computePay(hrs,rate)
#else:
#	p = hrs * rate
#print "Pay",p

#5.2
largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")

    if num == 'done' :
    	break
    else:
    	try:
    		num = int(num)
    	except:
    		num = -1

    	if num > 0:
    		if num > largest:
    			largest = num
    			if smallest == None:
    				smallest = num
    		elif num < smallest:
    			smallest = num
    	else:
    		print "Invalid input"
print "Minimum is", smallest
print "Maximum is", largest

