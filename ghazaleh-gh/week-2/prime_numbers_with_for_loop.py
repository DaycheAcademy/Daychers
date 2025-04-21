from math import sqrt

for num in range(2, 1001):
    for i in range(2, round(sqrt(num))+1): # instead of: sqrt(num)+1 we could have used: (num)/2 + 1
        if not (num % i):
            break
    else:
        print(num, end=", ")
