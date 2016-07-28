#import re

#fhname = raw_input("Enter filename: ")
#fn = open(fhname)
#sum = 0
#z = list()
#for line in fn:
#	for i in line.split():
#		y = (re.findall('[0-9]+', i))
#		if len(y) == 1:
#			y[0] = int(y[0])
#			sum = sum + y[0]
#
#print "The sum of the numbers in the file are", sum

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('a')

for tag in tags:
	html = tag.get('href', None)
	print html
