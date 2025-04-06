# numberString = "76,876532,9.356,0,0.23,-234,6,87586,987,142526353526353526, 6454737364654, -0.375"
# numberString = '34,0.86457,-23,0,876587,2,8'
#
# digits = '1234567890'
# signs = '-.'
# number = ''
# numbersList = []
# sumOfNumbers = 0
#
#
# for i in numberString:
#     if i in digits or i in signs:
#         number = number+i
#         # print(number)
#     elif i == ',':
#         # numbers_list.append(float(number))
#         numbersList = numbersList + [float(number)]  # instead of using method: .append()
#         number = ''
#         print(numbersList)
#         continue
#     elif i == ' ':  # for the space after ','
#         continue
#
# numbersList = numbersList + [float(number)]  # instead of using method: .append()
# print(numbersList)
#
# for num in numbersList:
#     sumOfNumbers += num
# # sumOfNumbers = sum(numbersList)
# print(f"sum of numbers in numberString is : {sumOfNumbers}")
#


# ---------------------------------------------------------------------------------------------
# using python functions
# numberString = '34,0.86457,-23,0,876587,2,8'
# stringList = numberString.split(',')
# numbersList = []
# for num in stringList:
#     numbersList.append(float(num))
# result = sum(numbersList)
# print(f"the list of numbers: {numbersList}\n sum of the numbers: {result}")


# ----------------------------------------------------------------------------------------------

numberString = '34,0.86457,-23,0,876587,2,8'
result = sum([float(num) for num in numberString.split(',')])
print(result)
