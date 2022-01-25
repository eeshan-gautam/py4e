#Write a program that prompts for a file name,
# then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.

fname = input('Enter the name of file to be opened: ')
filehandle = open(fname)
lm = ''
r= ''
count = 0
cumul = 0.0
avg = 0.0
for ln in filehandle:
    ln = ln.rstrip()
    if ln.startswith('X-DSPAM-Confidence:'):
        count = count +1
        dec = ln.find('.')
        lm =  (ln[dec-1:])
        fnum = float(lm)
        cumul = cumul + fnum
        #print (ln)
#print ('number of confidence values: ',count)
#print ("Sum of confidence's:" ,round(cumul,4))
print ('Average spam confidence:', cumul / count)
#print ("Average Confidence's: ", round(avg,4) )
