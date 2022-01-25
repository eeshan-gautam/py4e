# In this assignment you will write a Python program that expands on
# http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the
# HTML from the data files below, extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to
# the first name in the list, follow that link and repeat the process
# a number of times and report the last name you find.
#Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times.
# The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
#Last name in sequence: Anayah
#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Nakeisha.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times.
# The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: A
count = 0
ad=None
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
time= input('Enter number of times loop should run:')
t= int(time)
pos = input ('location to be copied:')
p = int(pos)
while count < t:

    if ad is None:
        url = input('Enter-')
    else:
        url = ad
        print('URL=',url)

    html= urllib.request.urlopen(url).read()
    soup = BeautifulSoup (html,'html.parser')
    n=1
    tags = soup('a')
    for tag in tags:
        print('line no.:',n,tag.get('href',None))
        if n==p :
            ad = tag.get('href',None)
            print('***address saved in ad: ',ad)
            break
        n= n +1
    count= count +1
    print( 'Process has run ',count,' times.')
#for ln in fhand:
        #print('Line Number:',a,line.decode().strip())
#        a=a+1
#        print (a)
