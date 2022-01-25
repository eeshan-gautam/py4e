# 7.1 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.

#enter file name

fh = input('Enter file name: ')
handle = open(fh)

for y in handle:
    y = y.rstrip()
    print (y.upper())
