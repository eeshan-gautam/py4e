#ask user input for Hours and Rate
hrs = input('Enter Number of hours')
fhrs = float (hrs)
rate = input('Enter hourly rate')
frate = float (rate)

#check if hours are more than 40
if fhrs > 40.0:
    gpay = frate*40 + frate*1.5*(fhrs-40)
else :
    gpay = frate*fhrs

print (gpay)
