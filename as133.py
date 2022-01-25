#In this assignment you will write a program that will prompt for a location, contact a web service and
#retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON.
#A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
#API End Points
#To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
#http://py4e-data.dr-chuck.net/json?
#This API uses the same parameter (address) as the Google API. This API also has no rate limit
#so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
#To call the API, you need to include a key= parameter and provide the address that you are requesting as
#the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function
#as shown in http://www.py4e.com/code3/geojson.py
#Make sure to check that your code is using the API endpoint is as shown above.
#You will get different results from the geojson and json endpoints so make sure you are using the
#same end point as this autograder is using.

#You can test to see if your program is working with a location of "South Federal University"
#which will have a place_id of "ChIJLzabHQ7i2IgRzeZb_AgUj0Q".

#$ python3 solution.py
#Enter location: South Federal University
#Retrieving http://...
#Retrieved 2146 characters
#Place id ChIJLzabHQ7i2IgRzeZb_AgUj0Q

#Turn In
#Please run your program to find the place_id for this location:
#University of Malaga
#Make sure to enter the name and case exactly as above and enter the place_id
#and your Python code below. Hint: The first seven characters of the place_id are "ChIJAQA ...
#Make sure to retreive the data from the URL specified above and not the normal Google API.
#Your program should work with the Google API - but the place_id may not match for this assignment.

import urllib.parse, urllib.request, urllib.error
import json
import ssl

api_key = False


websrv = 'http://py4e-data.dr-chuck.net/json?'
#websrv ='http://py4e-data.dr-chuck.net/comments_42.json'

ctx = ssl.create_defalut_context()
ctx.check_hostname = False
ctx/verify_mode = ssl.CERT_NONE

while True:
    location = input('****Enter the location to be searched::::: ')
    if len(location) <1:break

url = websrv + urllib.parse.urlencode({'Location':location})
print('Retrieving. . . ', url)
urlhand = urllib.request.urlopen(url)

data = urlhand.read().decode()
print('Retrieved',len(data))
print ('****Data on the Webpage::: ',data)

try:
    js = json.loads(data)
except :
    js = None
    print('none for js')

print('$%$^#&#&json =',js)
print('Place id',js['results'][0]['place_id'])
#print('****Unable to retrieve')
print(data)
