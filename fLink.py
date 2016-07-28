# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
##FOLLOWS LINKS IT HTML
#The program will use urllib to read the HTML from the data files 
#below, extract the href= vaues from the anchor tags, scan for a 
#tag that is in a particular position from the top and follow that link, 
#repeat the process a number of times, and report the last name you find.


import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
position=int(raw_input('Enter Position: '))
count=int(raw_input('Enter Count: '))
print 'Retrieving: ',url

#perform the loop "count" times.
for _ in xrange(0,count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags=soup('a')
    for tag in tags:
        url= tag.get('href')
        tags=soup('a')
        # if the link does not exist at that position, show error.
        if not tags[position-1]:
            print "A link does not exist at that position."
        # if the link at that position exist, overwrite it so the next search will use it.
        url = tags[position-1].get('href')
    print 'Retrieving: ',url

