
text = "ABCDEFGH"
print("Even-indexed elements:")
for i in range(0, len(text), 2):
    print(text[i])

print('='*40)
print("Odd-indexed elements:")
for i in range(1, len(text), 2):
    print(text[i])

