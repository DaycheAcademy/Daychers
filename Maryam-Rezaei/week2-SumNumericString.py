numericString = '12,14.5,-455,237.8493,0.34343,-0.13'
numericStringList = numericString.split(',')
sumOfNumbers = 0

for i in numericStringList:
     sumOfNumbers += float(i)

print(sumOfNumbers)



