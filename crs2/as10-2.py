#Write a program to read through the mbox-short.txt and figure out the distribution
#by hour of the day for each of the messages. You can pull the hour out from the
#'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

fhand = open('mbox-short.txt')
ls = list()
count = dict()
for ln in fhand:
    #print('line in fhand variable:' , fhand)
    if ln.startswith('From '):
#        print('the from ln: ', ln)
        words = ln.split()
        #print('words= ',words)
        time = words[5]
        #print ('full time = ', time)
        brokentime = time.split(':')
#        print ('after breaking time components:',brokentime)
        ls.append(brokentime[0])
    else:
        continue

#print ('list of hours: ', ls)
#print ('number of items in list: ',len(ls))
for w in ls:
#    print ('about to add a new hour in the list :',w)
    count[w] = count.get(w,0)+1
#print ('Collection of recieved hours:',count)

for k,v in sorted(count.items()):
 print (k,v)
