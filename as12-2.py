import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
#print(soup)
S = 0
tags = soup('span')
for tag in tags:
    #print('TAG', tag)
    #print('URL:',tag.get('href', None))
    #print('Contents:',tag.contents[0])
    r = tag.contents[0]
    #print(type(r))
    u = int (r)
    #print(type(u))
    S = S + u
    #print('Attrs:',tag.attrs)

print('sum of no.s=', S)
