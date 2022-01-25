#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input("Enter Score: ")
fs = float (score)

if fs > 1 or fs <0 :
	msg = "Error: Score out of Range"
elif fs < 0.6:
	msg = "F"
elif fs < 0.7:
	msg = "D"
elif fs < 0.8:
	msg = "C"
elif fs < 0.9:
	msg = "B"
elif fs <= 1.0:
	msg = "A"
print (msg)
