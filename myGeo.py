#In this program you will use a GeoLocation lookup API modelled after the 
#Google API to look up some universities and parse the returned data.



import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
	address = raw_input('Enter location: ')
	if len(address) < 1: break

	url = serviceurl + urllib.urlencode({'sensor':'false', 'address':address})
	print 'Retrieving',url
	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved',len(data),'characters'

	try: js = json.loads(str(data))
	except: js = None
	if 'status' not in js or js['status'] != 'OK':
		print' ==== Failure to Retrieve ===='
		print data
		continue
	#print json.dumps(js, ident=4)

	placeid = js["results"][0]['place_id']
	print 'Place id',placeid