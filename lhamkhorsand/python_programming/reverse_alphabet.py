alphabets_string='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# using reversed() function
for char in reversed(alphabets_string):
    print(char)


#using range() function
for char in range(len(alphabets_string)-1, -1, -1):
    print(alphabets_string[char])


# using while loop and without using built-in functions
i = -1
while True:
    print(alphabets_string[i])
    if alphabets_string[i] == alphabets_string[0]:
        break
    i -= 1



