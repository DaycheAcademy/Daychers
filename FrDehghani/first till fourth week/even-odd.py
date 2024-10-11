alphbetstring= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for even, odd in zip(alphbetstring[::2], alphbetstring[1::2]):
    print(even, odd)


print(alphbetstring[26:0:-1])
print(alphbetstring[-1:-27:-1])
print(alphbetstring[::-1])

for i in range(len(alphbetstring)):
    print(alphbetstring[-i - 1])
