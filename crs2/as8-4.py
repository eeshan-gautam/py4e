#Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see if the word
#is already in the list and if not append it to the list.
#When the program completes, sort and print the resulting words in alphabetical order.

hand = open('romeo.txt')          #file is open
inp = hand.read().strip()                 #all text is in inp
wrd = list()                      #new list created
fwrd = list()
count1 = 0
count2 = 0

wrd = inp.split()                 #list with all words no filters
count1 = len(wrd)
#print ('list length of words in romeo file:', count1)
try:
    for ln in wrd:
        if wrd[count2] not in fwrd:
            fwrd.append(wrd[count2])
            count2 = count2 +1
        else:
            count2 = count2 +1
except:
        print('Error occured')

finally:
    fwrd.sort()
    print (fwrd)
