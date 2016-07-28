# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
#In this assignment you will write a Python program to use urllib to read 
#the HTML from the data files below, and parse the data, extracting numbers and 
#compute the sum of the numbers in the file



import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
total = 0
num = None
count = 0
for tag in tags:
    # Look at the parts of a tag
    count = count + 1
    num = int(tag.contents[0])
    total = total + num
print 'Count',count
print 'Sum',total
    