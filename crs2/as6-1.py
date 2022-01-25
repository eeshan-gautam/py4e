text = "X-DSPAM-Confidence:    0.8475"
dec = text.find('.')
num = (text[dec-1:])

fnum = float(num)
print (fnum)
