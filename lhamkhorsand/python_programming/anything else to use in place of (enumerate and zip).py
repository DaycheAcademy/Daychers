# using enumerate() function
alpha= 'ABCDEFGH'
for ind , val in enumerate( alpha,1):
    print('value of {} is {}'.format(ind,val)  )



print('-------------------------------- ')
# using zip() function
number=[1,2,3,4]
for num, char in zip(number, alpha):
    print(f'value of {num} is {char}')


print('-------------------------------- ')

# 1: using range(len())

for ind in range(1, len(alpha) + 1):
    print('value of {} is {}'.format(ind, alpha[ind - 1]))


print('-------------------------------- ')

# 2: using itertools.count()
from itertools import count

for ind , value in zip(count(1), alpha):
    print(f'value of {ind} is {value}')

print('-------------------------------- ')



# 3: using itertools.zip_longest()

from itertools import zip_longest

number = [1, 2, 3, 4]
alpha = 'ABCDEFGH'

for num, char in zip_longest(number, alpha, fillvalue=None):
    print(f'value of {num} is {char}')


