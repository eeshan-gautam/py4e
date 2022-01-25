#Write a program to read through the mbox-short.txt and
#figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of
#those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address
#to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary
#using a maximum loop to find the most prolific committer.

hndl = open('mbox-short.txt')
sndrs = dict()
words = list()
adrs = list()

for line in hndl:
    if line.startswith('From '):
#        print ('line being checked for from:- ',line)
        words = line.split()
#        print ('The splitted words are:- ',words)
        adrs.append(words[1])
        #print ('email address sending mail: ',adrs)

    else:
        continue
#print ("all sender's email adresses:- ", adrs)
for word in adrs:
    sndrs[word]= sndrs.get(word,0)+1
#print('counts', sndrs)
keymax = max(sndrs, key=sndrs.get)
print (keymax,max(sndrs.values()))    # maximum of all senders
#sndrs.keys()
#max(sndrs.values()))
print(sndrs) # print whole dictionary

for k in sndrs:
    print(k)

for k in sndrs:
    print (sndrs[k])

#for k in sndrs:
print( max(sndrs))
#print(k)
print(max(sndrs),max(sndrs.values()))
