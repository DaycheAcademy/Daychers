
def float_range(start, stop, step):
    while start < stop:
        yield round(start, 2)
        start += step


for num in float_range(2.3, 3.78, 0.01):
    print(num)


def alphabet_range(start, stop, step):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    start_idx = alphabet.index(start)
    stop_idx = alphabet.index(stop)

    for i in range(start_idx, stop_idx, step):
        yield alphabet[i]


# Example usage:
for letter in alphabet_range('c', 'x', 2):
    print(letter)
