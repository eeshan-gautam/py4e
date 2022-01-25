import re
hand = open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    x=re.findall('\S+@\S+',line)
    if x:
      print (x)
