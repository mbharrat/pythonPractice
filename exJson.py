#The program will prompt for a URL, read the JSON data from that URL 
#using urllib and then parse and extract the comment counts from the JSON data, 
#compute the sum of the numbers in the file.


import urllib
import json

add = 0
count = 0
while True:
	address = raw_input('Enter url: ')
	if len(address) > 1 == True:
		break
	else:
		print "valid url is needed"
		continue
url = address
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
info = json.loads(data)
#print type(info)
#print 'User count:', len(info)
#print json.dumps(info, indent=4)
#keep in mind info is a dictionary, and there are two objects note: and comments:
#your info is in comments: so in second object parse through second dict
for item in info['comments']:
	#print 'Count', item['count']
	count = count + 1
	add = add + item['count']
print 'Count:',count
print 'Sum:',add
