#The program will prompt for a URL, read the XML data from that URL using urllib
#and then parse and extract the comment counts from the XML data,
#compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import re
lst = list()

#   Ask for User Input of xml URL
# http://py4e-data.dr-chuck.net/comments_42.xml
xrl = input('please enter the XML address to go to: ')
cmmnt_count= 0
# create a web-page handle
wphand = urllib.request.urlopen(xrl)
# iterate to count lines in webpage
lncount = 0
s= 0
a=0
nmbr = 0
wrds = None
nlist = list()
for line in wphand:
    # decode is being used to get rid of b'<skjnsdffjn>'n
    # print ('this is line',lncount,':',line)
    print ('this is line',lncount,':',line.decode())
    lncount = lncount+1

    #convert each line to string
    tring = str(line.decode().strip())
    print ('string=',tring)
    #count the number of comments in the page
    if tring == '<comment>':
        cmmnt_count= cmmnt_count+1
    elif tring.startswith('<count>'):
        #print ('!!number here',nmbr)
        nmbr = nmbr + 1
        pos = tring.find('/')
        nlist.append(tring[7:pos-1])
print (nlist)

for n in nlist:
    a = int(n)
    s = s + a
print(s)

print('number of comments:',cmmnt_count)
print('number of numbers:',nmbr)
