# for loop    for odd and even
# 1: using range(len())
num='12345678'
for i in range(0, len(num), 2):
    print(num[i], num[i+1])



print('-------------------------------- ')

# 2: using zip()
for odd, even in zip(num[0::2], num[1::2]):
    print(odd, even)
