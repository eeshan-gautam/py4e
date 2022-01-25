# Write a program that repeatedly prompts
# a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch
# it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

#infinite loop
mxi = 0
mni = 0
j = 0
while True:
#Get user Input for numbers

    n = input ('Enter int values and then done: ')
    j = j + 1
    if n == 'done':
        print ('Maximum is',mxi)
        print ('Minimum is',mni)
        break
    try:
        i = int (n)
        if (j == 1):
            mni = i
            mxi = i
        if (i > mxi):
            mxi = i
        elif (i < mni):
            mni = i

    except :
        print ("Invalid entry=")
