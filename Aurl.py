#prompt for a URL, read the XML data from that URL using urllib and then parse and 
#extract the comment counts from the XML data, compute the sum of the numbers in the 
#file and enter the sum,


import urllib
import xml.etree.ElementTree as ET


add = 0
count = 0
while True:
	address = raw_input('Enter location: ')
	if len(address) > 1 == True:
		break
	else:
		print "valid url is needed"
		continue

url = address
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')


for item in lst:
	#print 'count', item.find('count').text
	x = int(item.find('count').text)
	add = add + x
	count = count + 1

print 'Count:',count
print 'Sum:',add
	
		
