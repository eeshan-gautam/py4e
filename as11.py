#The basic outline of this problem is to read the file, look for integers using
#the re.findall(), looking for a regular expression of '[0-9]+' and then
#converting the extracted strings to integers and summing up the integers.
import re
#fhand = open('Regex_sum_42.txt')
fhand = open('Regex_sum_1213472.txt')
y = 0
b = 0
lst = list()
for ln in fhand:
    a = 0

    #x = 0
    #z=0
    #print ('reading now: ',ln)
    lst = re.findall('[0-9]+',ln)
    #print ('number(s) inside: ',lst)
    if len(lst) > 0:
            for n in lst:
                print ('nos till now: ',b)
                x = lst[a]
                a = a+1
                z = int(x)
                y = y +z
                b = b+1
    else : continue

print ('sum total= ',y)
print ('numbers present= ',b)
