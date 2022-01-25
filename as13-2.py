# The program will prompt for a URL, read the JSON data from that URL using urllib
# and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below:

import urllib.request, urllib.parse, urllib.error
import json
url = input('Enter the url to be opened')
print ('hello')

# Opening webpage to access data...
wphand = urllib.request.urlopen(url)
data = wphand.read().decode()
print (data)

#testing url: http://py4e-data.dr-chuck.net/comments_42.json
# final url: http://py4e-data.dr-chuck.net/comments_1213477.json
a=0
b=0
c=0
num = json.loads(data)

for n in data:
    try:
        print('index count:',a)
        print(num["comments"][a]["count"])
        b=num["comments"][a]["count"]
        c=int(b)+c
        a = a+1
    except:
        break

print('number:',num)
print('count of numbers:',a)
print (type(num))
print('sum of numbers',c)
#try:
#    print('48th number:',num["comments"][48]["count"])
#    print('49th number:',num["comments"][49]["count"])
#except:
#    print ('error printing')
