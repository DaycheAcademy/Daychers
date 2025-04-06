alphabet_string = "ABCDEFGHIJKLMNOPQRSTUVZ"

# method 1:
for i in range(len(alphabet_string)-1, -1, -1):
    print(alphabet_string[i], end=" ")


print()
print("-"*100)


# method 2:
for i in reversed(alphabet_string):
    print(i, end=" ")
