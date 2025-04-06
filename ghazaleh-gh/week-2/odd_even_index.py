odd_numbers = list()
even_numbers = list()


for odd, even in zip(range(1, 51, 2), range(2, 51, 2)):
    even_numbers.append(even)
    odd_numbers.append(odd)

print(f"odd numbers are: {odd_numbers}")
print(f"even numbers are: {even_numbers}")
