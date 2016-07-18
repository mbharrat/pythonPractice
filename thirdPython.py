#text = "X-DSPAM-Confidence:    0.8475";
#x = text.find('0')
#print x
#text2 = text[23:]
#print text2
#textfinal = float(text2)
#rint type(textfinal)
#
#
#print out file with no extra lines in all caps
##
#fname = raw_input("Enter file name: ")
#fh = open(fname)

#for line in fh:
#	line = line.rstrip()
#	line = line.upper()
#	print line
#
#
#find average of x-dspam-confidence number
#
#
#fname = raw_input("Enter file name: ")
#fh = open(fname)
#count = 0
#total = 0.0
#for line in fh:
#	line = line.rstrip()
#	if not line.startswith("X-DSPAM-Confidence:") :
#		continue
#	else:
#		occur = line.find(':')
#		text = line[occur+1:]
#		text = text.strip()
#		text = float(text)
#		count = count + 1
#		total = total + text
#		average = total / count
#print"Average spam confidence:",average
#
#
#take file, split into just words, if not in list add word to list
#sort that list and return it
#fname = raw_input("Enter file name: ")
#fh = open(fname)
#stuff = list()
#for line in fh:
#	for word in line.split():
#		if word not in stuff:
#			stuff.append(word)
#			
#tuff.sort()
#print(stuff)
#
#
#
#take file, and print address found after From and end print out count
#fname = raw_input("Enter file name: ")
#fh = open(fname)
#count = 0
#stuff = list()
#for line in fh:
#	for word in line.split():
#		if word == 'From':
#			stuff = line.split()
#			count = count + 1
#			print(stuff[1])
#print "There were", count, "lines in the file with From as the first word"

#fhname = raw_input("Enter file name: ")
#fh = open(fhname)
#text = fh.read()
#words = text.split()
#wasFrom = -1
#counts = dict()
#for word in words:
#	if wasFrom == 0:
#		counts[word] = counts.get(word,0) + 1
#		wasFrom = -1		
#	if word == 'From':
#		wasFrom = 0
#bigWord = None
#bigCount = None
#for word,count in counts.items():
#	if bigCount is None or count > bigCount:
#		bigWord = word
#		bigCount = count
#print bigWord, bigCount
#
#
#python arrange by time
#
#fhname = raw_input("Enter file name: ")
#fh = open(fhname)
#stuff = list()
#final = list()
#counts = dict()
#for line in fh:
#	for word in line.split():
#		if word == 'From':
#			stuff = line.split(":",)
#			stuff = stuff[0].split()
#			counts[stuff[5]] = counts.get((stuff[5]), 0) + 1
#for key, val in counts.items():
#	final.append( (key, val))
#final.sort()

#for val, key in final:
#	print val, key	






		
		















